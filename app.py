from users.logic.books import books_routes
from users.connections.connectors import app


app.register_blueprint(books_routes)


if __name__ == "__main__":
    app.run(debug=True)
