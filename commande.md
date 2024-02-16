# création environnement virtuel
#python -m venv virtual_env

# activation de l'environnement virtuel
#virtual_env\Scripts\activate.bat

# installation de la dépendance Django
#pip install Django

# pour utiliser la base de donnée mysql il faut installer une dépendance mysqlclient
#pip install mysqlclient

# lancer le projet
#python manage.py runserver

# après ajout de classe dans le fichier models.py d'une application
#python manage.py makemigrations

# pour créer les tables dans la base de donnée
#python manage.py migrate

# créer un répertoire courant
#django-admin startproject mysite

# créer une application dans le répertoire
# python manage.py startapp nom_de_lapplication

# installation de la dépendance Pillow pour gérer le champ image
#python -m pip install Pillow


# lancer le server
#python manage.py runserver

# create un superuser
#python manage.py createsuperuser

# notion de décorateur
#@admin.register(Livre)

# pour utiliser une vue générique je dois importer django.views.generic import DetailView, importer le modèle sur lequel je veux interagir...

@login_required : permet de dire que le statut de connexion de la personne qui cherhce à exécuter une fonction doit être connecté...

1. mettre en place l'application de base pour l'authentification