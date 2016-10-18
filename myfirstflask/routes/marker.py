from flask import Blueprint, request
from myfirstflask.app import db
from myfirstflask.models.marker import Marker
import json

mod_marker = Blueprint('mod_marker', __name__)


@mod_marker.route('/marker/add', methods=['POST'])
def add_marker():
    #  data = json.loads(request.data.decode('utf-8'))
    data = {
        'lat': request.form.get("lat"),
        'lng': request.form.get("lng")
    }
    marker = Marker(request.form.get("lat"), request.form.get("lng"))
    try:
        db.session.add(marker)
        db.session.commit()
        data['id'] = marker.id
        data['msg'] = "Adicionado com sucesso"
    except Exception as error:
        print(repr(error))
        data['id'] = -1
        data['msg'] = "Não foi possível adicionar o marcador"
    return json.dumps(data), 200


@mod_marker.route('/marker/all')
def all_markers():
    data = [{'id': marker.id, 'lat': marker.latitude, 'lng': marker.longitude}
            for marker in Marker.query.all()]
    return json.dumps(data), 200
