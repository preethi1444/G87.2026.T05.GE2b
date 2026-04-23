import json
import os
import re
import hashlib
import datetime
from .enterprise_project import EnterpriseProject
from .enterprise_management_exception import EnterpriseManagementException
from .project_document import ProjectDocument


class EnterpriseManager:
    def register_document(self, file_path):
        if not os.path.exists(file_path):
            raise EnterpriseManagementException("Input file not found")

        if os.path.getsize(file_path) == 0:
            raise EnterpriseManagementException("JSON data has no valid values")

        try:
            def dict_check(pairs):
                res = {}
                for k, v in pairs:
                    if k in res:
                        # Node 7 & 9 Duplicated: Triggers "no valid values" message
                        raise ValueError("Duplicate Key")
                    res[k] = v
                return res

            #Spoke to professor and implemented try catch block

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    raw = f.read()
            except Exception:
                raise EnterpriseManagementException("The file is not JSON formatted")


            data = json.loads(raw, object_pairs_hook=dict_check)

        except json.JSONDecodeError:
            raise EnterpriseManagementException("The file is not JSON formatted")
            
        except ValueError as e:
            if "Duplicate Key" in str(e):
                raise EnterpriseManagementException("JSON data has no valid values")
            #anything else
            raise EnterpriseManagementException("The file is not JSON formatted")

        except Exception:
            raise EnterpriseManagementException("The file is not JSON formatted")

        if not isinstance(data, dict) or "PROJECT_ID" not in data or "FILENAME" not in data:
            raise EnterpriseManagementException("JSON does not have expected structure")

        project_id = data.get("PROJECT_ID").strip()
        filename = data.get("FILENAME").strip()


        if not isinstance(project_id, str) or not re.fullmatch(r"[0-9a-fA-F]{32}", project_id):
            raise EnterpriseManagementException("JSON data has no valid values")

        if not isinstance(filename, str) or not (re.fullmatch(r"[a-zA-Z0-9]{8}\.(pdf|docx|xlsx)", filename)):
            raise EnterpriseManagementException("JSON data has no valid values")


        doc = ProjectDocument(project_id, filename)
        return doc.document_signature

        # today = datetime.datetime.now().strftime("%Y%m%d")

        # hash_input = f"{project_id}{filename}{today}"

        #dont need to do this because already done from proj doc --> auto amke hash. calling a subtree that is linear. 
        # if len(project_id) == 32:
        #     return hashlib.sha256(hash_input.encode("utf-8")).hexdigest()
        # else:
        #     return hashlib.md5(hash_input.encode("utf-8")).hexdigest()


        # project = EnterpriseProject(
        #     company_cif=data["PROJECT_ID"],
        #     project_acronym=data["FILENAME"],
        #     project_description="Baseline",
        #     department="IT",
        #     starting_date="2026-04-16",
        #     project_budget=1000
        # )

        # return project.project_id
