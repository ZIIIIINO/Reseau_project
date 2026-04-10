from re import error
from src.network.Packet import Packet
from src.simulator.Simulator import Simulator
from src.network.NIC import NIC


class Link:
    speed = None
    distance = None
    name = None
    nics = []

    def __init__(self, name: str, distance: float, speed: float):
        self.name = name
        self.distance = distance
        self.speed = speed

    def attach(self, nic: NIC):
        self.nics.append(nic) if len(self.nics) < 2 else error("Only 2 nic for a link")

    def other(self, nic: NIC):

        if nic in self.nics:
            for el in self.nics:
                if el != nic:
                    return el
        error("interface don't exist")

    def should_lose(self, pkt: Packet) -> bool:
        return False
