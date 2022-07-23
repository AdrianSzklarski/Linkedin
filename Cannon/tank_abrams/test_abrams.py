import unittest
from abrams import tank


class TestTank(unittest.TestCase):

    def test_stress(self):
        self.assertEqual(tank(57, 120, 200), (-200, 316.5, 0, 116.5), "The correct data was provided")


    def test_stress_incorrect_data_1(self):
        self.assertRaises(TypeError, tank, '57', 120, 200, "You have given the wrong value: a")
        self.assertRaises(TypeError, tank, 57, '120', 200, "You have given the wrong value: b")
        self.assertRaises(TypeError, tank, 57, 120, '200', "You have given the wrong value: p")
        self.assertRaises(TypeError, tank, '57', '120', 200, "You gave the wrong values: a, b")
        self.assertRaises(TypeError, tank, '57', 120, '200', "You gave the wrong values: a, p")
        self.assertRaises(TypeError, tank, 57, '120', '200', "You gave the wrong values: b, p")
        self.assertRaises(TypeError, tank, '57', '120', '200', "You gave the wrong values: a, b, p")

    # def test_stress_incorrect_data_2(self):
    #     self.assertRaises(ValueError, tank, -57, 120, 200, "You have given the wrong value: a")
    #     self.assertRaises(ValueError, tank, 57, -120, 200, "You have given the wrong value: b")
    #     self.assertRaises(ValueError, tank, 57, 120, -200, "You have given the wrong value: p")
    #     self.assertRaises(ValueError, tank, -57, -120, 200, "You gave the wrong values: a, b")
    #     self.assertRaises(ValueError, tank, -57, 120, -200, "You gave the wrong values: a, p")
    #     self.assertRaises(ValueError, tank, 57, -120, -200, "You gave the wrong values: b, p")
    #     self.assertRaises(ValueError, tank, -57, -120, -200, "You gave the wrong values: a, b, p")
