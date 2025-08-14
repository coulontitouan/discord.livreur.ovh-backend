from dotenv import dotenv_values
from flask import Blueprint

config = dotenv_values(".env")
TOKEN = config.get("TOKEN")

HEADERS = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "Website (http://discord.livreur.ovh, v1.0)",
}

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*"
}

PREFIX = "api"
DEFAULT_FILE = "index.html"
STATIC_FOLDER = "static"

LIVREUR_ID = 524926551431708674

API = Blueprint(PREFIX, __name__)