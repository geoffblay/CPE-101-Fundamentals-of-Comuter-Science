import unittest
from landerFuncs import *


class TestCases(unittest.TestCase):
    def test_update_acc1(self):
        self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)

    def test_update_acc2(self):
        self.assertAlmostEqual(updateAcceleration(1.62, 5), 0)

    def test_update_alt1(self):
        self.assertAlmostEqual(updateAltitude(1, -2, 1.62), 0)

    def test_update_alt2(self):
        self.assertAlmostEqual(updateAltitude(1300, -1.62, 9.8), 1303.28)

    def test_update_vel1(self):
        self.assertAlmostEqual(updateVelocity(-3.24, 9.8), 6.56)

    def test_update_vel2(self):
        self.assertAlmostEqual(updateVelocity(-1.62, 19.6), 17.98)

    def test_update_fuel1(self):
        self.assertAlmostEqual(updateFuel(5, 5), 0)

    def test_update_fuel2(self):
        self.assertAlmostEqual(updateFuel(9, 0), 9)



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
