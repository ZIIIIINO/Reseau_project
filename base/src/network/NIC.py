from queue import Queue

from simulator.Simulator import Simulator
from simulator.SimulatedEntity import SimulatedEntity


class NIC(SimulatedEntity):
    queue = Queue()
    rate = None
    queue_size = None
    sim = None
    name = None

    def __init__(self, sim: Simulator, name: str, rate: float, queue_size: int = 0):
        super().__init__(sim)
        self.rate = rate
        self.queue_size = queue_size
        self.sim = sim
        self.name = name
