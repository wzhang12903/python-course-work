import unittest
from analyzer import calculate_average

class TestAnalyzer(unittest.TestCase):

    def test_average_normal(self):
        class Dummy:
            def __init__(self):
                self.data = {"Score": [80, 90, 100]}
            def __getitem__(self, key):
                return self.data[key]

        df = Dummy()
        self.assertEqual(calculate_average(df), 90)

    def test_average_single(self):
        class Dummy:
            def __init__(self):
                self.data = {"Score": [50]}
            def __getitem__(self, key):
                return self.data[key]

        df = Dummy()
        self.assertEqual(calculate_average(df), 50)

    def test_average_empty(self):
        class Dummy:
            def __init__(self):
                self.data = {"Score": []}
            def __getitem__(self, key):
                return self.data[key]

        df = Dummy()
        self.assertEqual(calculate_average(df), 0)

if __name__ == "__main__":
    unittest.main()
    