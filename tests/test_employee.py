import unittest
from unittest.mock import patch

from employee import Employee


class MockResponse:

    def __init__(self, ok, text):
        self.ok = ok
        self.text = text


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Ryan", "Ermita", 9999999)

    def test_email(self):
        self.assertEqual("Ryan.Ermita@email.com", self.employee.email)

    def test_fullname(self):
        self.assertEqual("Ryan Ermita", self.employee.fullname)

    def test_apply_raise(self):
        self.assertEqual(9999999, self.employee.pay)
        self.employee.apply_raise()
        self.assertEqual(int(10499998.95), self.employee.pay)

    @patch("employee.requests.get")
    def test_monthly_schedule_success(self,
                                      mock_requests_get):
        mock_requests_get.return_value = MockResponse(True, "Ok!")
        self.assertEqual("Ok!", self.employee.monthly_schedule("x"))

    @patch("employee.requests.get")
    def test_monthly_schedule_fail(self,
                                      mock_requests_get):
        mock_requests_get.return_value = MockResponse(False, "Oh no!")
        self.assertEqual("Bad Response!", self.employee.monthly_schedule("x"))
