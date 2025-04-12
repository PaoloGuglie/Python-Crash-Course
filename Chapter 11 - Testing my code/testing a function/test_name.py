# The module "unittest" from the Python standard library provides tools for
# testing my code.
# A "unit test" verifies that one specific aspect of a function's
# behavior is correct.
# A "test case" is a collection of unit tests that together
# prove that a function behaves as it's supposed to.
# A test case with "full coverage" includes a full range of unit tests covering
# all the possible ways I can use a function.

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """

    # Any method that starts with "test_" will be run automatically when I
    # run this file

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        # "assert" methods verify that a result I received matches the result
        # I expected to receive.
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
