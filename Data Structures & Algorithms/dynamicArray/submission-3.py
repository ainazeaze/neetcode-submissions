class DynamicArray:
    
    def __init__(self, capacity: int):
        self.l = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        self.l[i] = n

    def pushback(self, n: int) -> None:
        self.l.append(n)
        while len(self.l) > self.capacity:
            self.resize()

    def popback(self) -> int:
        return self.l.pop(-1)
 
    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.l)
        
    def getCapacity(self) -> int:
        return self.capacity
