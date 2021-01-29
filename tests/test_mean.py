from unittest import TestCase
import unittest
from template import mean
import numpy as np


class TestPartialCorrelation(TestCase):
    def test_mean(self):
        samples = np.array([1, 2, 3])
        m = np.mean(samples)
        self.assertEqual(m, 2)


if __name__ == '__main__':
    unittest.main()
