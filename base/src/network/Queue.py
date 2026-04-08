class Queue:
    queue = []
    nbrCurrent = 0
    size = 0

    def __init__(self, size: int):
        self.size = size

    def add(self, elem):
        if self.nbrCurrent < self.size:
            self.nbrCurrent += 1
            self.queue.append(elem)

    def pop(self):
        if self.nbrCurrent > 0:
            self.nbrCurrent -= 1
            return self.queue.pop()
