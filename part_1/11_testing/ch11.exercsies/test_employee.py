import unittest
from employee import Employee 

class EmployeeSurvey(unittest.TestCase):
    def setUp(self):
        """Create an employee and test for his salary raise"""
        self.emp_1 = Employee('john', 'doe', 0)
        self.salaries = [0, 5000, 1000]

    def test_give_default_raise(self):
        """
        Tests that a salary raise is given properly
        """
        self.emp_1.give_raise()
        self.assertIn(self.salaries[1], self.emp_1.salary)

    def test_five_custom_raise(self):
        """
        Tests that a custom salary raise is given properly
        """
        self.emp_1.give_raise(1000)
        self.assertIn(self.salaries[2], self.emp_1.salary)


if __name__ == '__main__':
    unittest.main()