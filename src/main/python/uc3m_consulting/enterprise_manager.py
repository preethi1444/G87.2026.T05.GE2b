import json
from .enterprise_project import EnterpriseProject
from .enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:
    def register_document(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            raise EnterpriseManagementException("JSON data has no valid values")

        data = json.loads(content)
        project = EnterpriseProject(
            company_cif=data["PROJECT_ID"],
            project_acronym=data["FILENAME"],
            project_description="Baseline",
            department="IT",
            starting_date="2026-04-16",
            project_budget=1000
        )

        return project.project_id