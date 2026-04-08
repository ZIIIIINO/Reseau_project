class link:
    queue = None  # Ou une strut comme liste chainée

    host = None

    def __init__(self, sim: Simulator, name: str, rate: float, queue_size: int = 0):
        return

    def send(self, pkt: Packet):
        return

    def attach(self, link: Link):
        return

    def set_host(self, host):
        self.host = host

    def get_host(self, host):
        return self.host

    def queue_depth(self):
        return
