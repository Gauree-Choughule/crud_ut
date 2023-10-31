from flask import Blueprint, request, jsonify, abort
from users.exceptions.exceptions import BookNotFound, BookCreationFailed, BookUpdateFailed, BookDeletionFailed
from users.models.models import Book
from users.connections.connectors import db

books_routes = Blueprint("books", __name__)


@books_routes.route("/", methods=["GET"])
def get_books():
    try:
        books = Book.query.all()
        book_list = [{"id": book.id, "title": book.title, "author": book.author} for book in books]
        return jsonify({"books": book_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@books_routes.route("/books", methods=["POST"])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(title=data["title"], author=data["author"])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book created successfully"})
    except Exception as e:
        # return jsonify({"error": str(e)}), 500
        raise BookCreationFailed("book creation failed")from e


@books_routes.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        data = request.get_json()
        book = Book.query.get(book_id)
        if not book:
            raise BookNotFound("Book not found")
        book.title = data["title"]
        book.author = data["author"]
        db.session.commit()
        return jsonify({"message": "Book updated successfully"})
    except BookNotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # return jsonify({"error": str(e)}), 500
        raise BookUpdateFailed("book update failed")from e


@books_routes.route("/books/<int:book_id>", methods=["PATCH"])
def patch_book(book_id):
    try:
        data = request.get_json()
        book = Book.query.get(book_id)
        if not book:
            raise BookNotFound("Book not found")
        if "title" in data:
            book.title = data["title"]
        if "author" in data:
            book.author = data["author"]
        db.session.commit()
        return jsonify({"message": "Book fields updated successfully"})
    except BookNotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # return jsonify({"error": str(e)}), 500
        raise BookUpdateFailed("book update failed")from e


@books_routes.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        book = Book.query.get(book_id)
        if not book:
            raise BookNotFound("Book not found")
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"})
    except BookNotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        # return jsonify({"error": str(e)}), 500
        raise BookDeletionFailed("book deletion failed")from e

# @books_routes.route("/", methods=["GET"])
# def get_books():
#     try:
#         books = Book.query.all()
#         book_list = [{"id": book.id, "title": book.title,"author":book.author} for book in books]
#         return jsonify({"books": book_list})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# @books_routes.route("/book/<int:book_id>", methods=["GET"])
# def get_book(book_id):
#     try:
#         book = Book.query.get(book_id)
#         if not book:
#             abort(404, description="Book not found")
#         return jsonify({"id": book.id, "title": book.title,"author":book.author})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# @books_routes.route("/books", methods=["POST"])
# def create_book():
#     try:
#         data = request.get_json()
#         new_book = Book(title=data["title"], author=data["author"])
#         db.session.add(new_book)
#         db.session.commit()
#         return jsonify({"message": "Book created successfully"})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# @books_routes.route("/books/<int:book_id>", methods=["PUT"])
# def update_book(book_id):
#     try:
#         data = request.get_json()
#         book = Book.query.get(book_id)
#         if not book:
#             raise BookNotFound("Book not found")
#         book.title = data["title"]
#         book.author = data["author"]
#         db.session.commit()
#         return jsonify({"message": "Book updated successfully"})
#     except BookNotFound as e:
#         return jsonify({"error": str(e)}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# @books_routes.route("/books/<int:book_id>", methods=["PATCH"])
# def patch_book(book_id):
#     try:
#         data = request.get_json()
#         book = Book.query.get(book_id)
#         if not book:
#             raise BookNotFound("Book not found")
#         if "title" in data:
#             book.title = data["title"]
#         if "author" in data:
#             book.author = data["author"]
#         db.session.commit()
#         return jsonify({"message": "Book fields updated successfully"})
#     except BookNotFound as e:
#         return jsonify({"error": str(e)}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# @books_routes.route("/books/<int:book_id>", methods=["DELETE"])
# def delete_book(book_id):
#     try:
#         book = Book.query.get(book_id)
#         if not book:
#             raise BookNotFound("Book not found")
#         db.session.delete(book)
#         db.session.commit()
#         return jsonify({"message": "Book deleted successfully"})
#     except BookNotFound as e:
#         return jsonify({"error": str(e)}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
