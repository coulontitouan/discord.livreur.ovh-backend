from flask import Flask, send_from_directory
import os

import os
import importlib.util
import sys
from constants import API, DEFAULT_FILE, PREFIX, STATIC_FOLDER

app = Flask(__name__, static_folder=STATIC_FOLDER)

app.url_map.strict_slashes = False

routes_dir = os.path.join(os.path.dirname(__file__), 'routes')
for root, dirs, files in os.walk(routes_dir):
    for file in files:
        if file.endswith('.py') and not file.startswith('_'):
            rel_dir = os.path.relpath(root, os.path.dirname(__file__))
            module_name = os.path.splitext(file)[0]
            if rel_dir == 'routes':
                import_path = f'routes.{module_name}'
            else:
                sub_path = rel_dir.replace(os.sep, '.')
                import_path = f'{sub_path}.{module_name}'
            if import_path not in sys.modules:
                importlib.import_module(import_path)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_front(path:str):
    path = DEFAULT_FILE if path == "" else path
    return send_from_directory(app.static_folder, path if os.path.exists(os.path.join(app.static_folder, path)) else DEFAULT_FILE)

app.register_blueprint(API, url_prefix=f"/{PREFIX}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)