from enum import enum, auto

class ReliabilityMode(enum):
    NO_RELIABILITY = auto()
    ACKNOWLEDGES = auto()
    ACKNOWLEDGES_WITH_RETRANSMISSION = auto()
    PIPELINING_FIXED_WINDOW = auto()
    PIPELINING_DYNAMIC_WINDOW = auto()