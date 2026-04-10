from src.simulator import SimulatedEntity
from src.simulator import Simulator
import src.network.Packet


class Routeur(SimulatedEntity):
    def __init__(self, sim: Simulator, name: str):
        super(sim)
        self.name = name

    def __repr__(self):
        return self.name

    def add_nic(self, nic: NIC):
        pass
        # TODO

    def receive(self, nic: NIC, pkt: Packet):
        pass
        # TODO

