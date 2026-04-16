import unittest
import os
from freezegun import freeze_time
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

    def test_tc_sa_04_json_not_json(self):
        """tc_sa_04: This SHOULD fail if the manager has no try/except"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_04.json")

        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(test_file)

    def test_tc_sa_05_open_brace_deleted(self):
        """tc_sa_05: Missing opening brace should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_05.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_06_open_brace_duplicated(self):
        """tc_sa_06: Duplicated opening brace should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_06.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_07_open_brace_modified(self):
        """tc_sa_07: Opening brace replaced by bracket should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_07.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_08_close_brace_deleted(self):
        """tc_sa_08: Missing closing brace should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_08.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_09_close_brace_duplicated(self):
        """tc_sa_09: Duplicated closing brace should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_09.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_10_close_brace_modified(self):
        """tc_sa_10: Closing brace replaced by bracket should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_10.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_11_data_deleted(self):
        """tc_sa_11: Empty JSON object should trigger 'JSON does not have expected structure'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_11.json")

        expected_msg = "JSON does not have expected structure"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_12_data_duplicated(self):
        """tc_sa_12: Duplicated fields should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_12.json")

        expected_msg = "JSON data has no valid values"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_13_field1_deleted(self):
        """tc_sa_13: Missing PROJECT_ID should trigger 'JSON does not have expected structure'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_13.json")

        expected_msg = "JSON does not have expected structure"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_14_field1_duplicated(self):
        """tc_sa_14: Duplicated PROJECT_ID should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_14.json")

        expected_msg = "JSON data has no valid values"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

if __name__ == '__main__':
    unittest.main()