import unittest
import os
from freezegun import freeze_time
# Import the Manager from the package
from uc3m_consulting import EnterpriseManager

class MyTestCase(unittest.TestCase):
    @freeze_time("2026-04-16")
    def test_tc_sa_01_valid_baseline(self):
        manager = EnterpriseManager()

        base_path = os.path.dirname(__file__)
        test_file = os.path.join(base_path, "json_files", "tc_sa_01.json")

        result = manager.register_document(test_file)

        expected = "a3814e1ef2d474f6249c776b92fcdfc6"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()