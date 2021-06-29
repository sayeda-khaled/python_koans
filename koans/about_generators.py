#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Written in place of AboutBlocks in the Ruby Koans
#
# Note: Both blocks and generators use a yield keyword, but they behave
# a lot differently
#

from runner.koan import *

class AboutGenerators(Koan):

    # def test_generating_values_on_the_fly(self):
    #     result = list()
    #     bacon_generator = (n + ' bacon' for n in ['crunchy','veggie','danish'])
    #
    #     for bacon in bacon_generator:
    #         result.append(bacon)
    #
    #     self.assertEqual(__, result)

    # https://www.learnpython.org/en/Generators
    # https://book.pythontips.com/en/latest/generators.html
    # Generators are iterators, but you can only iterate over them once. It’s because they do not store
    # all the values in memory, they generate the values on the fly. You use them by iterating over them,
    # either with a ‘for’ loop or by passing them to any function or construct that iterates.
    # Most of the time generators are implemented as functions. However, they do not return a value,
    # they yield it.
    # Generators are best for calculating large sets of results

    def test_generating_values_on_the_fly(self):
        result = list()
        bacon_generator = (n + ' bacon' for n in ['crunchy','veggie','danish'])

        for bacon in bacon_generator:
            result.append(bacon)

        self.assertEqual(['crunchy bacon', 'veggie bacon', 'danish bacon'], result)

    # def test_generators_are_different_to_list_comprehensions(self):
    #     num_list = [x*2 for x in range(1,3)]
    #     num_generator = (x*2 for x in range(1,3))
    #
    #     self.assertEqual(2, num_list[0])
    #
    #     # A generator has to be iterated through.
    #     with self.assertRaises(___): num = num_generator[0]
    #
    #     self.assertEqual(__, list(num_generator)[0])

        # Both list comprehensions and generators can be iterated though. However, a generator
        # function is only called on the first iteration. The values are generated on the fly
        # instead of stored.
        #
        # Generators are more memory friendly, but less versatile

    def test_generators_are_different_to_list_comprehensions(self):
        num_list = [x*2 for x in range(1,3)]
        num_generator = (x*2 for x in range(1,3))

        self.assertEqual(2, num_list[0])

        # A generator has to be iterated through.
        with self.assertRaises(TypeError): num = num_generator[0]

        self.assertEqual(2, list(num_generator)[0])

        # Both list comprehensions and generators can be iterated though. However, a generator
        # function is only called on the first iteration. The values are generated on the fly
        # instead of stored.
        #
        # Generators are more memory friendly, but less versatile
    #
    # def test_generator_expressions_are_a_one_shot_deal(self):
    #     dynamite = ('Boom!' for n in range(3))
    #
    #     attempt1 = list(dynamite)
    #     attempt2 = list(dynamite)
    #
    #     self.assertEqual(__, attempt1)
    #     self.assertEqual(__, attempt2)

    def test_generator_expressions_are_a_one_shot_deal(self):
        dynamite = ('Boom!' for n in range(3))

        attempt1 = list(dynamite)
        attempt2 = list(dynamite)

        self.assertEqual(['Boom!', 'Boom!','Boom!'], attempt1)
        self.assertEqual([], attempt2)

    # ------------------------------------------------------------------

    # def simple_generator_method(self):
    #     yield 'peanut'
    #     yield 'butter'
    #     yield 'and'
    #     yield 'jelly'
    #
    # def test_generator_method_will_yield_values_during_iteration(self):
    #     result = list()
    #     for item in self.simple_generator_method():
    #         result.append(item)
    #     self.assertEqual(__, result)

    # https://wiki.python.org/moin/Generators

    def simple_generator_method(self):
        yield 'peanut'
        yield 'butter'
        yield 'and'
        yield 'jelly'

    def test_generator_method_will_yield_values_during_iteration(self):
        result = list()
        for item in self.simple_generator_method():
            result.append(item)
        self.assertEqual(['peanut', 'butter', 'and', 'jelly'], result)
    #
    # def test_generators_can_be_manually_iterated_and_closed(self):
    #     result = self.simple_generator_method()
    #     self.assertEqual(__, next(result))
    #     self.assertEqual(__, next(result))
    #     result.close()
    # https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/ch04.html
    # https://anandology.com/python-practice-book/iterators.html
    # https://realpython.com/introduction-to-python-generators/#how-to-use-close
    # As its name implies, .close() allows you to stop a generator. This can be especially
    # handy when controlling an infinite sequence generator.

    def test_generators_can_be_manually_iterated_and_closed(self):
        result = self.simple_generator_method()
        self.assertEqual('peanut', next(result))
        self.assertEqual('butter', next(result))
        result.close()


    # ------------------------------------------------------------------
    #
    # def square_me(self, seq):
    #     for x in seq:
    #         yield x * x
    #
    # def test_generator_method_with_parameter(self):
    #     result = self.square_me(range(2,5))
    #     self.assertEqual(__, list(result))

    # https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    # https://www.geeksforgeeks.org/python-yield-keyword/
    # Yield is a keyword in Python that is used to return from a function without destroying the states
    # of its local variable and when the function is called, the execution starts from the last yield
    # statement. Any function that contains a yield keyword is termed a generator.
    # Hence, yield is what makes a generator. The yield keyword in Python is less known
    # off but has a greater utility which one can think of.
    def square_me(self, seq):
        for x in seq:
            yield x * x

    def test_generator_method_with_parameter(self):
        result = self.square_me(range(2,5))
        self.assertEqual([4,9,16], list(result))
    # ------------------------------------------------------------------

    # def sum_it(self, seq):
    #     value = 0
    #     for num in seq:
    #         # The local state of 'value' will be retained between iterations
    #         value += num
    #         yield value
    #
    # def test_generator_keeps_track_of_local_variables(self):
    #     result = self.sum_it(range(2,5))
    #     self.assertEqual(__, list(result))

    # https://stackoverflow.com/questions/29759219/how-do-python-generator-functions-maintain-local-state
    # https://www.programiz.com/python-programming/generator
    def sum_it(self, seq):
        value = 0
        for num in seq:
            # The local state of 'value' will be retained between iterations
            value += num
            yield value

    def test_generator_keeps_track_of_local_variables(self):
        result = self.sum_it(range(2,5))
        self.assertEqual([2,5,9], list(result))

    # ------------------------------------------------------------------

    # def coroutine(self):
    #     result = yield
    #     yield result
    #
    # def test_generators_can_act_as_coroutines(self):
    #     generator = self.coroutine()
    #
    #     # THINK ABOUT IT:
    #     # Why is this line necessary?
    #     #
    #     # Hint: Read the "Specification: Sending Values into Generators"
    #     #       section of http://www.python.org/dev/peps/pep-0342/
    #     next(generator)
    #
    #     self.assertEqual(__, generator.send(1 + 2))

    # https://docs.python.org/3/library/asyncio-task.html
    # https://www.geeksforgeeks.org/coroutine-in-python/
    # https://www.python.org/dev/peps/pep-0342/#:~:text=Python's%20generator%20functions%20are%20almost,passed%20in%20when%20execution%20resumes.
    # Coroutines are a natural way of expressing many algorithms, such as simulations, games,
    # asynchronous I/O, and other forms of event-driven programming or co-operative multitasking.
    # Python's generator functions are almost coroutines -- but not quite -- in that they allow
    # pausing execution to produce a value, but do not provide for values or exceptions to be passed
    # in when execution resumes.

    def coroutine(self):
        result = yield
        yield result

    def test_generators_can_act_as_coroutines(self):
        generator = self.coroutine()

        # THINK ABOUT IT:
        # Why is this line necessary?
        #
        # Hint: Read the "Specification: Sending Values into Generators"
        #       section of http://www.python.org/dev/peps/pep-0342/
        next(generator)

        self.assertEqual(3, generator.send(1 + 2))

    def test_before_sending_a_value_to_a_generator_next_must_be_called(self):
        generator = self.coroutine()

        try:
            generator.send(1 + 2)
        except TypeError as ex:
            self.assertRegex(ex.args[0], 'generator')

    # ------------------------------------------------------------------

    # def yield_tester(self):
    #     value = yield
    #     if value:
    #         yield value
    #     else:
    #         yield 'no value'
    #
    # def test_generators_can_see_if_they_have_been_called_with_a_value(self):
    #     generator = self.yield_tester()
    #     next(generator)
    #     self.assertEqual('with value', generator.send('with value'))
    #
    #     generator2 = self.yield_tester()
    #     next(generator2)
    #     self.assertEqual(__, next(generator2))
    #
    # def test_send_none_is_equivalent_to_next(self):
    #     generator = self.yield_tester()
    #
    #     next(generator)
    #     # 'next(generator)' is exactly equivalent to 'generator.send(None)'
    #     self.assertEqual(__, generator.send(None))

    # https://realpython.com/introduction-to-python-generators/#how-to-use-close
    # https://stackoverflow.com/questions/19302530/python-generator-send-function-purpose
    # generator.send(None), It's used to send values into a generator that just yielded


    def yield_tester(self):
        value = yield
        if value:
            yield value
        else:
            yield 'no value'

    def test_generators_can_see_if_they_have_been_called_with_a_value(self):
        generator = self.yield_tester()
        next(generator)
        self.assertEqual('with value', generator.send('with value'))

        generator2 = self.yield_tester()
        next(generator2)
        self.assertEqual('no value', next(generator2))

    def test_send_none_is_equivalent_to_next(self):
        generator = self.yield_tester()

        next(generator)
        # 'next(generator)' is exactly equivalent to 'generator.send(None)'
        self.assertEqual('no value', generator.send(None))
