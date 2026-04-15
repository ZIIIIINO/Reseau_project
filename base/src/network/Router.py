from simulator.SimulatedEntity import SimulatedEntity
from simulator.Simulator import Simulator
from network.NIC import NIC
from network.Packet import Packet
from network.Packet import PacketType


class Router(SimulatedEntity):
    def __init__(self, sim: Simulator, name: str):
        super().__init__(sim)
        self.name = name
        self._nics = [] #liste des nic du routeur (limité à 2 pour ce projet)

    def __repr__(self):
        return self.name

    def add_nic(self, nic: NIC):
        if len(self._nics) <= 2:
            self._nics.append(nic)
        else:
            raise Exception("Only 2 nic for a routeur")

    def receive(self, nic: NIC, pkt: Packet):
        if not(nic in self._nics):
            raise Exception("Nic is not associed with the router")
        receiver = self._nics[1] if nic == self._nics[0] else self._nics[0]
        receiver.send(pkt)