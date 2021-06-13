#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    # def test_use_format_to_interpolate_variables(self):
    #     value1 = 'one'
    #     value2 = 2
    #     string = "The values are {0} and {1}".format(value1, value2)
    #     self.assertEqual(__, string)

    # https://www.w3schools.com/python/ref_string_format.asp
    # https://www.geeksforgeeks.org/python-format-function/
    # The format() method formats the specified value(s) and insert them inside the string's placeholder.
    # The placeholder is defined using curly brackets: {}.

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)
    #
    # def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
    #     value1 = 'doh'
    #     value2 = 'DOH'
    #     string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
    #     self.assertEqual(__, string)

    # https://www.geeksforgeeks.org/python-format-function/
    # The order of the formatted valued, doesn't mattar or how many times it's used

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    # def test_any_python_expression_may_be_interpolated(self):
    #     import math # import a standard python module with math functions
    #
    #     decimal_places = 4
    #     string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
    #         decimal_places)
    #     self.assertEqual(__, string)

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

    # def test_you_can_get_a_substring_from_a_string(self):
    #     string = "Bacon, lettuce and tomato"
    #     self.assertEqual(__, string[7:10])

    # https://www.jquery-az.com/2-ways-get-python-substring-strings-5-examples/
    # You specify the start and end position of the source string to get the substring. The complete syntax is as follows:
    # object[start:stop:step]
    # Where:
    #     object is the source string (can be any sequence like list etc.)
    #     Start – the character where you want to get a substring from
    #     Stop – specifies the end position in the source string
    #     Step – the default is 1
    #     Parameters are enclosed in the square brackets
    #     Parameters are separated by colon

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10])

    # def test_you_can_get_a_single_character_from_a_string(self):
    #     string = "Bacon, lettuce and tomato"
    #     self.assertEqual(__, string[1])
    # https://www.jquery-az.com/2-ways-get-python-substring-strings-5-examples/
    # Specifying only a single index, gives us a single character
    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("a", string[1])

    # def test_single_characters_can_be_represented_by_integers(self):
    #     self.assertEqual(__, ord('a'))
    #     self.assertEqual(__, ord('b') == (ord('a') + 1))

    # https://www.geeksforgeeks.org/ord-function-python/
    # the ord() function accepts a string of unit length as an argument
    # and returns the Unicode equivalence of the passed argument.
    # Syntax: ord("string")
    # https://www.w3schools.com/python/ref_func_ord.asp
    # The ord() function returns the number representing the unicode code of a specified character.
    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))


    # def test_strings_can_be_split(self):
    #     string = "Sausage Egg Cheese"
    #     words = string.split()
    #     self.assertListEqual([__, __, __], words)
    # https://www.geeksforgeeks.org/python-string-split/
    # https://www.w3schools.com/python/ref_string_split.asp
    # The split() method splits a string into a list.

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(["Sausage", "Egg", "Cheese"], words)

    # def test_strings_can_be_split_with_different_patterns(self):
    #     import re #import python regular expression library
    #
    #     string = "the,rain;in,spain"
    #     pattern = re.compile(',|;')
    #
    #     words = pattern.split(string)
    #
    #     self.assertListEqual([__, __, __, __], words)
    #
    #     # Pattern is a Python regular expression pattern which matches ',' or ';'
    # https://docs.python.org/2/library/re.html#re.compile
    # Compile a regular expression pattern into a regular expression object
    # prog = re.compile(pattern)
    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'
    # https://www.journaldev.com/23598/python-raw-string#:~:text=Python%20raw%20string%20is%20created,treated%20as%20an%20escape%20character.
    # Python raw string is created by prefixing a string literal with ‘r’ or ‘R’. Python raw string treats backslash (\)
    # as a literal character. This is useful when we want to have a string that contains backslash and don’t want
    # it to be treated as an escape character.
    # Useful in regular expressions, file paths, URLs, etc.

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))


    # def test_strings_can_be_joined(self):
    #     words = ["Now", "is", "the", "time"]
    #     self.assertEqual(__, ' '.join(words))

    # https://www.geeksforgeeks.org/join-function-python/
    # The join() method is a string method and returns a string in which the elements of sequence
    # have been joined by str separator.
    # Syntax:
    # string_name.join(iterable)


    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words))
    #
    # def test_strings_can_change_case(self):
    #     self.assertEqual(__, 'guido'.capitalize())
    #     self.assertEqual(__, 'guido'.upper())
    #     self.assertEqual(__, 'TimBot'.lower())
    #     self.assertEqual(__, 'guido van rossum'.title())
    #     self.assertEqual(__, 'ToTaLlY aWeSoMe'.swapcase())

    # https://www.w3schools.com/python/ref_string_lower.asp
    # The lower() method returns a string where all characters are lower case. Symbols and Numbers are ignored.
    # https://www.w3schools.com/python/ref_string_upper.asp
    # The upper() method returns a string where all characters are in upper case. Symbols and Numbers are ignored.
    # https://www.w3schools.com/python/ref_string_capitalize.asp
    # The capitalize() method returns a string where the first character is upper case.
    # https://www.w3schools.com/python/ref_string_title.asp
    # The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
    # https://www.w3schools.com/python/ref_string_swapcase.asp
    # The swapcase() method returns a string where all the upper case letters are lower case and vice versa.


    def test_strings_can_change_case(self):
        self.assertEqual('Guido', 'guido'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', 'TimBot'.lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
