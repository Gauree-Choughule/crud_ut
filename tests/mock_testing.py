import unittest
import json
from unittest.mock import patch
from users.connections.connectors import app
from users.logic.books import books_routes



@patch("users.models.models.Book")
def test_mock_books(mock_user_model, client):
    client = app.test_client()
    mock_user_model().get_books.return_value = [{'author': 'H.G. Wells', 'id': 2, 'title': 'Time Machine'},
                        {'author': 'Kautilya', 'id': 3, 'title': 'The great Arthashastra'},
                         {'author': 'Rabindra Nath Tagore', 'id': 4, 'title': 'Geetanjali'},
                         {'author': 'post_Author', 'id': 5, 'title': 'post_Book'}]

    response = client.get('/books')
    print(response)
    assert response.status_code == 200
    actual_result = json.loads(response.data)
    expected_result = [{'author': 'H.G. Wells', 'id': 2, 'title': 'Time Machine'},
                        {'author': 'Kautilya', 'id': 3, 'title': 'The great Arthashastra'},
                         {'author': 'Rabindra Nath Tagore', 'id': 4, 'title': 'Geetanjali'},
                         {'author': 'post_Author', 'id': 5, 'title': 'post_Book'}]
    assert actual_result == expected_result


# @patch("users.models.models.Book")
# def test_delete_books(mock_user_model, client):
#     mock_user_model().get_books.return_value = [{'author': 'H.G. Wells', 'id': 2, 'title': 'Time Machine'},
#                         {'author': 'Kautilya', 'id': 3, 'title': 'The great Arthashastra'},
#                          {'author': 'Rabindra Nath Tagore', 'id': 4, 'title': 'Geetanjali'},
#                          {'author': 'post_Author', 'id': 5, 'title': 'post_Book'}]
#
#     response = client.delete('/books/<int:book_id>')
#     print(response)
#     assert response.status_code == 200
#     actual_result = json.loads(response.data)
#     expected_result = [{'author': 'H.G. Wells', 'id': 2, 'title': 'Time Machine'},
#                         {'author': 'Kautilya', 'id': 3, 'title': 'The great Arthashastra'},
#                          {'author': 'Rabindra Nath Tagore', 'id': 4, 'title': 'Geetanjali'},
#                          {'author': 'post_Author', 'id': 5, 'title': 'post_Book'}]
#     assert actual_result == expected_result

# class TestBookRoutes(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.register_blueprint(books_routes)
#         self.app = app.test_client()
#
#     @patch('users.logic.books.get_books')
#     def test_get_books(self, query):                   # Create return value for Book.query.all()
#         mock_books = [{'author': 'H.G. Wells', 'id': 2, 'title': 'Time Machine'},
#                         {'author': 'Kautilya', 'id': 3, 'title': 'The great Arthashastra'},
#                          {'author': 'Rabindra Nath Tagore', 'id': 4, 'title': 'Geetanjali'},
#                          {'author': 'post_Author', 'id': 5, 'title': 'post_Book'}]
#         query.all.return_value = mock_books
#
#         response = self.app.get('/books')
#         self.assertEqual(response.status_code, 200)               # successful retrieval
#         data = response.get_json()
#         self.assertEqual(data['books'], mock_books)
#
#     @patch('users.logic.books.get_single_book')
#     def test_get_book(self, query):
#         mock_book = {"id": 2, "title": "Time Machine", "author": "H.G. Wells"}
#         query.get.return_value = mock_book
#
#         response = self.app.get('/books/2')
#         self.assertEqual(response.status_code, 200)
#         data = response.get_json()
#         self.assertEqual(data, mock_book)
#
#     @patch('users.logic.books.create_book')
#     def test_create_book(self, query):
#         mock_book = {"id": 5}
#         query.post.return_value = mock_book
#
#         post_data = {"title": "post_Book", "author": "post_Author"}               # data to post
#
#         response = self.app.post('/books', json=post_data)
#         self.assertEqual(response.status_code, 200)
#
#     @patch('users.logic.books.update_book')
#     def test_update_book(self, query):
#         mock_book = {"id": 1, "title": "Animal", "author": "George"}             # mock book
#         query.get.return_value = mock_book
#
#         update_data = {"title": "Updated Book", "author": "Updated Author"}               # data for update
#
#         response = self.app.put('/books/1', json=update_data)
#         self.assertEqual(response.status_code, 200)                  # Optionally, check if the book was updated in the database
#
#     @patch('users.logic.books.patch_book')
#     def test_patch_book(self, query):
#         mock_book = {"id": 3, "title": "Arthashastra", "author": "Kautilya"}
#         query.get.return_value = mock_book
#
#         patch_data = {"title": "The great Arthashastra"}
#
#         response = self.app.patch('/books/3', json=patch_data)
#         self.assertEqual(response.status_code, 200)
#
#     @patch('users.logic.books.delete_book')
#     def test_delete_book(self, query):
#         mock_book = {"title": "Updated Book", "author": "Updated Author"}
#         query.get.return_value = mock_book
#
#         response = self.app.delete('/books/1')
#         self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
