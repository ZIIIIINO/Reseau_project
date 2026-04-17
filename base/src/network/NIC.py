from simulator.Simulator import Simulator
from simulator.SimulatedEntity import SimulatedEntity
from network.Packet import Packet
from collections import deque
from simulator.Event import Event


class NIC(SimulatedEntity):
    def __init__(self, sim: Simulator, name: str, rate: float, queue_size: int = 0):
        self.link = None
        self.host = None
        self.occupied = False
        super().__init__(sim)
        self.rate = rate
        self.queue_size = queue_size
        self.sim = sim
        self.name = name

        self.queue = []

    def send(self, pkt: Packet):

        if len(self.queue) <= self.queue_size:
            self.queue.append(pkt)

        self.sendTry()

    def sendTry(self):
        if len(self.queue) != 0:
            pkt = self.queue.pop(0)
            if (self.occupied == False) and (self.link != None):
                # Car envoie en bits
                tTransmission = (pkt.size / self.rate) * 8
                print(tTransmission)
                tPropagation = self.link.distance / self.link.speed
                print(tPropagation)
                self.sim.add_event(
                    Event(pkt, self.sendPacket), tTransmission + tPropagation
                )
                self.sim.add_event(Event(None, self.checkup), tPropagation)
                self.occupied = True

    def sendPacket(self, pkt: Packet):
        self.link.other(self).receive(pkt)

    def checkup(self, x=None):
        self.occupied = False
        self.sendTry()

    def receive(self, pkt: Packet):
        self.host.receive(self, pkt)

    def attach(self, link):
        self.link = link

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def queue_depth(self):
        return len(self.queue)
