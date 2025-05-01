# 1. Importation des bibliothèques nécessaires
from faker import Faker
import random
import json
import yaml
from datetime import datetime

# 2. Initialisation de Faker avec le paramètre de localisation français (Europe)
fake = Faker('fr_FR')
# (Optionnel) On peut fixer la graine pour obtenir des résultats reproductibles :
# fake.seed_instance(1234)

# 3. Définir une fonction pour générer un événement
def generate_event(event_id):
    event = {
        "id": event_id,
        "titre": fake.sentence(nb_words=6),  # Titre composé de 6 mots
        "date": fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
        "lieu": fake.city(),                # Ville aléatoire
        "description": fake.text(max_nb_chars=200)  # Description limitée à 200 caractères
    }
    return event

# 4. Générer une liste d'événements (ici 10 événements par exemple)
def generate_events(num_events=50):
    return [generate_event(i+1) for i in range(num_events)]

# 5. Définir une fonction pour générer une actualité (news)
def generate_news_item(news_id):
    news = {
        "id": news_id,
        "titre": fake.sentence(nb_words=8),  # Un titre plus long (8 mots)
        "date": fake.date_time_between(start_date="-6m", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
        "contenu": fake.paragraph(nb_sentences=5),  # Paragraphe de 5 phrases
        "auteur": fake.name()  # Nom complet de l'auteur
    }
    return news

# 6. Générer une liste d’actualités (ici 5 actualités par exemple)
def generate_news(num_news=40):
    return [generate_news_item(i+1) for i in range(num_news)]

# 7. Génération des données
events = generate_events(50)
news = generate_news(40)

# 8. Export des événements en JSON
with open("events.json", "w", encoding="utf-8") as json_file:
    json.dump(events, json_file, ensure_ascii=False, indent=4)

# 9. Export des actualités en YAML
with open("news.yaml", "w", encoding="utf-8") as yaml_file:
    yaml.dump(news, yaml_file, allow_unicode=True, sort_keys=False, default_flow_style=False)

print("Les fichiers 'events.json' et 'news.yaml' ont été générés avec succès !")
