import unittest
from python import algorithms

arrays = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [2], [2, 1], [1, 2], [2, 4, 6], [1, 3, 9], [10, 8], [11, 31]]
expected = [7, 1, 2, 2, 2, 6, 9, 10, 31]


class AlgorithmsTests(unittest.TestCase):
    def test_ternary_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            exp = expected[i]
            answer = (algorithms.ternary_search(array, 0, len(array) - 1, exp))
            var = not None

            self.assertTrue(answer is not var)

    def test_Binary_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            exp = expected[i]
            self.assertTrue(algorithms.binary_search(array, exp, 0, len(array) - 1), True)

    def test_linear_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            exp = expected[i]
            self.assertTrue(algorithms.linear_search(array, exp))


if __name__ == "__main__":
    unittest.main()
