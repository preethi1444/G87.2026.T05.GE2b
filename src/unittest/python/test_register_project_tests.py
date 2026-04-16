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

if __name__ == '__main__':
    unittest.main()
