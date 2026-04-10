class Host:

    TIMEOUT_DELAY = None

    sim = None
    name = None
    mode = None


    def  __init__(self,sim:Simulator,name:str,mode:ReliabilityMode):

        self.sim = sim
        self.name = name
        self.mode = mode 
            
    def add_nic(self,nic:NIC):
        self.nic = nic

    def send_data(self, data: str):

    def  receive(self, nic: NIC, pkt: Packet):

    def get_received_data(self) -> str:

    def get_current_window_size(self) -> int : 

    def get_total_retransmissions(self) -> int : 
