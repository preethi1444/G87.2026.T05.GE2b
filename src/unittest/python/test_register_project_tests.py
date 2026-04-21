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

    def test_tc_sa_15_separator_deleted(self):
        """tc_sa_15: Missing comma between fields should trigger 'file not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_15.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_16_separator_duplicated(self):
        """tc_sa_16: Duplicated comma between fields should trigger 'file not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        # Ensure tc_sa_16.json exists in your json_files folder with the double comma
        test_file = os.path.join(base_path, "json_files", "tc_sa_16.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_17_separator_modified(self):
        """tc_sa_17: Semicolon instead of comma should trigger 'file not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_17.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_18_field2_deleted(self):
        """tc_sa_18: Missing FILENAME field should trigger 'JSON does not have expected structure'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_18.json")

        expected_msg = "JSON does not have expected structure"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_19_field2_duplicated(self):
        """tc_sa_19: Duplicated FILENAME field should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_19.json")

        expected_msg = "JSON data has no valid values"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_20_label_pid_deleted(self):
        """tc_sa_20: Missing key label for PROJECT_ID should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_20.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_21_label_pid_duplicated(self):
        """tc_sa_21: Duplicated key label (syntax error) should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_21.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_22_label_pid_modified(self):
        """tc_sa_22: Modified key name (PROJ_ID) should trigger 'JSON does not have expected structure'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_22.json")

        expected_msg = "JSON does not have expected structure"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_23_colon_pid_deleted(self):
        """tc_sa_23: Missing colon after PROJECT_ID should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_23.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_24_colon_pid_duplicated(self):
        """tc_sa_24: Duplicated colon after PROJECT_ID should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_24.json")

        expected_msg = "The file is not JSON formatted"

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)

        self.assertEqual(expected_msg, str(context.exception))

    def test_tc_sa_25_colon_pid_modified(self):
        """tc_sa_25: Equals sign instead of colon should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_25.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))

    def test_tc_sa_26_value_pid_deleted(self):
        """tc_sa_26: Empty PROJECT_ID string should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_26.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_27_value_pid_duplicated(self):
        """tc_sa_27: 64-char PROJECT_ID (invalid length) should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_27.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_28_label_fn_deleted(self):
        """tc_sa_28: Missing FILENAME key should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_28.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))

    def test_tc_sa_29_label_fn_duplicated(self):
        """tc_sa_29: Repeated FILENAME key should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_29.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))

    def test_tc_sa_30_label_fn_modified(self):
        """tc_sa_30: Modified key name (FILE_NAME) should trigger 'JSON does not have expected structure'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_30.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON does not have expected structure", str(context.exception))

    def test_tc_sa_31_colon_fn_deleted(self):
        """tc_sa_31: Missing colon after FILENAME should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_31.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))

    def test_tc_sa_32_colon_fn_duplicated(self):
        """tc_sa_32: Double colon after FILENAME should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_32.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))

    def test_tc_sa_33_colon_fn_modified(self):
        """tc_sa_33: Equals sign after FILENAME should trigger 'The file is not JSON formatted'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_33.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))

    def test_tc_sa_34_value_fn_deleted(self):
        """tc_sa_34: Empty FILENAME value should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_34.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_35_value_fn_duplicated(self):
        """tc_sa_35: Duplicated filename value should trigger 'JSON data has no valid values'"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_35.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_36_string_token_deleted(self):
        """tc_sa_36: <STRING_TOKEN> deleted: label quotes missing entirely"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_36.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("The file is not JSON formatted", str(context.exception))
    
    def test_tc_sa_37_string_token_modified(self):
        """tc_sa_37: <STRING_TOKEN> modified: label is wrong string"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_37.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON does not have expected structure", str(context.exception))
    
    def test_tc_sa_38_hex_0_chars(self):
        """tc_sa_38: <HEX> deleted: PROJECT_ID value empty (0 chars)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_38.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))
    
    def test_tc_sa_39_hex_1_char(self):
        """tc_sa_39: <HEX> duplicated: 1 char only in PROJECT_ID"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_39.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))
    
    def test_tc_sa_40_hex_31_chars(self):
        """tc_sa_40: Hex terminal: 31 chars (n-1 boundary)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_40.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))


class MyStructuralTests(unittest.TestCase):
    def setUp(self):
        self.manager = EnterpriseManager()
        self.base_path = os.path.dirname(__file__)
        self.json_folder = os.path.join(self.base_path, "json_files")
        if not os.path.exists(self.json_folder):
            os.makedirs(self.json_folder)

    def create_test_file(self, filename, content):
        path = os.path.join(self.json_folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    # TC-ST-01: Path 1→2(yes)→3→11
    def test_tc_st_01_file_not_found(self):
        invalid_path = "/invalid/path/to/document.json"

        with self.assertRaises(EnterpriseManagementException) as context:
            self.manager.register_document(invalid_path)
        self.assertEqual("Input file not found", str(context.exception))

if __name__ == '__main__':
    unittest.main()