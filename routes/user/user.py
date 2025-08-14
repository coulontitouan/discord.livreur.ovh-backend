import http.client
import requests
from constants import API, CORS_HEADERS, HEADERS, LIVREUR_ID

@API.route("/user", methods=["GET"])
@API.route("/user/<int:user_id>", methods=["GET"])
def user(user_id:int = LIVREUR_ID):
    response = requests.get(f"https://discord.com/api/v10/users/{user_id}", headers=HEADERS)

    return response.json(), http.client.OK, CORS_HEADERS

@API.route("/user/@me", methods=["GET"])
def me():
    return user(LIVREUR_ID)
