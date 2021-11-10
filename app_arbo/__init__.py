from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '123456'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app_arbo.admin import rotas
from app_arbo.trees import rotas



if __name__ == "__main__":
    app.run(threaded=True, port=5000)