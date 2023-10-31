# import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# username = os.environ['USERNAME']
# password = os.environ['PASSWORD']
# host = os.environ['HOST']
# db_name = os.environ['DB_NAME']

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{username}:{password}@{host}/{db_name}".format(username, password, host, db_name)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

