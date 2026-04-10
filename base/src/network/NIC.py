from simulator.Simulator import Simulator
from simulator.SimulatedEntity import SimulatedEntity
from network.Packet import Packet


class NIC(SimulatedEntity):
    rate = None
    queue_size = None
    sim = None
    name = None
    host = None
    link = None

    def __init__(self, sim: Simulator, name: str, rate: float, queue_size: int = 0):
        super().__init__(sim)
        self.rate = rate
        self.queue_size = queue_size
        self.sim = sim
        self.name = name

        self.queue = Queue(queue_size)

    def Send(self, pkt: Packet):
        return

    def receive(self, pkt: Packet):
        host.receive(self, pkt)

    def attach(self, link: Link):
        self.link=link

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def queue_depth(self):
        return self.queue.nbrCurrent
