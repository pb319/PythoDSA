import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        res = calc.multipy(10,5)
        self.assertEqual(res,51)