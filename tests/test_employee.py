import unittest
from employee import Employee
from unittest.mock import patch

class testEmployeeClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global employee_obj
        employee_obj = Employee("Paulo", "Gonda", 1000)

    @classmethod
    def tearDownClass(cls):
        print("Teardown")

    def test_email(self):
        self.assertEqual(employee_obj.email, "Paulo.Gonda@email.com")

    def test_fullname(self):
        self.assertEqual(employee_obj.fullname, "Paulo Gonda")

    def test_apply_raise(self):
        employee_obj.apply_raise()

        self.assertEqual(employee_obj.pay, 1050)

    @patch("employee.requests")
    def test_monthly_schedule_ok(self, mock_requests):
        mock_requests.get.return_value.ok = True
        mock_requests.get.return_value.text = "Hello"
        func = employee_obj.monthly_schedule("January")

        self.assertEqual(func, "Hello")

    @patch("employee.requests")
    def test_monthly_schedule_else(self, mock_requests):
        mock_requests.get.return_value.ok = False
        func = employee_obj.monthly_schedule("January")

        self.assertEqual(func, "Bad Response!")