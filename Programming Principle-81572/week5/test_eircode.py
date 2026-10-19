import unittest
from eircode_validator import has_eircode_shape

class TestEircode(unittest.TestCase):
    def test_valid_eircode_shape(self):
        self.assertTrue(has_eircode_shape("A65 F4E2"))

    def test_dublin_eircode_shape(self):
        self.assertTrue(has_eircode_shape("D02 X285"))

    def test_missing_space(self):
        self.assertFalse(has_eircode_shape("A65F4E2"))

    def test_too_short(self):
        self.assertFalse(has_eircode_shape("A65 F4"))

    def test_too_long(self):
        self.assertFalse(has_eircode_shape("A65 F4E23"))

    def test_non_string_value(self):
        self.assertFalse(has_eircode_shape(None))

    def test_empty_string(self):
        self.assertFalse(has_eircode_shape(""))

if __name__ == "__main__":
        unittest.main() 