import unittest
from users.connections.connectors import app, db


class TestCRUDOperations(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flask"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        with app.app_context():
            db.create_all()
        self.app = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_book(self):
        response = self.app.post("/books", json={"title": "Test Book", "author": "Test Author"})
        print(response)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Book created successfully")

    def test_get_books(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data["books"], list)

    def test_update_book(self):
        response = self.app.post("/books", json={"title": "Test Book", "author": "Test author"})
        data = response.get_json()
        print(data)
        book_id = data['id']

        response = self.app.put(f"/books/{book_id}", json={"title": "Updated Book", "author": "Updated author"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Book updated successfully")

    def test_patch_book(self):
        response = self.app.post("/books", json={"title": "Test Book", "author": "Test author"})
        data = response.get_json()
        book_id = data['id']

        response = self.app.patch(f"/books/{book_id}", json={"author": "New Updated Author"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Book fields updated successfully")

    def test_delete_book(self):
        # First, create a book
        response = self.app.post("/books", json={"title": "Test Book", "author": "Test author"})
        data = response.get_json()
        book_id = data['id']

        response = self.app.delete(f"/books/{book_id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Book deleted successfully")


if __name__ == "__main__":
    unittest.main()
