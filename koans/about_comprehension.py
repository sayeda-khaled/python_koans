#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutComprehension(Koan):

    #
    # def test_creating_lists_with_list_comprehensions(self):
    #     feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals',
    #         'fruit bats']
    #
    #     comprehension = [delicacy.capitalize() for delicacy in feast]
    #
    #     self.assertEqual(__, comprehension[0])
    #     self.assertEqual(__, comprehension[2])

    # https://www.geeksforgeeks.org/comprehensions-in-python/
    # Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:
    # List Comprehensions
    # Dictionary Comprehensions
    # Set Comprehensions
    # Generator Comprehensions
    #
    # List Comprehensions creates new lists. The following is the basic structure of a list comprehension:
    # output_list = [output_exp for var in input_list if (var satisfies this condition)]
    #
    # So this is created a new list and capitalized each word in the original list..


    def test_creating_lists_with_list_comprehensions(self):
        feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

        comprehension = [delicacy.capitalize() for delicacy in feast]

        self.assertEqual('Lambs', comprehension[0])
        self.assertEqual('Orangutans', comprehension[2])

    # def test_filtering_lists_with_list_comprehensions(self):
    #     feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
    #         'fruit bats']
    #
    #     comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]
    #
    #     self.assertEqual(__, len(feast))
    #     self.assertEqual(__, len(comprehension))

    # In this example, we created a new list that contains all the elements that has a length
    # of more than 6, which are 3.. the new list has not been changed

    def test_filtering_lists_with_list_comprehensions(self):
        feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

        comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

        self.assertEqual(5, len(feast))
        self.assertEqual(3, len(comprehension))
    #
    # def test_unpacking_tuples_in_list_comprehensions(self):
    #     list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
    #     comprehension = [ skit * number for number, skit in list_of_tuples ]
    #
    #     self.assertEqual(__, comprehension[0])
    #     self.assertEqual(__, comprehension[2])
    #
    # https://docs.python.org/3/tutorial/datastructures.html
    # https://www.geeksforgeeks.org/python-unpacking-nested-tuples/
    # https://realpython.com/list-comprehension-python/
    # new_list = [expression (if conditional) for member in iterable]


    def test_unpacking_tuples_in_list_comprehensions(self):
        list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
        comprehension = [ skit * number for number, skit in list_of_tuples ]

        self.assertEqual('lumberjack', comprehension[0])
        self.assertEqual('spamspamspamspam', comprehension[2])

    # def test_double_list_comprehension(self):
    #     list_of_eggs = ['poached egg', 'fried egg']
    #     list_of_meats = ['lite spam', 'ham spam', 'fried spam']
    #
    #
    #     comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]
    #
    #
    #     self.assertEqual(__, comprehension[0])
    #     self.assertEqual(__, len(comprehension))

    # https://book.pythontips.com/en/latest/comprehensions.html
    # https://stackoverflow.com/questions/1198777/double-iteration-in-list-comprehension
    # https://www.kite.com/python/answers/how-to-do-a-double-iteration-with-a-list-comprehension-in-python
    # https://www.w3schools.com/python/ref_string_format.asp
    # The format() method formats the specified value(s) and insert them inside the string's placeholder.
    # The placeholder is defined using curly brackets: {}.
    # https://www.geeksforgeeks.org/python-format-function/


    def test_double_list_comprehension(self):
        list_of_eggs = ['poached egg', 'fried egg']
        list_of_meats = ['lite spam', 'ham spam', 'fried spam']


        comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]


        self.assertEqual('poached egg and lite spam', comprehension[0])
        self.assertEqual(6, len(comprehension))


    # def test_creating_a_set_with_set_comprehension(self):
    #     comprehension = { x for x in 'aabbbcccc'}
    #
    #     self.assertEqual(__, comprehension)  # remember that set members are unique

    # as sets are unique and can not contain ayn duplicated, this will create only
    # unique letters..

    def test_creating_a_set_with_set_comprehension(self):
        comprehension = { x for x in 'aabbbcccc'}

        self.assertEqual({'a', 'c', 'b'}, comprehension)  # remember that set members are unique

    # def test_creating_a_dictionary_with_dictionary_comprehension(self):
    #     dict_of_weapons = {'first': 'fear', 'second': 'surprise',
    #                        'third':'ruthless efficiency', 'fourth':'fanatical devotion',
    #                        'fifth': None}
    #
    #     dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
    #
    #     self.assertEqual(__, 'first' in dict_comprehension)
    #     self.assertEqual(__, 'FIRST' in dict_comprehension)
    #     self.assertEqual(__, len(dict_of_weapons))
    #     self.assertEqual(__, len(dict_comprehension))

    # dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third': 'ruthless efficiency', 'fourth': 'fanatical devotion', 'fifth': None}
    # dict_comprehension = {'FIRST': 'fear', 'SECOND': 'surprise', 'THIRD': 'ruthless efficiency', 'FOURTH': 'fanatical devotion'}

    def test_creating_a_dictionary_with_dictionary_comprehension(self):
        dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                           'third':'ruthless efficiency', 'fourth':'fanatical devotion',
                           'fifth': None}

        dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

        self.assertEqual(False, 'first' in dict_comprehension)
        self.assertEqual(True, 'FIRST' in dict_comprehension)
        self.assertEqual(5, len(dict_of_weapons))
        self.assertEqual(4, len(dict_comprehension))
