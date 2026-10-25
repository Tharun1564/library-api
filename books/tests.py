from django.test import TestCase
from rest_framework.test import APIClient
from .validators import is_valid_isbn


class ISBNValidatorTests(TestCase):
    def test_valid_isbn13(self):
        self.assertTrue(is_valid_isbn("9780306406157"))

    def test_valid_isbn10(self):
        self.assertTrue(is_valid_isbn("0306406152"))

    def test_invalid_checksum(self):
        self.assertFalse(is_valid_isbn("9780306406158"))


class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'isbn': '978-0-306-40615-7',
        }

    def test_create_book(self):
        response = self.client.post('/api/books/', self.payload, format='json')
        self.assertEqual(response.status_code, 201, response.data)

    def test_duplicate_isbn_rejected(self):
        self.client.post('/api/books/', self.payload, format='json')
        response = self.client.post('/api/books/', self.payload, format='json')
        self.assertEqual(response.status_code, 400)

    def test_missing_title_rejected(self):
        response = self.client.post('/api/books/', {
            'author': 'A', 'isbn': '9780306406157'
        }, format='json')
        self.assertEqual(response.status_code, 400)
