class MyCircularQueue:
    def __init__(self, k: int):
        self.list = [None] * k
        self.max = k
        self.fp = 0
        self.rp = 0
    def enQueue(self, value: int) -> bool:
        if self.list[self.rp] is None:
            self.list[self.rp] = value
            self.rp = (self.rp + 1) % self.max
            return True
        else:
            return False
    def deQueue(self) -> bool:
        if self.list[self.fp] is not None:
            self.list[self.fp] = None
            self.fp = (self.fp + 1) % self.max
            return True
        else:
            return False
    def Front(self) -> int:
        if self.list[self.fp] is not None:
            return self.list[self.fp]
        else:
            return -1
    def Rear(self) -> int:
        if self.list[self.rp - 1] is not None:
            return self.list[self.rp - 1]
        else:
            return -1
    def isEmpty(self) -> bool:
        for c in self.list:
            if c is not None:
                return False
        return True
    def isFull(self) -> bool:
        for c in self.list:
            if c is None:
                return False
        return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()