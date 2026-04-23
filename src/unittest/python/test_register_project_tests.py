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

    @freeze_time("2026-04-16")
    def test_tc_sa_41_hex_32_chars(self):
        """tc_sa_41: Hex terminal: 32 chars (valid boundary)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_41.json")
        result = manager.register_document(test_file)
        self.assertEqual(
            "0533a93ad643a625ca5ca6ac3b2c36d1f158d7351f534dec4b5357684a9ea6a4",
            result
        )
   
    def test_tc_sa_42_hex_33_chars(self):
        """tc_sa_42: Hex terminal: 33 chars (n+1 boundary)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_42.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_43_hex_nonhex_char(self):
        """tc_sa_43: Hex terminal: non-hex char (g) in value"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_43.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_44_hex_symbol_char(self):
        """tc_sa_44: Hex terminal: symbol (@) in PROJECT_ID"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_44.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_45_fn_token_deleted(self):
        """tc_sa_45: <FILENAME_TOKEN> deleted: label quotes missing"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_45.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_46_fn_token_modified(self):
        """tc_sa_46: <FILENAME_TOKEN> modified: wrong label string"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_46.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON does not have expected structure", str(context.exception))

    def test_tc_sa_47_fn_value_deleted(self):
        """tc_sa_47: <FILENAME_VALUE> deleted: only extension remains"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_47.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_48_fn_value_duplicated(self):
        """tc_sa_48: <FILENAME_VALUE> duplicated: name+ext repeated"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_48.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_49_name_deleted(self):
        """tc_sa_49: <NAME> deleted: no name, only extension"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_49.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_50_name_duplicated(self):
        """tc_sa_50: <NAME> duplicated: 16-char name"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_50.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_51_ext_deleted(self):
        """tc_sa_51: <EXTENSION> deleted: no extension in filename"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_51.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_52_ext_duplicated(self):
        """tc_sa_52: <EXTENSION> duplicated: .pdf.pdf"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_52.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_53_ext_invalid(self):
        """tc_sa_53: <EXTENSION> modified: .txt (not allowed)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_53.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_54_alphanum_0_chars(self):
        """tc_sa_54: <ALPHANUMERIC> deleted: empty NAME (0 chars)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_54.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_55_alphanum_1_char(self):
        """tc_sa_55: <ALPHANUMERIC> duplicated: 1-char NAME"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_55.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_56_alphanum_7_chars(self):
        """tc_sa_56: Alphanum terminal: 7 chars (n-1 boundary)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_56.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    @freeze_time("2026-01-01")
    def test_tc_sa_57_alphanum_8_chars(self):
        """tc_sa_57: Alphanum terminal: 8 chars (valid boundary)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_57.json")
        result = manager.register_document(test_file)
        self.assertEqual(
            "a9c50519863c10254c82cf0415bb5f58ebbd86bcc9928c5b1097a100c3ce3082",
            result
        )

    def test_tc_sa_58_alphanum_9_chars(self):
        """tc_sa_58: Alphanum terminal: 9 chars (n+1 boundary)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_58.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_59_alphanum_symbol(self):
        """tc_sa_59: Alphanum terminal: symbol (%) in NAME"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_59.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_60_alphanum_space(self):
        """tc_sa_60: Alphanum terminal: space in NAME"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_60.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    @freeze_time("2026-04-16")
    def test_tc_sa_61_ext_pdf(self):
        """tc_sa_61: Extension terminal: .pdf (valid)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_61.json")
        result = manager.register_document(test_file)
        self.assertEqual(
            "0533a93ad643a625ca5ca6ac3b2c36d1f158d7351f534dec4b5357684a9ea6a4",
            result
        )

    @freeze_time("2026-01-01")
    def test_tc_sa_62_ext_docx(self):
        """tc_sa_62: Extension terminal: .docx (valid)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_62.json")
        result = manager.register_document(test_file)
        self.assertEqual(
            "e324578bb6c0ac4a97b6eee2d79bdcaf16ec8ae372f8078fed7afb993994a1d7",
            result
        )

    @freeze_time("2026-01-01")
    def test_tc_sa_63_ext_xlsx(self):
        """tc_sa_63: Extension terminal: .xlsx (valid)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_63.json")
        result = manager.register_document(test_file)
        self.assertEqual(
            "253408a2f50672b8b88e9cc64bb448733cc6e6c2ad538d5b34f8b8721827be2e",
            result
        )

    def test_tc_sa_64_ext_uppercase(self):
        """tc_sa_64: Extension terminal: .PDF (uppercase, not allowed)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_64.json")
        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(test_file)
        self.assertEqual("JSON data has no valid values", str(context.exception))

    def test_tc_sa_65_ext_csv(self):
        """tc_sa_65: <EXTENSION_TOKEN> modified: .csv (not allowed)"""
        manager = EnterpriseManager()
        test_file = os.path.join(os.path.dirname(__file__), "json_files", "tc_sa_65.json")
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