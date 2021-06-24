#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    # def test_sets_make_keep_lists_unique(self):
    #     highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']
    #
    #     there_can_only_be_only_one = set(highlanders)
    #
    #     self.assertEqual(__, there_can_only_be_only_one)


    # https://www.w3schools.com/python/python_lists.asp
    # Lists are used to store multiple items in a single variable.
    # Lists are one of 4 built-in data types in Python used to store collections of data,
    # the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
    # Lists are created using square brackets.
    #
    # List items are ordered, changeable, and allow duplicate values.
    # List items are indexed, the first item has index [0], the second item has index [1] etc.
    #
    # https://www.w3schools.com/python/python_sets.asp
    # Sets are used to store multiple items in a single variable.
    # A set is a collection which is both unordered and unindexed.
    # Sets are written with curly brackets.
    # Set Items:
    # Set items are unordered, unchangeable, and do not allow duplicate values.

    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual({'MacLeod','Ramirez', 'Matunas', 'Malcolm'},  there_can_only_be_only_one)

    # def test_empty_sets_have_different_syntax_to_populated_sets(self):
    #     self.assertEqual(__, {1, 2, 3})
    #     self.assertEqual(__, set())

    #to create an empty set, use the following syntax: set= set()

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual({1, 2, 3}, {1, 2, 3})
        self.assertEqual(set(), set())

    # def test_dictionaries_and_sets_use_same_curly_braces(self):
    #     # Note: Literal sets using braces were introduced in python 3.
    #     #       They were also backported to python 2.7.
    #
    #     self.assertEqual(__, {1, 2, 3}.__class__)
    #     self.assertEqual(__, {'one': 1, 'two': 2}.__class__)
    #
    #     self.assertEqual(__, {}.__class__)

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.
        #
        # https://stackoverflow.com/questions/36674083/why-is-it-possible-to-replace-sometimes-set-with
        # Python sets and dictionaries can both be constructed using curly braces:
        # The interpreter (and human readers) can distinguish between them based on their contents.
        # However it isn't possible to distinguish between an empty set and an empty dict,
        # so this case you need to use set() for empty sets to disambiguate.

        self.assertEqual(set, {1, 2, 3}.__class__)
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__)

        self.assertEqual(dict, {}.__class__)

    # def test_creating_sets_using_strings(self):
    #     self.assertEqual(__, {'12345'})
    #     self.assertEqual(__, set('12345'))

    # https://www.geeksforgeeks.org/python-sets/

    def test_creating_sets_using_strings(self):
        self.assertEqual({'12345'}, {'12345'})
        self.assertEqual({'1', '2', '3', '4', '5'}, set('12345'))
    #
    # def test_convert_the_set_into_a_list_to_sort_it(self):
    #     self.assertEqual(__, sorted(set('12345')))

    # https://www.geeksforgeeks.org/python-convert-set-into-a-list/
    # There are multiple ways to convert a set into a list..
    # one way by using: sorted() method..

    # A set is a collection which is unordered and unindexed, and doesnt allow duplicates.
    # In Python, sets are written with curly brackets. A list is a collection which is ordered and changeable.
    # In Python lists are written with square brackets

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('12345')))

    # ------------------------------------------------------------------

    # def test_set_have_arithmetic_operators(self):
    #     scotsmen = {'MacLeod', 'Wallace', 'Willie'}
    #     warriors = {'MacLeod', 'Wallace', 'Leonidas'}
    #
    #     self.assertEqual(__, scotsmen - warriors)
    #     self.assertEqual(__, scotsmen | warriors)
    #     self.assertEqual(__, scotsmen & warriors)
    #     self.assertEqual(__, scotsmen ^ warriors)
    # https://docs.python.org/2/library/sets.html

    # https://www.geeksforgeeks.org/python-arithmetic-operators/
    # Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.
    # There are 7 arithmetic operators in Python :
    # Addition
    # Subtraction
    # Multiplication
    # Division
    # Modulus
    # Exponentiation
    # Floor division

    # https://realpython.com/python-sets/#operating-on-a-set
    # the - operator in the set, return set of all elements that are in first setbut not in the second
    # the | operator, merges the two sets, without duplication
    # & Compute the intersection of two or more sets.
    # & return the set of elements common to both first set and second set..
    # ^  operator returns the elements that are unique to each set..
    # The ^ operator also allows more than two sets



    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual({'Willie'}, scotsmen - warriors)
        self.assertEqual({'MacLeod', 'Wallace', 'Willie', 'Leonidas'}, scotsmen | warriors)
        self.assertEqual({'MacLeod', 'Wallace'}, scotsmen & warriors)
        self.assertEqual({'Willie', 'Leonidas'}, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    # def test_we_can_query_set_membership(self):
    #     self.assertEqual(__, 127 in {127, 0, 0, 1} )
    #     self.assertEqual(__, 'cow' not in set('apocalypse now') )

    # https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/
    # Membership operators are operators used to validate the membership of a value.
    # It test for membership in a sequence, such as strings, lists, or tuples.
    # in operator : The ‘in’ operator is used to check if a value exists in a sequence or not.
    # Evaluates to true if it finds a variable in the specified sequence and false otherwise.

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
        self.assertEqual(True, 'cow' not in set('apocalypse now') )
    #
    # def test_we_can_compare_subsets(self):
    #     self.assertEqual(__, set('cake') <= set('cherry cake'))
    #     self.assertEqual(__, set('cake').issubset(set('cherry cake')) )
    #
    #     self.assertEqual(__, set('cake') > set('pie'))

    # https://www.geeksforgeeks.org/python-check-if-one-list-is-subset-of-other/
    #
    # Using set.issubset()
    # The most used and recommended method to check for a sublist.
    # This function is tailor made to perform the particular task of checking if
    # one list is a subset of another.

    # https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch16s04.html
    # Therera re a number of set comparisons.
    # All of the standard comparisons (<, <=, >, >=, ==, !=, in , not in ) work with sets,
    # but the interpretation of the operators is based on set theory. For example, the comparisons
    # determine if we have subset or superset (<=, >=) relationships between two sets.

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) )

        self.assertEqual(False, set('cake') > set('pie'))
