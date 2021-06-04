class Stats:
	__slots__ = (
		"messagesTotal",
		"socketCapturesTotal",
	)

	def __init__(self, messagesTotal: int = 0, socketCapturesTotal: int = 0):
		self.messagesTotal = messagesTotal
		self.socketCapturesTotal = socketCapturesTotal

	def __add__(self, other):
		return self.__class__(**{k: (getattr(self, k) + getattr(other, k)) for k in self.__class__.__slots__})

	def __radd__(self, other):
		for k in self.__class__.__slots__:
			setattr(self, k, getattr(self, k) + getattr(other, k))


class WebSocketMessage:
	__slots__ = ("opcode", "data", "timestamp")

	def __init__(self, opcode: int, data: bytes, timestamp: float):
		self.opcode = opcode
		self.data = data
		self.timestamp = timestamp
