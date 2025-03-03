from flask import Flask, send_from_directory
import os
from routes import api_blueprint  # Import des routes API

app = Flask(__name__, static_folder="static")
app.url_map.strict_slashes = False
default_file = "index.html"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_front(path:str):
    path = default_file if path == "" else path
    return send_from_directory(app.static_folder, path if os.path.exists(os.path.join(app.static_folder, path)) else default_file)

app.register_blueprint(api_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)