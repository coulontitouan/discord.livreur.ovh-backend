import http.client
from flask import current_app, jsonify
from constants import API, CORS_HEADERS, PREFIX

@API.route("", methods=["GET"])
def home():
    routes = [str(p) for p in current_app.url_map.iter_rules() if p.endpoint.startswith(f"{PREFIX}.")]
    return jsonify(routes), http.client.OK, CORS_HEADERS