import heapq


class prioritymap:
    def __init__(self):
        self.queue = {}
        self.heap = []

    def __contains__(self, item):
        return item in self.queue

    def __str__(self):
        return ' '.join(str(i) for i in self.queue.items())

    def __getitem__(self, item):
        return self.queue[item]

    def __iter__(self, heap):
        return iter(self.heap)

    def __len__(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self) == 0

    def insert(self, key, data):
        self.queue[key] = data
        heapq.heappush(self.heap, key)

    def pop(self):
        remove1 = heapq.heappop(self.heap)
        remove2 = self.queue.pop(remove1)
        return remove1, remove2

    def min(self):
        return self.heap[0], self.queue[self.heap[0]]
