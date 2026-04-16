"""class for testing the regsiter_order method"""
from freezegun import freeze_time
import json
import unittest
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException, ProjectDocument

class MyManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = EnterpriseManager()

    @freeze_time("2026-04-16")  # Freezing time as per your Excel
    def test_tc_sa_01_valid_baseline(self):
        """
        ID_TEST: tc_sa_01_valid_baseline
        Description: Valid JSON - baseline (.pdf)
        """
        path = "tc_sa_01.json"
        expected_hash = "c29b7d03db0e597a9a178318e0121697c8a2523c874190c1d5cfb352e0dcbd55"

        data = {
            "PROJECT_ID": "0123456789abcdef0123456789abcdef",
            "FILENAME": "ABcd1234.pdf"
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

        result = self.manager.register_document(path)
        self.assertEqual(result, expected_hash)

    @freeze_time("2026-04-16")
    def test_tc_sa_02_json_empty(self):
        """
        ID_TEST: tc_sa_02_json_empty
        Description: Entire JSON content deleted (empty file)
        """
        path = "tc_sa_02.json"
        with open(path, "w", encoding="utf-8") as f:
            f.write("")

        with self.assertRaises(EnterpriseManagementException) as context:
            self.manager.register_document(path)

        self.assertEqual(str(context.exception), "file not JSON formatted")

    def test_tc_sa_03_json_duplicated(self):
            """
            ID_TEST: tc_sa_03_json_duplicated
            Description: JSON object duplicated at root
            """
            path = "tc_sa_03.json"
            # Two JSON objects in one file is invalid
            content = """{
    "PROJECT_ID": "0123456789abcdef0123456789abcdef",
    "FILENAME": "ABcd1234.pdf"
    }
    {
    "PROJECT_ID": "0123456789abcdef0123456789abcdef",
    "FILENAME": "ABcd1234.pdf"
    }"""
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            # We expect the lab-mandated exception and message
            with self.assertRaises(EnterpriseManagementException) as context:
                self.manager.register_document(path)

            # Checking the message to satisfy the 100% goal
            self.assertEqual(str(context.exception), "file not JSON formatted")

    def test_tc_sa_04_json_not_json(self):
        """
        ID_TEST: tc_sa_04_json_not_json
        Description: File content is plain text, not JSON
        """
        path = "tc_sa_04.json"
        content = "this is not json"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        with self.assertRaises(EnterpriseManagementException) as context:
            self.manager.register_document(path)

        self.assertEqual(str(context.exception), "file not JSON formatted")

    def test_tc_sa_05_open_brace_deleted(self):
            """
            ID_TEST: tc_sa_05_open_brace_deleted
            Description: <open_object> deleted: opening { missing
            """
            path = "tc_sa_05.json"
            content = """ "PROJECT_ID": "0123456789abcdef0123456789abcdef",
    "FILENAME": "ABcd1234.pdf"
    }"""
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            with self.assertRaises(EnterpriseManagementException) as context:
                self.manager.register_document(path)

            self.assertEqual(str(context.exception), "file not JSON formatted")

    def test_tc_sa_06_open_brace_duplicated(self):
        """
        ID_TEST: tc_sa_06_open_brace_duplicated
        Description: <open_object> duplicated: {{ at start
        """
        path = "tc_sa_06.json"
        content = """{{
    "PROJECT_ID": "0123456789abcdef0123456789abcdef",
    "FILENAME": "ABcd1234.pdf"
    }"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        with self.assertRaises(EnterpriseManagementException) as context:
            self.manager.register_document(path)

        self.assertEqual(str(context.exception), "file not JSON formatted")

    def test_tc_sa_07_open_brace_modified(self):
            """
            ID_TEST: tc_sa_07_open_brace_modified
            Description: <open_object> modified: [ instead of {
            """
            path = "tc_sa_07.json"
            content = """[
    "PROJECT_ID": "0123456789abcdef0123456789abcdef",
    "FILENAME": "ABcd1234.pdf"
    }"""
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            with self.assertRaises(EnterpriseManagementException) as context:
                self.manager.register_document(path)

            self.assertEqual(str(context.exception), "file not JSON formatted")

    def test_tc_sa_08_close_brace_deleted(self):
        """
        ID_TEST: tc_sa_08_close_brace_deleted
        Description: <end_object> deleted: closing } missing
        """
        path = "tc_sa_08.json"
        content = """{
    "PROJECT_ID": "0123456789abcdef0123456789abcdef",
    "FILENAME": "ABcd1234.pdf" """
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        with self.assertRaises(EnterpriseManagementException) as context:
            self.manager.register_document(path)

        self.assertEqual(str(context.exception), "file not JSON formatted")

if __name__ == '__main__':
    unittest.main()
