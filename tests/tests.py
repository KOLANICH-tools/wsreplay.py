import asyncio
import json
import sys
import unittest
from pathlib import Path
from threading import Event, Thread
from time import sleep
from urllib.parse import urlsplit

import sh
import websockets

cwd = Path(".").absolute()
thisDir = Path(__file__).parent.absolute().relative_to(cwd)
harFilePath = thisDir / "dump.har"


class Tests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		harJSON = json.loads(harFilePath.read_text())
		wsConnJSON = harJSON["log"]["entries"][0]
		cls.port = urlsplit(wsConnJSON["request"]["url"]).port
		cls.wsMessages = wsConnJSON["_webSocketMessages"]

		evt = Event()

		cls.startWSReplayServerCmd = sh.Command(sys.executable).bake(m="wsreplay")

		isStarted = False

		def process_output(line):
			nonlocal isStarted
			if not isStarted:
				if line.startswith("Imported"):
					print("The server has started.\n" + line)
					if line != "Imported " + str(harFilePath) + " : 5 messages, 1 captures, 1 ports\n":
						cls.serverProcess.kill()
						evt.set()
						raise ValueError("Unexpected start up message", repr(line))
					isStarted = True
					evt.set()

		cls.serverProcess = cls.startWSReplayServerCmd(str(harFilePath), _bg=True, _out=process_output)
		while not evt.wait():
			print("Waiting for server startup")

	@classmethod
	def tearDownClass(cls):
		cls.serverProcess.kill()

	def testHAR(self):
		try:

			async def asyncTestFunc():
				uri = "ws://localhost:" + str(self.__class__.port)
				async with websockets.connect(uri) as websocket:
					for jMsg in self.__class__.wsMessages:
						etalonRes = jMsg["data"]
						self.assertEqual(await websocket.recv(), etalonRes)

			asyncio.get_event_loop().run_until_complete(asyncTestFunc())
		except websockets.exceptions.ConnectionClosedOK:
			pass


if __name__ == "__main__":
	unittest.main()
