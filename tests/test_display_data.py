import unittest
from src.app import app  # Utilisez un import absolu
import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning, module='werkzeug')


class TestDisplayData(unittest.TestCase):
    warnings.filterwarnings("ignore", category=DeprecationWarning, module='werkzeug')


    def setUp(self):
        self.client = app.test_client()

    def test_static_display(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenue sur Mon Site', response.data)

if __name__ == "__main__":
    unittest.main()
