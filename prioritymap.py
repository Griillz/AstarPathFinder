import heapq

class prioritymap:
    def __init__(self):
        self.queue = {}
        self.heap = []

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

    def heappush(self, cost):
        heapq.heappush(self.heap, cost)

    def heappop(self):
        return heapq.heappop(self.heap)


dict_obj = prioritymap()
print(dict_obj.isEmpty())
dict_obj.insert((200, 200), 5)
print(dict_obj.isEmpty())
print(dict_obj[(200, 200)])


