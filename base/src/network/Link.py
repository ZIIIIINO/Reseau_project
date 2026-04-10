from network.Packet import Packet
from simulator.Simulator import Simulator
from network.NIC import NIC


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
        if len(self.nics) < 2:
            self.nics.append(nic)
        else:
            raise Exception("Only 2 nic for a routeur")

    def other(self, nic: NIC):

        if nic in self.nics:
            for el in self.nics:
                if el != nic:
                    return el
        raise Exception("interface don't exist")

    def should_lose(self, pkt: Packet) -> bool:
        return False
