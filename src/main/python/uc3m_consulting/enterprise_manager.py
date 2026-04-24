"""Enterprise manager module"""
import json
import os
import re
from .enterprise_management_exception import EnterpriseManagementException
from .project_document import ProjectDocument


class EnterpriseManager:
    """enterprise manager class"""

    def register_document(self, file_path):
        """register doc and return signature"""
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

        if not isinstance(filename, str) or not re.fullmatch(r"[a-zA-Z0-9]{8}\.(pdf|docx|xlsx)", filename):
            raise EnterpriseManagementException("JSON data has no valid values")


        doc = ProjectDocument(project_id, filename)
        #code for structural tests
        storage_path = getattr(self, "storage_path", "document_store.json")

        try:
            with open(storage_path, "a", encoding="utf-8") as store:
                store.write(doc.document_signature + "\n")
        except Exception:
            raise EnterpriseManagementException("Internal processing error when getting the file_signature.")

        return doc.document_signature
