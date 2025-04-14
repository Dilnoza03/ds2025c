class Node:
    def __init__(self, data, link=None):
        self.data = data  # значение (например, "Database")
        self.link = link   # ссылка на следующий узел


class Queue:
    def __init__(self):
        self.front = None  # первый элемент очереди
        self.rear = None  # последний элемент очереди
        self.size = 0  # количество элементов

    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None: # создаём новый узел
            self.front = node #если очередь пуста
            self.rear = node  # и начало, и конец — этот узел
        else:
            self.rear.link = node # связываем старый "хвост" с новым узлом
            self.rear = node   # новый "хвост" теперь — добавленный узел

q = Queue()
q.enqueue("Database")
q.enqueue("Data structure")
print(q.size, q.front.data, q.rear.data)
