__author__ = 'Eduardo'

class Stack(object):

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

