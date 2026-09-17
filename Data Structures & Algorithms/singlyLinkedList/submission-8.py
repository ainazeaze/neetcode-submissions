class LinkedList:
    def __init__(self):
        self.l = []

    def get(self, index: int) -> int:
        if len(self.l) == 0:
            return -1
        if index > len(self.l) - 1:
            return -1
        return self.l[index].value


    def insertHead(self, val: int) -> None:
        if len(self.l) > 0:
            node = ListNode(val, self.l[0])
        else:
            node = ListNode(val, None)
        self.l.insert(0, node)
        print([x.value for x in self.l])

    def insertTail(self, val: int) -> None:
        node = ListNode(val, None)
        if len(self.l) > 0:
            self.l[-1].next = node
        self.l.append(node)
        print([x.value for x in self.l])


    def remove(self, index: int) -> bool:
        if index == len(self.l) - 1:
            self.l[index - 1].next = None
            self.l.pop(index)
            return True 
        elif index < len(self.l) - 1:
            self.l[index - 1].next = self.l[index + 1]
            self.l.pop(index)
            return True
        return False

    def getValues(self) -> List[int]:
        return [x.value for x in self.l]


class ListNode:
    def __init__(self, value, next: ListNode):
        self.value = value
        self.next = next
