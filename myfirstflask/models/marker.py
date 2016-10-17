# from geoalchemy2 import Geography
from myfirstflask.app import db
from myfirstflask.constants import SRID


class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # coordenadas = db.Column(Geography(geometry_type='POINT', srid=SRID), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, latitude=None, longitude=None):
        # self.coordenadas = coordenadas
        self.latitude = latitude
        self.longitude = longitude
