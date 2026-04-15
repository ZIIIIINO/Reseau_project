from simulator.SimulatedEntity import SimulatedEntity
from simulator.Simulator import Simulator
from network.NIC import NIC
from network.Packet import Packet


class Router(SimulatedEntity):
    def __init__(self, sim: Simulator, name: str):
        super(sim)
        self.name = name
        self.nics = [] #liste des nic du routeur (limité à 2 pour ce projet)

    def __repr__(self):
        return self.name

    def add_nic(self, nic: NIC):
        if len(self.nics) < 2:
            self.nics.append(nic)
        else:
            raise Exception("Only 2 nic for a routeur")

    def receive(self, nic: NIC, pkt: Packet):
        if not(nic in self.nics):
            raise Exception("Nic is not associed with the router")
        receiver = self.nics[1] if nic == self.nics[0] else self.nics[0]
        receiver.send(pkt)