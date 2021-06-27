#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutExceptions(Koan):

    class MySpecialError(RuntimeError):
        pass

    # def test_exceptions_inherit_from_exception(self):
    #     mro = self.MySpecialError.mro()
    #     self.assertEqual(__, mro[1].__name__)
    #     self.assertEqual(__, mro[2].__name__)
    #     self.assertEqual(__, mro[3].__name__)
    #     self.assertEqual(__, mro[4].__name__)
    #
    # https://www.tutorialspoint.com/Are-Python-Exceptions-runtime-errors
    # Runtime errors:
    # If a program is free of syntax errors, it will be run by the Python interpreter. However, the program may exit if it encounters a runtime error – a problem that went undetected when the program was parsed, but is only revealed when the code is executed.
    # Some examples of Python Runtime errors −
    # division by zero
    # performing an operation on incompatible types
    # using an identifier which has not been defined
    # accessing a list element, dictionary value or object attribute which doesn’t exist
    # trying to access a file which doesn’t exist

    # https://docs.python.org/3/library/exceptions.html

    # https://docs.python.org/3/tutorial/errors.html#tut-userexceptions
    # Even if a statement or expression is syntactically correct, it may cause an error
    # when an attempt is made to execute it. Errors detected during execution are called
    # exceptions and are not unconditionally fatal

    # https://docs.python.org/3/library/exceptions.html#BaseException
    # exception BaseException:
    # The base class for all built-in exceptions. It is not meant to be directly inherited by
    # user-defined classes (for that, use Exception). If str() is called on an instance of this class,
    # the representation of the argument(s) to the instance are returned, or the empty string when there
    # were no arguments.

    def test_exceptions_inherit_from_exception(self):
        mro = self.MySpecialError.mro()
        self.assertEqual('RuntimeError', mro[1].__name__)
        self.assertEqual('Exception', mro[2].__name__)
        self.assertEqual('BaseException', mro[3].__name__)
        self.assertEqual('object', mro[4].__name__)

    # def test_try_clause(self):
    #     result = None
    #     try:
    #         self.fail("Oops")
    #     except Exception as ex:
    #         result = 'exception handled'
    #
    #         ex2 = ex
    #
    #     self.assertEqual(__, result)
    #
    #     self.assertEqual(__, isinstance(ex2, Exception))
    #     self.assertEqual(__, isinstance(ex2, RuntimeError))
    #
    #     self.assertTrue(issubclass(RuntimeError, Exception), \
    #         "RuntimeError is a subclass of Exception")
    #
    #     self.assertEqual(__, ex2.args[0])

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'

            ex2 = ex

        self.assertEqual('exception handled', result)

        self.assertEqual(True, isinstance(ex2, Exception))
        self.assertEqual(False, isinstance(ex2, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, Exception), \
            "RuntimeError is a subclass of Exception")

        self.assertEqual('Oops', ex2.args[0])

    # def test_raising_a_specific_error(self):
    #     result = None
    #     try:
    #         raise self.MySpecialError("My Message")
    #     except self.MySpecialError as ex:
    #         result = 'exception handled'
    #         msg = ex.args[0]
    #
    #     self.assertEqual(__, result)
    #     self.assertEqual(__, msg)

    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]

        self.assertEqual('exception handled', result)
        self.assertEqual('My Message', msg)


    # def test_else_clause(self):
    #     result = None
    #     try:
    #         pass
    #     except RuntimeError:
    #         result = 'it broke'
    #         pass
    #     else:
    #         result = 'no damage done'
    #
    #     self.assertEqual(__, result)

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        self.assertEqual('no damage done', result)


    # def test_finally_clause(self):
    #     result = None
    #     try:
    #         self.fail("Oops")
    #     except:
    #         # no code here
    #         pass
    #     finally:
    #         result = 'always run'
    #
    #     self.assertEqual(__, result)

    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual('always run', result)
