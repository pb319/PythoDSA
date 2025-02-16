import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        # res = calc.multipy(10,5)
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-3),-4)

    def test_subtract(self):
            # res = calc.multipy(10,5)
            self.assertEqual(calc.substract(10,5),5)
            self.assertEqual(calc.substract(-1,1),-2)
            self.assertEqual(calc.substract(1,1),0)

    def test_multiply(self):
            # res = calc.multipy(10,5)
            self.assertEqual(calc.multipy(10,5),50)
            self.assertEqual(calc.multipy(-1,1),-1)
            self.assertEqual(calc.multipy(-1,-3),3)

    def test_divide(self):
            # res = calc.multipy(10,5)
            self.assertEqual(calc.divide(10,5),2)
            self.assertEqual(calc.divide(-1,1),-1)
            self.assertEqual(calc.divide(-4,-2),2)



if __name__ == '__main__':
    unittest.main()