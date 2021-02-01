# test for function
# 'doctest' module provides a tool for scanning
# a module and validating tests emnedded in a
# program's docstrings

def average(values):
    """Computes the arithmetic mean of a list of number.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()  # automatically validate the embedded tests

# the 'unittest' module is not as efforless as the 'doctest' module,
# nut it allows a more comprehensive set of tests to be maintained 
# in a separate file

import unittest

class TestStatisticalFunctions(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests