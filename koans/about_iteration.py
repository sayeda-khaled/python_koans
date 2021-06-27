#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    # def test_iterators_are_a_type(self):
    #     it = iter(range(1,6))
    #
    #     total = 0
    #
    #     for num in it:
    #         total += num
    #
    #     self.assertEqual(__ , total)
    # https://www.w3schools.com/python/python_iterators.asp
    # https://www.geeksforgeeks.org/iterators-in-python/
    # Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts,
    # and sets. The iterator object is initialized using the iter() method. It uses the next() method for
    # iteration.
    # __iter(iterable)__ method that is called for the initialization of an iterator.
    # This returns an iterator object

    def test_iterators_are_a_type(self):
        it = iter(range(1,6))

        total = 0

        for num in it:
            total += num

        self.assertEqual(15 , total)

    # def test_iterating_with_next(self):
    #     stages = iter(['alpha','beta','gamma'])
    #
    #     try:
    #         self.assertEqual(__, next(stages))
    #         next(stages)
    #         self.assertEqual(__, next(stages))
    #         next(stages)
    #     except StopIteration as ex:
    #         err_msg = 'Ran out of iterations'
    #
    #     self.assertRegex(err_msg, __)

    # https://www.geeksforgeeks.org/iterators-in-python/
    # The next method returns the next value for the iterable. When we use a for loop to traverse
    # any iterable object, internally it uses the iter() method to get an iterator object which
    # further uses next() method to iterate over. This method raises a StopIteration to signal
    # the end of the iteration.


    def test_iterating_with_next(self):
        stages = iter(['alpha','beta','gamma'])

        try:
            self.assertEqual('alpha', next(stages))
            next(stages)
            self.assertEqual('gamma', next(stages))
            next(stages)
        except StopIteration as ex:
            err_msg = 'Ran out of iterations'

        self.assertRegex(err_msg, 'Ran out of iterations')

    # ------------------------------------------------------------------
    #
    # def add_ten(self, item):
    #     return item + 10
    #
    # def test_map_transforms_elements_of_a_list(self):
    #     seq = [1, 2, 3]
    #     mapped_seq = list()
    #
    #     mapping = map(self.add_ten, seq)
    #
    #     self.assertNotEqual(list, mapping.__class__)
    #     self.assertEqual(__, mapping.__class__)
        # In Python 3 built in iterator funcs return iterable view objects
        # instead of lists

        # for item in mapping:
        #     mapped_seq.append(item)
        #
        # self.assertEqual(__, mapped_seq)

        # Note, iterator methods actually return objects of iter type in
        # python 3. In python 2 map() would give you a list.

    # https://www.geeksforgeeks.org/python-map-function/
    # map() function returns a map object(which is an iterator) of the results after applying the given
    # function to each item of a given iterable (list, tuple etc.)
    # Syntax :
    # map(fun, iter)
    # Parameters :
    # fun : It is a function to which map passes each element of given iterable.
    # iter : It is a iterable which is to be mapped.

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]
        mapped_seq = list()

        mapping = map(self.add_ten, seq)

        self.assertNotEqual(list, mapping.__class__)
        self.assertEqual(map, mapping.__class__)
        # In Python 3 built in iterator funcs return iterable view objects
        # instead of lists

        for item in mapping:
            mapped_seq.append(item)

        self.assertEqual([11,12,13], mapped_seq)

        # Note, iterator methods actually return objects of iter type in
        # python 3. In python 2 map() would give you a list.

    # def test_filter_selects_certain_items_from_a_list(self):
    #     def is_even(item):
    #         return (item % 2) == 0
    #
    #     seq = [1, 2, 3, 4, 5, 6]
    #     even_numbers = list()
    #
    #     for item in filter(is_even, seq):
    #         even_numbers.append(item)
    #
    #     self.assertEqual(__, even_numbers)

    # https://www.geeksforgeeks.org/filter-in-python/
    # The filter() method filters the given sequence with the help of a function that tests each
    # element in the sequence to be true or not.
    #
    # syntax:
    #
    # filter(function, sequence)
    # Parameters:
    # function: function that tests if each element of a
    # sequence true or not.
    # sequence: sequence which needs to be filtered, it can
    # be sets, lists, tuples, or containers of any iterators.
    # Returns:
    # returns an iterator that is already filtered.

    def test_filter_selects_certain_items_from_a_list(self):
        def is_even(item):
            return (item % 2) == 0

        seq = [1, 2, 3, 4, 5, 6]
        even_numbers = list()

        for item in filter(is_even, seq):
            even_numbers.append(item)

        self.assertEqual([2,4,6], even_numbers)

    # def test_filter_returns_all_items_matching_criterion(self):
    #     def is_big_name(item):
    #          return len(item) > 4
    #
    #     names = ["Jim", "Bill", "Clarence", "Doug", "Eli", "Elizabeth"]
    #     iterator = filter(is_big_name, names)
    #
    #     self.assertEqual(__, next(iterator))
    #     self.assertEqual(__, next(iterator))
    #
    #     try:
    #         next(iterator)
    #         pass
    #     except StopIteration:
    #         msg = 'Ran out of big names'
    #
    #     self.assertEquals(__, msg)

    # https://book.pythontips.com/en/latest/map_filter.html
    # filter creates a list of elements for which a function returns true.
    # The filter resembles a for loop but it is a builtin function and faster.
    #
    #
    # https://www.programiz.com/python-programming/methods/built-in/filter#:~:text=Python%20abs()-,Python%20filter(),to%20be%20true%20or%20not.

    def test_filter_returns_all_items_matching_criterion(self):
        def is_big_name(item):
             return len(item) > 4

        names = ["Jim", "Bill", "Clarence", "Doug", "Eli", "Elizabeth"]
        iterator = filter(is_big_name, names)

        self.assertEqual("Clarence", next(iterator))
        self.assertEqual('Elizabeth', next(iterator))

        try:
            next(iterator)
            pass
        except StopIteration:
            msg = 'Ran out of big names'

        self.assertEquals('Ran out of big names', msg)

    # ------------------------------------------------------------------

    # def add(self,accum,item):
    #     return accum + item
    #
    # def multiply(self,accum,item):
    #     return accum * item
    #
    # def test_reduce_will_blow_your_mind(self):
    #     import functools
    #     # As of Python 3 reduce() has been demoted from a builtin function
    #     # to the functools module.
    #
    #     result = functools.reduce(self.add, [2, 3, 4])
    #     self.assertEqual(__, result.__class__)
    #     # Reduce() syntax is same as Python 2
    #
    #     self.assertEqual(__, result)
    #
    #     result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
    #     self.assertEqual(__, result2)
    #
    #     # Extra Credit:
    #     # Describe in your own words what reduce does.

    # https://book.pythontips.com/en/latest/map_filter.html
    # Reduce is a really useful function for performing some computation on a list and returning the result.
    # It applies a rolling computation to sequential pairs of values in a list. For example,
    # if you wanted to compute the product of a list of integers.
    #
    # https://www.geeksforgeeks.org/reduce-in-python/
    # The reduce(fun,seq) function is used to apply a particular function passed in its argument
    # to all of the list elements mentioned in the sequence passed along.
    # This function is defined in “functools” module.
    # Working :
    # At first step, first two elements of sequence are picked and the result is obtained.
    # Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
    # This process continues till no more elements are left in the container.
    # The final returned result is returned and printed on console.

    def add(self,accum,item):
        return accum + item

    def multiply(self,accum,item):
        return accum * item

    def test_reduce_will_blow_your_mind(self):
        import functools
        # As of Python 3 reduce() has been demoted from a builtin function
        # to the functools module.

        result = functools.reduce(self.add, [2, 3, 4])
        self.assertEqual(int, result.__class__)
        # Reduce() syntax is same as Python 2

        self.assertEqual(9, result)

        result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
        self.assertEqual(24, result2)

        # Extra Credit:
        # Describe in your own words what reduce does.

    # ------------------------------------------------------------------
    #
    # def test_use_pass_for_iterations_with_no_body(self):
    #     for num in range(1,5):
    #         pass
    #
    #     self.assertEqual(__, num)

    # https://www.geeksforgeeks.org/break-continue-and-pass-in-python/
    # pass statement simply does nothing. The pass statement in Python is used when a statement
    # is required syntactically but you do not want any command or code to execute.
    # It is like null operation, as nothing will happen is it is executed.
    # Pass statement can also be used for writing empty loops.
    # Pass is also used for empty control statement, function and classes.

    def test_use_pass_for_iterations_with_no_body(self):
        for num in range(1,5):
            pass

        self.assertEqual(4, num)

    # ------------------------------------------------------------------
    #
    # def test_all_iteration_methods_work_on_any_sequence_not_just_lists(self):
    #     # Ranges are an iterable sequence
    #     result = map(self.add_ten, range(1,4))
    #     self.assertEqual(__, list(result))
    # https://realpython.com/python-map-function/

    def test_all_iteration_methods_work_on_any_sequence_not_just_lists(self):
        # Ranges are an iterable sequence
        result = map(self.add_ten, range(1,4))
        self.assertEqual([11,12,13], list(result))

    # def test_lines_in_a_file_are_iterable_sequences_too(self):
    #     def make_upcase(line):
    #         return line.strip().title()
    #
    #     file = open("example_file.txt")
    #     upcase_lines = map(make_upcase, file.readlines())
    #     self.assertEqual(__, list(upcase_lines))
    #     file.close()

    def test_lines_in_a_file_are_iterable_sequences_too(self):
        def make_upcase(line):
            return line.strip().title()

        file = open("example_file.txt")
        upcase_lines = map(make_upcase, file.readlines())
        self.assertEqual(['This', 'Is', 'A', 'Test'], list(upcase_lines))
        file.close()
