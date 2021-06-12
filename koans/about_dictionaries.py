#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    # def test_creating_dictionaries(self):
    #     empty_dict = dict()
    #     self.assertEqual(dict, type(empty_dict))
    #     self.assertDictEqual({}, empty_dict)
    #     self.assertEqual(__, len(empty_dict))
    # https://pythonexamples.org/python-dictionary-length-example/
    # len() returns an integer representing the number of key:value pairs in the dictionary.

    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(0, len(empty_dict))

    # def test_dictionary_literals(self):
    #     empty_dict = {}
    #     self.assertEqual(dict, type(empty_dict))
    #     babel_fish = { 'one': 'uno', 'two': 'dos' }
    #     self.assertEqual(__, len(babel_fish))

    # https://www.geeksforgeeks.org/get-length-of-dictionary-in-python/
    # len(dict) provides the bumber of key:value pairs in teh dictionary

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(2, len(babel_fish))

    # def test_accessing_dictionaries(self):
    #     babel_fish = { 'one': 'uno', 'two': 'dos' }
    #     self.assertEqual(__, babel_fish['one'])
    #     self.assertEqual(__, babel_fish['two'])

    # https://www.tutorialspoint.com/python/python_dictionary.htm
    # To access dictionary elements, we use the square brackets along with the key to obtain its value

    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual('uno', babel_fish['one'])
        self.assertEqual('dos', babel_fish['two'])


    # def test_changing_dictionaries(self):
    #     babel_fish = { 'one': 'uno', 'two': 'dos' }
    #     babel_fish['one'] = 'eins'
    #
    #     expected = { 'two': 'dos', 'one': __ }
    #     self.assertDictEqual(expected, babel_fish)
    #
    # https://www.tutorialspoint.com/python/python_dictionary.htm
    # You can modify an existing entry in a  dictionary by adding a new key-value pair.

    def test_changing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        expected = { 'two': 'dos', 'one': 'eins' }
        self.assertDictEqual(expected, babel_fish)

    # def test_dictionary_is_unordered(self):
    #     dict1 = { 'one': 'uno', 'two': 'dos' }
    #     dict2 = { 'two': 'dos', 'one': 'uno' }
    #
    #     self.assertEqual(__, dict1 == dict2)

    # https://www.geeksforgeeks.org/regular-dictionary-vs-ordered-dictionary-in-python/
    # Dictionary in Python is an unordered collection of data values

    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(True, dict1 == dict2)


    # def test_dictionary_keys_and_values(self):
    #     babel_fish = {'one': 'uno', 'two': 'dos'}
    #     self.assertEqual(__, len(babel_fish.keys()))
    #     self.assertEqual(__, len(babel_fish.values()))
    #     self.assertEqual(__, 'one' in babel_fish.keys())
    #     self.assertEqual(__, 'two' in babel_fish.values())
    #     self.assertEqual(__, 'uno' in babel_fish.keys())
    #     self.assertEqual(__, 'dos' in babel_fish.values())

    # dictionary consist of key:value pairs
    # https://www.geeksforgeeks.org/python-dictionary/

    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys()))
        self.assertEqual(2, len(babel_fish.values()))
        self.assertEqual(True, 'one' in babel_fish.keys())
        self.assertEqual(False, 'two' in babel_fish.values())
        self.assertEqual(False, 'uno' in babel_fish.keys())
        self.assertEqual(True, 'dos' in babel_fish.values())

    # def test_making_a_dictionary_from_a_sequence_of_keys(self):
    #     cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)
    #
    #     self.assertEqual(__, len(cards))
    #     self.assertEqual(__, cards['green elf'])
    #     self.assertEqual(__, cards['yellow dwarf'])

    # https://codesource.io/how-to-create-dictionary-from-a-sequence-in-python/
    # The dict.fromkeys() method functions by creating a dictionary from a sequence of keys with value

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards))
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])
