import unittest
from chapter_11.Employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.eric = Employee('Eric', 'Jordan', 6000)

    def test_give_default_raise(self):
        self.eric.raise_up()
        self.assertIn(self.eric.annual_salary, 70000)

    def test_give_custom_raise(self):
        self.eric.raise_up(6000)
        self.assertIn(self.eric.annual_salary, 75000)

unittest.main(TestEmployee.eric())