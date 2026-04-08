from enum import enum, auto

class PacketType(enum):
    DATA = auto()
    ACK = auto()

class Packet:
    seq_num = None
    is_ack = None
    payload = None
    size = None

    def _init__(
        self, seq_num: int, type: PacketType = PacketType.DATA, payload: str = ""
    ):
        self.seq_num = seq_num
        self.payload = payload

    def setSize(self, size: int):
        self.size = size
