"""class for testing the regsiter_order method"""
from freezegun import freeze_time
import json
import unittest
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException, ProjectDocument, EnterpriseProject

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    def setUp(self):
        self.manager = EnterpriseManager()
    def test_coverage_enterprise_project(self):
        project = EnterpriseProject(
            company_cif="B12345678",
            project_acronym="TDD-LAB",
            project_description="Test Coverage Project",
            department="IT",
            starting_date="2026-04-16",
            project_budget=1000.50
        )

        _ = project.company_cif
        _ = project.project_description
        _ = project.project_acronym
        _ = project.project_budget
        _ = project.department
        _ = project.starting_date
        _ = project.time_stamp
        _ = project.project_id

        _ = project.to_json()
        _ = str(project)

        project.company_cif = "A87654321"
        project.project_description = "Updated description"
        project.project_acronym = "NEW-ACR"
        project.project_budget = 5000.0
        project.department = "HR"
        project.starting_date = "2026-05-20"

        self.assertEqual(project.company_cif, "A87654321")

    @freeze_time("2026-04-16")
    def test_tc_sa_01_valid_baseline(self):
        """Valid JSON - baseline (.pdf)"""
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

        # Coverage Fix: Access properties directly
        doc = ProjectDocument("0123456789abcdef0123456789abcdef", "ABcd1234.pdf")
        self.assertEqual(doc.project_id, "0123456789abcdef0123456789abcdef")
        self.assertEqual(doc.file_name, "ABcd1234.pdf")
        self.assertEqual(doc.document_signature, expected_hash)

if __name__ == '__main__':
    unittest.main()
