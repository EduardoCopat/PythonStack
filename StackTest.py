__author__ = 'Eduardo'

import unittest
from Stack import Stack
from EmptyStackException import EmptyStackException



class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_element_size_1(self):
        self.stack.push("a")
        self.assertEqual(self.stack.size(), 1)

    def test_two_pushes_size_2(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.size(), 2)

    def test_two_pushes_one_pop(self):
        self.stack.push("a")
        self.stack.push("b")

        self.assertEqual(self.stack.pop(), "b")
        self.assertEqual(self.stack.size(), 1)

    def test_two_pushes_two_pop(self):
        self.stack.push("a")
        self.stack.push("b")
        self.stack.pop()

        self.assertEqual(self.stack.pop(), "a")
        self.assertEqual(self.stack.size(), 0)

    def test_empty_pop(self):
        self.assertRaises(EmptyStackException, self.stack.pop())





