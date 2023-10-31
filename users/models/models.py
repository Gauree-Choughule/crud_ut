from users.connections.connectors import app, db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title})"


with app.app_context():
    db.create_all()
    # db.drop_all()

