from simulator.Simulator import Simulator
from network.Packet import Packet
from network.NIC import NIC
from network.ReliabilityMode import ReliabilityMode


class Host:
    TIMEOUT_DELAY = None

    sim = None
    name = None
    mode = None

    def __init__(self, sim: Simulator, name: str, mode: ReliabilityMode):

        self.sim = sim
        self.name = name
        self.mode = mode

    def add_nic(self, nic: NIC):
        self.nic = nic

    def send_data(self, data: str):
        
    def receive(self, nic: NIC, pkt: Packet):
        pass

    def get_received_data(self) -> str:
        pass

    def get_current_window_size(self) -> int:
        pass

    def get_total_retransmissions(self) -> int:
        pass
