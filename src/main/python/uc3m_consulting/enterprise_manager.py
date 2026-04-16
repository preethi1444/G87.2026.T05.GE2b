import json
import os
from .enterprise_project import EnterpriseProject
from .enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:
    def register_document(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            if os.path.getsize(file_path) == 0:
                raise EnterpriseManagementException("JSON data has no valid values")

            raise EnterpriseManagementException("The file is not JSON formatted")

        project = EnterpriseProject(
            company_cif=data["PROJECT_ID"],
            project_acronym=data["FILENAME"],
            project_description="Baseline",
            department="IT",
            starting_date="2026-04-16",
            project_budget=1000
        )
        return project.project_id