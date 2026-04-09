from queue import Queue

from simulator.Simulator import Simulator
from simulator.SimulatedEntity import SimulatedEntity


class NIC(SimulatedEntity):
    rate = None
    queue_size = None
    sim = None
    name = None
    host = None

    def __init__(self, sim: Simulator, name: str, rate: float, queue_size: int = 0):
        super().__init__(sim)
        self.rate = rate
        self.queue_size = queue_size
        self.sim = sim
        self.name = name

        self.queue = Queue(queue_size)

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def queue_depth(self):
        return self.queue.nbrCurrent
