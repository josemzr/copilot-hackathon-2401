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

    def test_palindrome_text_empty(self):
        response = client.get("/api/palindrome?text=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"palindrome": True})

    def test_palindrome_text_true(self):
        response = client.get("/api/palindrome?text=A man a plan a canal Panama")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"palindrome": True})

    def test_palindrome_text_false(self):
        response = client.get("/api/palindrome?text=Hello World")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"palindrome": False})

if __name__ == '__main__':
    unittest.main()