from flask import Blueprint, jsonify, request, current_app
import requests

PREFIX = "api"

api_blueprint = Blueprint(PREFIX, __name__)

TOKEN = "TOKEN"
HEADERS = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "Website (http://discord.livreur.ovh, v1.0)",
}
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*"
}

def get_extension(image):
    return "gif" if image.split("_")[0] else "png"

@api_blueprint.route("", methods=["GET"])
def home():
    routes = [str(p) for p in current_app.url_map.iter_rules() if p.endpoint.startswith(f"{PREFIX}.")]
    return jsonify({"status": "online", "routes" : routes}), 200, CORS_HEADERS

@api_blueprint.route("/user", methods=["GET"])
@api_blueprint.route("/user/<int:user_id>", methods=["GET"])
def user(user_id:int = 524926551431708674):
    response = requests.get(f"https://discord.com/api/v10/users/{user_id}", headers=HEADERS)

    return response.json(), 200, CORS_HEADERS

@api_blueprint.route("/user/@me", methods=["GET"])
def me():
    return user("@me")

@api_blueprint.route("/banner", methods=["GET"])
def banner():
    response = requests.get("https://discord.com/api/v10/users/524926551431708674", headers=HEADERS)
    
    avatar = response.json()["avatar"]

    avatar_url = None

    if avatar:
        extension = get_extension(avatar)
        avatar_url = f"https://cdn.discordapp.com/avatars/524926551431708674/{avatar}.{extension}?size=4096"

    avatar_decoration = response.json()["avatar_decoration_data"]["asset"]

    avatar_decoration_url = None

    if avatar_decoration:
        extension = get_extension(avatar_decoration)
        avatar_decoration_url = f"https://cdn.discordapp.com/avatar-decoration-presets/{avatar_decoration}.{extension}?size=4096"

    banner = response.json()["banner"]
    # banner = "a_b48b408392ecb36e2a378d224d255bee"
    banner_color = response.json()["banner_color"]

    banner_url = None

    if banner:
        extension = get_extension(banner)
        banner_url = f"https://cdn.discordapp.com/banners/524926551431708674/{banner}.{extension}?size=4096"

    return jsonify({"banner_url": banner_url, "banner_color" : banner_color, "avatar_url": avatar_url, "avatar_decoration_url": avatar_decoration_url }), 200,  {
                "Access-Control-Allow-Origin": "*"
            }