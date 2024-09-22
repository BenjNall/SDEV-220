import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()


# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
# OK means that the test passed. If the test failed, you would see FAIL instead.
# the test passed because the sum function in my_sum correctly returns 6 when passed a list of integers [1, 2, 3].