from enum import Enum, auto


class PacketType(Enum):
    DATA = auto()
    ACK = auto()


class Packet:

    def __init__(
        self, seq_num: int, type: PacketType = PacketType.DATA, payload: str = ""
    ):
        self.seq_num = seq_num
        self.payload = payload
        self.is_ack = type == PacketType.ACK
        # si c'est packet ACK alors il fait 20 octet car il n'as pas de message
        self.size = 20 if self.is_ack else 21

