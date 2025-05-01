# 🌐 Flask Azure App

Ce projet est une application web développée avec Flask, intégrée à Azure Blob Storage pour la gestion de contenu. Elle permet d'afficher des événements et des actualités stockés dans des fichiers JSON et YAML hébergés sur Azure.

## 🚀 Fonctionnalités

- **Affichage statique** des événements et actualités depuis Azure Blob Storage.
- **Utilisation de `DefaultAzureCredential`** pour une authentification sécurisée avec Azure.
- **Rendu des pages** via des templates.
- **Déploiement** via Azure Kubernetes Service.

## 🛠️ Prérequis

- Python 3.11+
- Un compte Azure avec un conteneur Blob Storage configuré.
- Variables d'environnement configurées :
  - `AZURE_STORAGE_URL`
  - `AZURE_SAS_TOKEN` 

## 📦 Installation

```bash
git clone https://github.com/hilary-tchokote/Flask-Azure-App.git
cd Flask-Azure-App
pip install -r requirements.txt


