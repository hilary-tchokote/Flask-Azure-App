
# App Flask principal
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from flask import Flask, jsonify, render_template
from flask_caching import Cache
import requests
import yaml
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import AZURE_STORAGE_URL, AZURE_SAS_TOKEN

app = Flask(__name__, template_folder="../templates")
cache = Cache(config={'CACHE_TYPE': 'simple'})

def get_blob_content(blob_name,  file_type):
    """Récupère un fichier JSON/YAML depuis Azure Blob Storage via l’API REST."""
    url = f"{AZURE_STORAGE_URL}{blob_name}?{AZURE_SAS_TOKEN}"  # Générer l’URL complète avec le token
    response = requests.get(url)

    if response.status_code == 200:
        if file_type == "json":
            return response.json()  # Convertir en JSON
        elif file_type == "yaml":
            return yaml.safe_load(response.text)  # Convertir en YAML
    return None  # Retourne None si l’appel échoue


@app.route("/")
def welcome():
    """Page d'accueil"""
    return render_template("welcome.html")


@app.route("/events")
#@cache.cached(timeout=60)       # Mise en cache de 60 secondes
def events():
    """Endpoint API pour récupérer les événements"""
    data = get_blob_content("events.json", file_type ="yaml")  # Récupérer le fichier JSON des événements
    # if data:
    #     return jsonify(data)
    # return jsonify({"error": "Impossible de récupérer les événements"}), 500
    events = data if data else []
    return render_template("events.html", events=events)

@app.route("/news")
#@cache.cached(timeout=60)       # Mise en cache de 60 secondes
def news():
    """Endpoint API pour récupérer les actualités"""
    data = get_blob_content("news.yaml", file_type="yaml")  # Récupérer le fichier YAML
    # if data:
    #     return jsonify(data)
    # return jsonify({"error": "Impossible de récupérer les actualités"}), 500
    news_list = data if data else []
    return render_template("news.html", news_list=news_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)




