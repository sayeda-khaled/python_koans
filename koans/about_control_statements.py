#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutControlStatements(Koan):

    # def test_if_then_else_statements(self):
    #     if True:
    #         result = 'true value'
    #     else:
    #         result = 'false value'
    #     self.assertEqual(__, result)

    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        self.assertEqual('true value', result)


    # def test_if_then_statements(self):
    #     result = 'default value'
    #     if True:
    #         result = 'true value'
    #     self.assertEqual(__, result)


    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        self.assertEqual('true value', result)

    # def test_if_then_elif_else_statements(self):
    #     if False:
    #         result = 'first value'
    #     elif True:
    #         result = 'true value'
    #     else:
    #         result = 'default value'
    #     self.assertEqual(__, result)

    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        self.assertEqual( 'true value', result)

    # def test_while_statement(self):
    #     i = 1
    #     result = 1
    #     while i <= 10:
    #         result = result * i
    #         i += 1
    #     self.assertEqual(__, result)

    # While statement, whill continue to loop and multiply i * result for 10 times, and stops when i reaches 10
    # https://realpython.com/python-while-loop/
    # while <expr>:
    # <statement(s)>

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

    # def test_break_statement(self):
    #     i = 1
    #     result = 1
    #     while True:
    #         if i > 10: break
    #         result = result * i
    #         i += 1
    #     self.assertEqual(__, result)

    # https://realpython.com/python-while-loop/
    # The Python break statement immediately terminates a loop entirely.
    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

    # def test_continue_statement(self):
    #     i = 0
    #     result = []
    #     while i < 10:
    #         i += 1
    #         if (i % 2) == 0: continue
    #         result.append(i)
    #     self.assertEqual(__, result)

    # https://towardsdatascience.com/append-in-python-41c37453400
    #
    # The append() method in python adds a single item to the existing list.
    # It doesn’t return a new list of items but will modify the original list
    # by adding the item to the end of the list.

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        self.assertEqual([1, 3, 5, 7, 9], result)

    # def test_for_statement(self):
    #     phrase = ["fish", "and", "chips"]
    #     result = []
    #     for item in phrase:
    #         result.append(item.upper())
    #     self.assertEqual([__, __, __], result)

    # https://www.geeksforgeeks.org/python-convert-case-of-elements-in-a-list-of-strings/
    # item.upper() convert all string from lowercase to uppercase

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        self.assertEqual(["FISH", "AND", "CHIPS"], result)

    # def test_for_statement_with_tuples(self):
    #     round_table = [
    #         ("Lancelot", "Blue"),
    #         ("Galahad", "I don't know!"),
    #         ("Robin", "Blue! I mean Green!"),
    #         ("Arthur", "Is that an African Swallow or European Swallow?")
    #     ]
    #     result = []
    #     for knight, answer in round_table:
    #         result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")
    #
    #     text = __
    #
    #     self.assertRegex(result[2], text)
    #
    #     self.assertNotRegex(result[0], text)
    #     self.assertNotRegex(result[1], text)
    #     self.assertNotRegex(result[3], text)

    # https://www.w3schools.com/python/python_tuples.asp
    # Tuples are used to store multiple items in a single variable.
    # Tuple is one of 4 built-in data types in Python used to store collections of data,
    # the other 3 are List, Set, and Dictionary, all with different qualities and usage.
    # A tuple is a collection which is ordered and unchangeable.
    # Tuples are written with round brackets.

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")

        text = "Blue! I mean Green!"

        self.assertRegex(result[2], text)

        self.assertNotRegex(result[0], text)
        self.assertNotRegex(result[1], text)
        self.assertNotRegex(result[3], text)
