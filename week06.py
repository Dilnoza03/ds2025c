class Node:
    def __init__(self, data, link=None):
        self.data = data  # значение (например, "Database")
        self.link = link   # ссылка на следующий узел


class Queue:
    def __init__(self):
        self.front = None  # первый элемент очереди
        self.rear = None  # последний элемент очереди
        self.size = 0  # количество элементов

    def enqueue(self, data): #добовляет в очкередь
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node


    def dequeue(self): #это удаляет очередь
        if self.front is None:
            raise IndexError('Queue is empty')
        self.size = self.size - 1
        temp = self.front
        if self.front is None:
            self.rear = None
        temp.link = None
        return temp.data

q = Queue()
q.enqueue("Database")
q.enqueue("Data structure")
q.enqueue("Java script")
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front.data, q.rear.data)
# print(q.size, q.front, q.rear)
# print(q.dequeue())







