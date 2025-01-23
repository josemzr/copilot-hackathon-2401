import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_reverse_text_empty(self):
        response = client.get("/api/reverse?text=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"reversed": ""})
        
    def test_disemvowel_text_empty(self):
        response = client.get("/api/disemvowel?text=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"disemvoweled": ""})

if __name__ == '__main__':
    unittest.main()