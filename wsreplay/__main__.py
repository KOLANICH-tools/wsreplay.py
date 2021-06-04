#!/usr/bin/env python3

import asyncio
import typing
from collections import defaultdict
from pathlib import Path, PurePath

import websockets.server
from plumbum import cli

from . import PathOrStrT, readCaptureFile
from .core import Stats


class CLI(cli.Application):
	"""Websocket replay server for mitmproxy. Please note that currently only basic stuff is implemented. It may make sense to implement mirroring whole connection options, like compression."""

	bindAddr = cli.SwitchAttr(["-b", "--bind", "--listen_host", "--listen-host"], default="127.0.0.1")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.messagesPerPortAndPath = defaultdict(lambda: defaultdict(list))
		self.stats = Stats()
		self.servers = ()

	def readCaptureFile(self, capFile: PathOrStrT):
		stats = readCaptureFile(capFile, self.messagesPerPortAndPath)
		self.stats += stats
		return stats

	def importCaptureFiles(self, captureFiles: typing.Iterable[PathOrStrT]):
		for capFile in captureFiles:
			stats = self.readCaptureFile(capFile)
			print("Imported " + str(capFile) + " : " + str(stats.messagesTotal) + " messages, " + str(stats.socketCapturesTotal) + " captures, " + str(len(self.messagesPerPortAndPath)) + " ports")

	async def replayer(self, websocket: websockets.server.WebSocketServerProtocol, path: str):
		path = PurePath(path)
		print("Connection:", websocket.port, path)

		messagesPerPath = self.messagesPerPortAndPath[websocket.port]
		messages = messagesPerPath[path]
		if not messages:
			return

		prevTs = messages[0].timestamp
		for m in messages:
			delay = m.timestamp - prevTs
			if delay > 0:
				await asyncio.sleep(delay)
			prevTs = m.timestamp
			await websocket.write_frame(True, m.opcode, m.data)

	def spawnAndRunServers(self):
		self.servers = []
		for port in self.messagesPerPortAndPath:
			self.servers.append(websockets.server.serve(self.replayer, self.bindAddr, port))

		l = asyncio.get_event_loop()
		try:
			l.run_until_complete(asyncio.gather(*self.servers))
			l.run_forever()
		except KeyboardInterrupt:
			print("Termination was requested.")

	def main(self, *captureFiles: str):  # cli.switches.ExistingFile causes the path to be absolute
		if not captureFiles:
			candidates = ("flows", "dump.har")
			thisDir = Path(".")
			for cand in candidates:
				cand = thisDir / cand
				if cand.is_file():
					captureFiles = (cand,)
					break

		self.importCaptureFiles(captureFiles)
		print("Starting server: " + str(sorted(self.messagesPerPortAndPath.keys())))
		self.spawnAndRunServers()


if __name__ == "__main__":
	CLI.run()
