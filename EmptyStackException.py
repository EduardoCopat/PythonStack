__author__ = 'Eduardo'

class EmptyStackException(IndexError):
    def __init__(self):
        super(EmptyStackException, self).__init__()

