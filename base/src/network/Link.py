from network.Packet import Packet
from simulator.Simulator import Simulator
from network.NIC import NIC


class Link:

    def __init__(self, name: str, distance: float, speed: float):
        self._nics = []
        self.name = name
        self.distance = distance
        self.speed = speed

    def attach(self, nic: NIC):
        if len(self._nics) <= 2:
            self._nics.append(nic)
        else:
            raise Exception("Only 2 nic for a routeur")

    def other(self, nic: NIC):

        if nic in self._nics:
            for el in self._nics:
                if el != nic:
                    return el
        raise Exception("interface don't exist")

    def should_lose(self, pkt: Packet) -> bool:
        return False
