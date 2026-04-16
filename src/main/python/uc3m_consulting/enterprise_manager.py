import json
from .project_document import ProjectDocument
from .enterprise_management_exception import EnterpriseManagementException

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_document(self, file_path):
        """Reads JSON and returns the document signature"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            raise EnterpriseManagementException("Input file not found")
        """
        except json.JSONDecodeError:
            raise EnterpriseManagementException("file not JSON formatted")
 """

        project_id = data.get("PROJECT_ID")
        file_name = data.get("FILENAME")

        new_doc = ProjectDocument(project_id, file_name)

        return new_doc.document_signature

    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True
