from create_table_data import go_data
from models import db

db.create_all()
go_data()
