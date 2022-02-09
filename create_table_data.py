from parse import parse_wiki
from models import Population, db


def go_data():
    for el in list(filter(None, parse_wiki()[2:])):
        countries = Population(f'{el[2]}', f'{[el[2], el[3], el[4]]}')

        db.session.add(countries)
        db.session.commit()
