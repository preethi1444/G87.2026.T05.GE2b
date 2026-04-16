import unittest
import os
from freezegun import freeze_time
# Import the Manager from the package
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class MyTestCase(unittest.TestCase):
    @freeze_time("2026-04-16")
    def test_tc_sa_01_valid_baseline(self):
        manager = EnterpriseManager()

        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_01.json")

        result = manager.register_document(test_file)

        expected = "a3814e1ef2d474f6249c776b92fcdfc6"
        self.assertEqual(result, expected)

    def test_tc_sa_02_json_empty(self):
        """Test for empty JSON file"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_02.json")

        expected_msg = "JSON data has no valid values"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_03_json_duplicated(self):
        """Test for duplicated JSON objects (malformed)"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_03.json")

        # This must match the string raised in your manager exactly
        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

if __name__ == '__main__':
    unittest.main()