#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):

    # https://www.geeksforgeeks.org/declare-an-empty-list-in-python/
    # def test_creating_lists(self):
    #     empty_list = list()
    #     self.assertEqual(list, type(empty_list))
    #     self.assertEqual(__, len(empty_list))

    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))
    #
    # def test_list_literals(self):
    #     nums = list()
    #     self.assertEqual([], nums)
    #
    #     nums[0:] = [1]
    #     self.assertEqual([1], nums)
    #
    #     nums[1:] = [2]
    #     self.assertListEqual([1, __], nums)
    #
    #     nums.append(333)
    #     self.assertListEqual([1, 2, __], nums)

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

    # https://www.kite.com/python/docs/unittest.FunctionTestCase.assertListEqual
    # Tests that two lists are equal.

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

    # https://www.programiz.com/python-programming/methods/list/append
    # The append() method adds an item to the end of the list.
    # The syntax of the append() method is: list.append(item)
        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    # def test_accessing_list_elements(self):
    #     noms = ['peanut', 'butter', 'and', 'jelly']
    #
    #     self.assertEqual(__, noms[0])
    #     self.assertEqual(__, noms[3])
    #     self.assertEqual(__, noms[-1])
    #     self.assertEqual(__, noms[-3])

    # https://www.w3schools.com/python/gloss_python_access_list_items.asp
    # Python is a zero index based.. to access the elements at the end of the list,
    # you use a - and the index of the element
    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    # def test_slicing_lists(self):
    #     noms = ['peanut', 'butter', 'and', 'jelly']
    #
    #     self.assertEqual(__, noms[0:1])
    #     self.assertEqual(__, noms[0:2])
    #     self.assertEqual(__, noms[2:2])
    #     self.assertEqual(__, noms[2:20])
    #     self.assertEqual(__, noms[4:0])
    #     self.assertEqual(__, noms[4:100])
    #     self.assertEqual(__, noms[5:0])

    # https://www.geeksforgeeks.org/python-list-slicing/
    # https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
    # The full slice syntax is: start:stop:step. start refers to the index of the element which is used as a start
    # of our slice. stop refers to the index of the element we should stop just before to finish our slice.
    # if the index doesn't exist, the return will be an empty list

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])


    # def test_slicing_to_the_edge(self):
    #     noms = ['peanut', 'butter', 'and', 'jelly']
    #
    #     self.assertEqual(__, noms[2:])
    #     self.assertEqual(__, noms[:2])

    # https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
    # Slice notation allows you to skip any element of the full syntax.
    # If we skip the start number then it starts from 0 index:

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])

    # def test_lists_and_ranges(self):
    #     self.assertEqual(range, type(range(5)))
    #     self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
    #     self.assertEqual(__, list(range(5)))
    #     self.assertEqual(__, list(range(5, 9)))

    # https://www.programiz.com/python-programming/methods/built-in/range
    # range() returns an immutable sequence object of numbers depending upon the definitions used:
    # range(stop):
    # Returns a sequence of numbers starting from 0 to stop - 1
    # range(start, stop)

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        self.assertEqual([5, 6, 7, 8], list(range(5, 9)))

    # https://www.programiz.com/python-programming/methods/built-in/range
    # (list(range(start, stop, step)))
    # In the examples below, list(range(5, 3, -1)) creates a list that
    # starts at 5, subtract the values by 1, and ends at stop - 1

    # def test_ranges_with_steps(self):
    #     self.assertEqual(__, list(range(5, 3, -1)))
    #     self.assertEqual(__, list(range(0, 8, 2)))
    #     self.assertEqual(__, list(range(1, 8, 3)))
    #     self.assertEqual(__, list(range(5, -7, -4)))
    #     self.assertEqual(__, list(range(5, -8, -4)))


    def test_ranges_with_steps(self):
        self.assertEqual([5, 4], list(range(5, 3, -1)))
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))

    # def test_insertions(self):
    #     knight = ['you', 'shall', 'pass']
    #     knight.insert(2, 'not')
    #     self.assertEqual(__, knight)
    #
    #     knight.insert(0, 'Arthur')

    # https://www.programiz.com/python-programming/methods/list/insert
    # The insert() method takes two parameters:
    # index - the index where the element needs to be inserted
    # element - this is the element to be inserted in the list

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)

    # def test_popping_lists(self):
    #     stack = [10, 20, 30, 40]
    #     stack.append('last')
    #
    #     self.assertEqual(__, stack)
    #
    #     popped_value = stack.pop()
    #     self.assertEqual(__, popped_value)
    #     self.assertEqual(__, stack)
    #
    #     popped_value = stack.pop(1)
    #     self.assertEqual(__, popped_value)
    #     self.assertEqual(__, stack)

    # A 'push' is the same as an 'append' in python
    # pop(index) this is to pop the element with this index

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    # def test_making_queues(self):
    #     queue = [1, 2]
    #     queue.append('last')
    #
    #     self.assertEqual(__, queue)
    #
    #     popped_value = queue.pop(0)
    #     self.assertEqual(__, popped_value)
    #     self.assertEqual(__, queue)

        # https://www.geeksforgeeks.org/queue-in-python/

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.
