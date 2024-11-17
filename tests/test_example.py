import unittest
from app import create_app

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home_route(self):
        """Test if the server is running."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # Modify based on actual routes

if __name__ == "__main__":
    unittest.main()
