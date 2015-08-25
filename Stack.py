__author__ = 'Eduardo'

class Stack(object):

    def __init__(self):
        self.stack_size = 0

    def push(self, element):
        self.stack_size += 1

    def pop(self):
        self.stack_size -= 1
        return "b"

    def size(self):
        return self.stack_size
