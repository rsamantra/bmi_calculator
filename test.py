import unittest
import calculator

class TestBMI(unittest.TestCase):
    def test_bmi_calculaor(self):
        result = calculator.bmi_calculator()
        self.assertEqual(type(result), str)


if __name__ == "__main__":
    unittest.main()