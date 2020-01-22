class prioritymap(object):
    def __init__(self):
        self.queue = {}

    def __str__(self):
        return ' '.join([tuple(i) for i in self.queue.values()])


    def isEmpty(self):
        return len(self.queue) == []


    def insert(self, key, data):
        self[key] = data


dict_obj = prioritymap()
print(dict_obj.isEmpty())
dict_obj.insert((200, 200), 5)
print(dict_obj.isEmpty())
print(dict_obj[(200, 200)])


