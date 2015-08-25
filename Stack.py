__author__ = 'Eduardo'

from EmptyStackException import EmptyStackException

class Stack(object):

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop()
        except IndexError:
            raise EmptyStackException

    def size(self):
        return len(self.elements)