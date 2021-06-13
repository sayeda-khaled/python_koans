#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):
    # def test_creating_a_tuple(self):
    #     count_of_three =  (1, 2, 5)
    #     self.assertEqual(__, count_of_three[2])

    # https://www.w3schools.com/python/python_tuples.asp
    # A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.


    def test_creating_a_tuple(self):
        count_of_three =  (1, 2, 5)
        self.assertEqual(5, count_of_three[2])


    # def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):
    #
    #     count_of_three = (1, 2, 5)
    #     try:
    #         count_of_three[2] = "three"
    #     except TypeError as ex:
    #         msg = ex.args[0]
    #
    #     # Note, assertRegex() uses regular expression pattern matching,
    #     # so you don't have to copy the whole message.
    #
    #     self.assertRegex(msg, __)

    # https://www.w3schools.com/python/python_tuples.asp
    # A tuple is a collection which is ordered and unchangeable.
    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):
        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        self.assertRegex(msg,"'tuple' object does not support item assignment")

    # def test_tuples_are_immutable_so_appending_is_not_possible(self):
    #     count_of_three =  (1, 2, 5)
    #     with self.assertRaises(___): count_of_three.append("boom")
    # https://www.datacamp.com/community/tutorials/python-tuples-tutorial
    # This throws an error because you cannot delete from or append to a tuple but you can with a list

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three =  (1, 2, 5)
        with self.assertRaises(AttributeError): count_of_three.append("boom")

        # Tuples are less flexible than lists, but faster.

    # def test_tuples_can_only_be_changed_through_replacement(self):
    #     count_of_three = (1, 2, 5)
    #
    #     list_count = list(count_of_three)
    #     list_count.append("boom")
    #     count_of_three = tuple(list_count)
    #
    #     self.assertEqual(__, count_of_three)

    # https://www.datacamp.com/community/tutorials/python-tuples-tutorial
    # https://www.w3schools.com/python/gloss_python_change_tuple_item.asp
    # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
    # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual((1, 2, 5, 'boom'), count_of_three)

    # def test_tuples_of_one_look_peculiar(self):
    #     self.assertEqual(__, (1).__class__)
    #     self.assertEqual(__, (1,).__class__)
    #     self.assertEqual(__, ("I'm a tuple",).__class__)
    #     self.assertEqual(__, ("Not a tuple").__class__)
    # https://realpython.com/python-lists-tuples/
    # To tell Python that you really want to define a singleton tuple, include a trailing
    # comma (,) just before the closing parenthesis

    def test_tuples_of_one_look_peculiar(self):
        self.assertEqual(int, (1).__class__)
        self.assertEqual(tuple, (1,).__class__)
        self.assertEqual(tuple, ("I'm a tuple",).__class__)
        self.assertEqual(str, ("Not a tuple").__class__)

    # def test_tuple_constructor_can_be_surprising(self):
    #     self.assertEqual(__, tuple("Surprise!"))
    # https://stackoverflow.com/questions/61704534/purpose-of-tuple-constructor-in-python
    # With the tuple function, the single argument must be iterable

    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!'), tuple("Surprise!"))

    # def test_creating_empty_tuples(self):
    #     self.assertEqual(__ , ())
    #     self.assertEqual(__ , tuple()) #Sometimes less confusing
    # https://medium.com/@GalarnykMichael/python-basics-9-tuples-tuple-manipulation-and-the-fibonacci-sequence-2d0da4e2d326
    # There are two ways to initialize an empty tuple. You can initialize an empty tuple by having () with no values in them.
    # You can also initialize an empty tuple by using the tuple function.

    def test_creating_empty_tuples(self):
        self.assertEqual(() , ())
        self.assertEqual((), tuple()) #Sometimes less confusing

    # def test_tuples_can_be_embedded(self):
    #     lat = (37, 14, 6, 'N')
    #     lon = (115, 48, 40, 'W')
    #     place = ('Area 51', lat, lon)
    #     self.assertEqual(__, place)
    # https://www.learnbyexample.org/python-tuple/
    # You can embed tuples
    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(('Area 51', (37, 14, 6, 'N'), (115, 48, 40, 'W')), place)

    # def test_tuples_are_good_for_representing_records(self):
    #     locations = [
    #         ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
    #         ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
    #     ]
    #
    #     locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )
    #
    #     self.assertEqual(__, locations[2][0])
    #     self.assertEqual(__, locations[0][1][2])
    # https://docs.python.org/3.3/library/stdtypes.html?highlight=tuple

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual("Cthulu", locations[2][0])
        self.assertEqual(15.56, locations[0][1][2])
