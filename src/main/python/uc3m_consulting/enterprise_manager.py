import json
import os
from .enterprise_project import EnterpriseProject
from .enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:
    def register_document(self, file_path):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            raise EnterpriseManagementException("JSON data has no valid values")

        try:
            def dict_check(pairs):
                res = {}
                for k, v in pairs:
                    if k in res: raise ValueError("Duplicate")
                    res[k] = v
                return res

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f, object_pairs_hook=dict_check)

                if f.read().strip():
                    raise json.JSONDecodeError("Extra data", "", 0)

        except json.JSONDecodeError:
            raise EnterpriseManagementException("The file is not JSON formatted")

        except ValueError:
            raise EnterpriseManagementException("JSON data has no valid values")

        except Exception:
            raise EnterpriseManagementException("The file is not JSON formatted")

        if not isinstance(data, dict) or "PROJECT_ID" not in data or "FILENAME" not in data:
            raise EnterpriseManagementException("JSON does not have expected structure")

        project = EnterpriseProject(
            company_cif=data["PROJECT_ID"],
            project_acronym=data["FILENAME"],
            project_description="Baseline",
            department="IT",
            starting_date="2026-04-16",
            project_budget=1000
        )
        return project.project_id