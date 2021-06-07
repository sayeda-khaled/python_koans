#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    # def test_double_quoted_strings_are_strings(self):
    #     string = "Hello, world."
    #     self.assertEqual(__, isinstance(string, str))

    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # In Python, single or double quotes can be used with strings..
    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))


    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # In Python, single or double quotes can be used with strings..

    # def test_single_quoted_strings_are_also_strings(self):
    #     string = 'Goodbye, world.'
    #     self.assertEqual(__, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # In Python, trible double quotes are used for multiple lines..

    # def test_triple_quote_strings_are_also_strings(self):
    #     string = """Howdy, world!"""
    #     self.assertEqual(__, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))


    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # In Python,triple single quotes are used for multiple lines..

    # def test_triple_single_quotes_work_too(self):
    #     string = '''Bonjour tout le monde!'''
    #     self.assertEqual(__, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))



    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # A raw string tells Python to ignore all formatting within a string, including escape characters.
    # We create a raw string by putting an r in front of the string, right before the beginning quotation mark
    # By constructing a raw string by using r in front of a given string, we can retain backslashes and other
    # characters that are used as escape characters.

    # def test_raw_strings_are_also_strings(self):
    #     string = r"Konnichi wa, world!"
    #     self.assertEqual(__, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

    # https://www.geeksforgeeks.org/single-and-double-quotes-python/
    # Since we can use single quotes or double quotes within Python, it is simple to embed
    # quotes within a string by using double quotes within a string enclosed by single quotes:
    # This would print: He said, 'Go Away.'..
    # If we embed quotes within a string by using single quotes wihin a string enclosed by double
    # quotes, it will print: He said, "Go Away."
    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # we can use the escape character \" to add the quotation marks in a string
    # that is enclosed in double quotes

    # def test_use_single_quotes_to_create_string_with_double_quotes(self):
    #     string = 'He said, "Go Away."'
    #     self.assertEqual(__, string)

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual("He said, \"Go Away.\"", string)



    # def test_use_double_quotes_to_create_strings_with_single_quotes(self):
    #     string = "Don't"
    #     self.assertEqual(__, string)

    # https://www.geeksforgeeks.org/python-unittest-assertequal-function/
    # The above website, helped with understanding again, how asserEqual is structured
    # https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    # we can use the escape character \' to add an apostrophe in a string
    # that is enclosed in single quotes

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual('Don\'t', string)

    # Same information for the above 2 examples..
    # def test_use_backslash_for_escaping_quotes_in_strings(self):
    #     a = "He said, \"Don't\""
    #     b = 'He said, "Don\'t"'
    #     self.assertEqual(__, (a == b))

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))



#     def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
#         string = "It was the best of times,\n\
# It was the worst of times."
#         self.assertEqual(__, len(string))

    #https://www.w3schools.com/python/ref_func_len.asp
    #The len() function returns the number of items in an object.
    #When the object is a string, the len() function returns the number of characters in the string.

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))


    #def test_triple_quoted_strings_can_span_lines(self):
    #string = """
    # Howdy,
    # world!
    # """
    #self.assertEqual(__, len(string))
    #https://www.w3schools.com/python/ref_func_len.asp
    #https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    #When we use triple quotes, there will be a space at the top and
    #bottom when we print the string

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    #def test_triple_quoted_strings_need_less_escaping(self):
    #  a = "Hello \"world\"."
    #  b = """Hello "world"."""
    #  self.assertEqual(__, (a == b))

    #We only need to use escape characters if we are using double quotes and have a quotation or single
    #quotation and need ot use an apostrophe. With the triple quotes, we won't need to use the escaping
    #characters.
    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    # def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
    #     string = """Hello "world\""""
    #     self.assertEqual(__, string)

    #https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3
    #When we use triple quotes, we will see that there is a space at the top and bottom when we print the string.
    #We can remove those spaces by using the \ escape key.. The escape character here is to eliminate the space
    #at the bottom.

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

    #
    # def test_plus_concatenates_strings(self):
    #     string = "Hello, " + "world"
    #     self.assertEqual(__, string)

    #The plus sign here is concatenating the two strings..
    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)


    # def test_adjacent_strings_are_concatenated_automatically(self):
    #     string = "Hello" ", " "world"
    #     self.assertEqual(__, string)
    #https://docs.python.org/3/reference/lexical_analysis.html
    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)



    # def test_plus_will_not_modify_original_strings(self):
    #     hi = "Hello, "
    #     there = "world"
    #     string = hi + there
    #     self.assertEqual(__, hi)
    #     self.assertEqual(__, there)

    # https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/py-string.html
    # The + operator combines (aka "concatenates") two strings to make a bigger string.
    # This creates new strings to represent the result, leaving the original strings unchanged.

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)


    #def test_plus_equals_will_append_to_end_of_string(self):
    #    hi = "Hello, "
    #    there = "world"
    #    hi += there
    #    self.assertEqual(__, hi)
    #the += will append the string at the end and that will mutate the original string

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    # def test_plus_equals_also_leaves_original_string_unmodified(self):
    #     original = "Hello, "
    #     hi = original
    #     there = "world"
    #     hi += there
    #     self.assertEqual(__, original)
    #tested it in the console. The original string was not modified, only the string with the += operators

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)
    #
    # def test_most_strings_interpret_escape_characters(self):
    #     string = "\n"
    #     self.assertEqual('\n', string)
    #     self.assertEqual("""\n""", string)
    #     self.assertEqual(__, len(string))
    #Escape character is recognized by the string and the value is 1 for the string length.

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
