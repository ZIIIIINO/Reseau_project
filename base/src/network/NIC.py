from simulator.Simulator import Simulator
from simulator.SimulatedEntity import SimulatedEntity
from network.Packet import Packet
from collections import deque


class NIC(SimulatedEntity):
    rate = None
    queue = None
    queue_size = None
    sim = None
    name = None
    host = None
    link = None
    occupied = False

    def __init__(self, sim: Simulator, name: str, rate: float, queue_size: int = 0):
        super().__init__(sim)
        self.rate = rate
        self.queue_size = queue_size
        self.sim = sim
        self.name = name

        self.queue = Queue(queue_size)

    def Send(self, pkt: Packet):
        if occupied == False:
            tTransmission = pkt.size * self.rate
            tPropagation = self.link.distance / self.link.speed

            self.sim.add_event(Event(pkt, self.sendPacket), tTransmission)
            self.sim.add_event(Event(pkt, self.checkup), tPropagation)

    def sendPacket(pkt: Packet):
        self.link.other().receive(pkt)

    def checkup(x=None):
        self.occupied = True

    def receive(self, pkt: Packet):
        host.receive(self, pkt)

    def attach(self, link: Link):
        self.link = link

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def queue_depth(self):
        return
