class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        return
        current = self.head
        while current.next:
            current = current.next #move current
        current.next = Node(data)

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)


