from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from config import user, password, host, db_name

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}"
db = SQLAlchemy(app)


class Population(db.Model):
    id = Column(Integer, primary_key=True)
    country = Column(String(255))
    data = Column(String)

    def __init__(self, country, data):
        self.country = country
        self.data = data

    def __repr__(self):
        return f'{self.data}'
