from flask import Blueprint, request
from myfirstflask.app import db
from myfirstflask.models.marker import Marker
import json

mod_marker = Blueprint('mod_marker', __name__)


@mod_marker.route('/marker/add', methods=['POST'])
def add_marker():
    data = {
        'lat': request.form.get("lat"),
        'lng': request.form.get("lng")
    }
    marker = Marker(request.form.get("lat"), request.form.get("lng"))
    db.session.add(marker)
    db.session.commit()
    data['id'] = marker.id
    return json.dumps(data), 200
    # return render_template('index.html', title='Index')


@mod_marker.route('/marker/all')
def all_markers():
    data = [{'id': marker.id, 'lat': marker.latitude, 'lng': marker.longitude}
            for marker in Marker.query.all()]
    return json.dumps(data), 200
