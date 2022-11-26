import unittest
import main


class TestRabinKarp(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.search("vevvddf", "hevevhjbevvevvddfvbvne"), [10])

    def test_2(self):
        self.assertEqual(main.search("vev", "vevdffdffdfdfdfdfdfve"), [0])


if __name__ == '__main__':
    unittest.main()