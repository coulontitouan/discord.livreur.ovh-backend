from flask import jsonify
import requests
from constants import HEADERS, LIVREUR_ID
from constants import API

def get_extension(image):
    return "gif" if image.split("_")[0] else "png"

@API.route("/banner", methods=["GET"])
def banner():
    response = requests.get(f"https://discord.com/api/v10/users/{LIVREUR_ID}", headers=HEADERS)
    print(HEADERS)
    avatar = response.json()["avatar"]

    avatar_url = None

    if avatar:
        extension = get_extension(avatar)
        avatar_url = f"https://cdn.discordapp.com/avatars/{LIVREUR_ID}/{avatar}.{extension}?size=4096"

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
        banner_url = f"https://cdn.discordapp.com/banners/{LIVREUR_ID}/{banner}.{extension}?size=4096"

    return jsonify({"banner_url": banner_url, "banner_color" : banner_color, "avatar_url": avatar_url, "avatar_decoration_url": avatar_decoration_url }), 200,  {
                "Access-Control-Allow-Origin": "*"
            }