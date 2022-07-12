# we can use list for this but it has problems assiciated with dynamic list
from collections import deque


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    'company': 'WallMart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.1
})

pq.enqueue({
    'company': 'WallMart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 120
})

pq.enqueue({
    'company': 'WallMart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

# print(pq.buffer)
print(pq.dequeue())
