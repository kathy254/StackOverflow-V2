import unittest

from app.api.v2.utils.validators import Validations


class TestValidations(unittest.TestCase):
    def setUp(self):
        self.test = Validations()

    def tearDown(self):
        self.test = None

    def test_is_empty(self):
        test = self.test.is_empty(["", "name"])
        self.assertTrue(test)

    def test_not_empty(self):
        test = self.test.is_empty(["my", "name"])
        self.assertFalse(test)

    def test_is_whitespace(self):
        test = self.test.is_whitespace([" ", "name"])
        self.assertTrue(test)

    def test_not_whitespace(self):
        test = self.test.is_whitespace(["your", "name"])
        self.assertFalse(test)

    def test_valid_signup(self):
        payload = {"email_address": "email@gmail.com", "username": "user1", "password": "abcd"}
        test = self.test.is_signup_payload(payload)
        self.assertTrue(test)

    def test_invalid_signup(self):
        payload1 = {"email": "none@gmail.com", "pqr": "ksksksks", "one": "mine"}
        test = self.test.is_signup_payload(payload1)
        self.assertFalse(test)

    def test_valid_login(self):
        payload1 = {"username": "none@gmail.com", "password": "abcdefg"}
        test = self.test.is_login_payload(payload1)
        self.assertTrue(test)

    def test_invalid_login(self):
        payload1 = {"user": "me", "pass": "abcdefg"}
        test = self.test.is_login_payload(payload1)
        self.assertFalse(test)

    def test_valid_email(self):
        test1 = self.test.is_valid_email("myname@gmail.com")
        test2 = self.test.is_valid_email("you@gmail.co.uk")
        test3 = self.test.is_valid_email("me@gmail.travel")
        self.assertTrue(test1)
        self.assertTrue(test2)
        self.assertTrue(test3)

    def test_invalid_email(self):
        test1 = self.test.is_valid_email("myname.com")
        test2 = self.test.is_valid_email("emailaddress")
        self.assertFalse(test1)
        self.assertFalse(test2)

    def test_valid_password(self):
        test1 = self.test.is_valid_password("abcdefghsl")
        test2 = self.test.is_valid_password("18899299")
        self.assertTrue(test1)
        self.assertTrue(test2)

    def test_invalid_password(self):
        test1 = self.test.is_valid_password("abcd")
        test2 = self.test.is_valid_password("abdiislsllslallalslkkd")
        self.assertFalse(test1)
        self.assertFalse(test2)

if __name__ == "__main__":
    unittest.main()
