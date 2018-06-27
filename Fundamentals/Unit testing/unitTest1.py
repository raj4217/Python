import unittest
import unit_testing_1


class testCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(unit_testing_1.add(2, 3), 5)
        self.assertEqual(unit_testing_1.add(-7, 3), -4)
        self.assertEqual(unit_testing_1.add(-2, -13), -15)

    def test_subtract(self):
        self.assertEqual(unit_testing_1.subtract(2, 3), -1)
        self.assertEqual(unit_testing_1.subtract(-7, 3), -10)
        self.assertEqual(unit_testing_1.subtract(-2, -13), 11)

    def test_multiply(self):
        self.assertEqual(unit_testing_1.multiply(2, 3), 6)
        self.assertEqual(unit_testing_1.multiply(-7, 3), -21)
        self.assertEqual(unit_testing_1.multiply(-2, -13), 26)

    def test_divide(self):
        self.assertEqual(unit_testing_1.divide(6, 3), 2)
        self.assertEqual(unit_testing_1.divide(-7, 1), -7)
        self.assertEqual(unit_testing_1.divide(-12, -3), 4)
        self.assertEqual(unit_testing_1.divide(12, 0), exception)


# if __name__ == '__main__':
unittest.main()
