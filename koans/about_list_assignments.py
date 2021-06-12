#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    # def test_non_parallel_assignment(self):
    #     names = ["John", "Smith"]
    #     self.assertEqual(__, names)
    # Assigning names to the list
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(['John', 'Smith'], names)


    #
    # def test_parallel_assignments(self):
    #     first_name, last_name = ["John", "Smith"]
    #     self.assertEqual(__, first_name)
    #     self.assertEqual(__, last_name)
    #
    # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
    # https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment
    # In Python, we can put a tuple of variables on the left side of an assignment operator (=)
    # and a tuple of values on the right side. The values on the right will be automatically assigned
    # to the variables on the left according to their position in the tuple. This is commonly known as
    # tuple unpacking in Python.

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)


    # def test_parallel_assignments_with_extra_values(self):
    #     title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
    #     self.assertEqual(__, title)
    #     self.assertEqual(__, first_names)
    #     self.assertEqual(__, last_name)

    # https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment
    # The * operator is known, in this context, as the tuple (or iterable) unpacking operator.
    # It extends the unpacking functionality to allow us to collect or pack multiple values in
    # a single variable. In

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(['Ricky', 'Bobby'], first_names)
        self.assertEqual("Worthington", last_name)

    # def test_parallel_assignments_with_sublists(self):
    #     first_name, last_name = [["Willie", "Rae"], "Johnson"]
    #     self.assertEqual(__, first_name)
    #     self.assertEqual(__, last_name)
    # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)

    # def test_swapping_with_parallel_assignment(self):
    #     first_name = "Roy"
    #     last_name = "Rob"
    #     first_name, last_name = last_name, first_name
    #     self.assertEqual(__, first_name)
    #     self.assertEqual(__, last_name)

    # https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment
    # In Python we can swap values between variables without using a temporary or auxiliary variable. 

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)
