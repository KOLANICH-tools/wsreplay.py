from pathlib import PurePath
from urllib.parse import urlsplit

from ..core import Stats, WebSocketMessage

try:
	import ujson as json
except ImportError:
	import json


def parseFlowFile(f, messagesPerPortAndPath):
	j = json.load(f)

	stats = Stats()

	for e in j["log"]["entries"]:
		ms = e.get("_webSocketMessages", None)
		if ms:
			stats.socketCapturesTotal += 1
			pURI = urlsplit(e["request"]["url"])
			p = PurePath(pURI.path)
			messagesPerPath = messagesPerPortAndPath[pURI.port]
			messages = messagesPerPath[p]

			stats.messagesTotal += len(ms)
			for m in ms:
				opcode = m["opcode"]
				data = m["data"]
				if opcode == 1:
					data = data.encode("utf-8")
				elif opcode == 2:
					pass
				messages.append(WebSocketMessage(opcode, data, m["time"]))

	return stats
