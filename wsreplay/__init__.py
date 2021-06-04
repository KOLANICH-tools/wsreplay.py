#!/usr/bin/env python3

import asyncio
import typing
from collections import defaultdict
from pathlib import Path, PurePath

import websockets.server
from plumbum import cli

PathOrStrT = typing.Union[Path, str]


def readCaptureFile(capFile: PathOrStrT, messagesPerPortAndPath):
	capFile = Path(capFile)
	# pylint: disable=import-outside-toplevel
	with capFile.open("rb") as f:
		startChar = f.read(1)
		f.seek(0)
		if startChar == b"{":
			from .backends.har import parseFlowFile as readHARFile

			return readHARFile(f, messagesPerPortAndPath)

		from .backends.mitmproxy import parseFlowFile as readMitmproxyFile

		return readMitmproxyFile(f, messagesPerPortAndPath)
