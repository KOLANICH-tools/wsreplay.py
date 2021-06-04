from pathlib import PurePath

from mitmproxy import io

from ..core import Stats, WebSocketMessage


def parseFlowFile(f, messagesPerPortAndPath):
	stats = Stats()
	freader = io.FlowReader(f)
	for fl in freader.stream():
		if fl.websocket:
			stats.socketCapturesTotal += 1
			p = PurePath(fl.request.path)
			messagesPerPath = messagesPerPortAndPath[fl.server_conn.address[1]]
			messages = messagesPerPath[p]
			for m in fl.websocket.messages:
				stats.messagesTotal += 1
				messages.append(WebSocketMessage(m.type, m.content, m.timestamp))
	del freader
	return stats
