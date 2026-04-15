from simulator.Simulator import Simulator
from network.Packet import Packet
from network.Packet import PacketType
from network.NIC import NIC
from network.ReliabilityMode import ReliabilityMode


class Host:
    TIMEOUT_DELAY = None

    def __init__(self, sim: Simulator, name: str, mode: ReliabilityMode):

        self.sim = sim
        self.name = name
        self.mode = mode
        self.buffer = []

    def add_nic(self, nic: NIC):
        self._nic = nic

    def send_data(self, data: str):
        for i in range(0 , len(data)):
            self._nic.send(Packet(None, PacketType.DATA, data[i]))

    def receive(self, nic: NIC, pkt: Packet):
        self.buffer.append(pkt)

    def get_received_data(self) -> str:
        return "".join(self.buffer)

    def get_current_window_size(self) -> int:
        return 0

    def get_total_retransmissions(self) -> int:
        return 0
