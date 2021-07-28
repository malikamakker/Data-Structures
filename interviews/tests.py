import unittest
from test_file import fruits
from unittest.mock import Mock, patch

class TestFruits(unittest.TestCase):
    def setUp(self):
        self.fruit =  fruits("mango", "summer")

    def testGoodMonths(self):
        mock = Mock(return_value=True)
        with patch('test_file.check_this', mock):
            self.assertEqual(self.fruit.good_months(), "March-June")

        # mock = Mock(return_value=False)
        def mock(season):
            return False

        with patch('test_file.check_this', mock):
            self.assertFalse(self.fruit.good_months())
