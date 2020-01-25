class node:
    def __init__(self, children, parent):
        self.children = list(children)
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0