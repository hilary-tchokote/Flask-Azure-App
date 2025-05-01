from unittest.mock import patch
import unittest
from src.app import get_blob_content
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import AZURE_STORAGE_URL, AZURE_SAS_TOKEN
import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning, module='werkzeug')


class TestGetData(unittest.TestCase):
    warnings.filterwarnings("ignore", category=DeprecationWarning, module='werkzeug')


    @patch('src.app.requests.get')
    def test_get_data_azure(self, mock_get):
        # Simulation de la réponse de l'API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"statistique": 42}

        resultat = get_blob_content("events.json", "json")
        self.assertEqual(resultat, {"statistique": 42})

        #Vérifier que requests.get a été appelé avec l'URL correcte
        mock_get.assert_called_once_with(f"{AZURE_STORAGE_URL}events.json?{AZURE_SAS_TOKEN}")
