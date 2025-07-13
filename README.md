# creation d'un projet pour authentification    
```
- création du projet: mkdir wathup_auth
- accéder au dossier avec : cd wathup_auth
- création de environnement virtuel: python3.13 -m venv venv
- activer environnement virtuel sur Windows : venv\Scripts\activate 
- on installe django : pip install django   
- création d'un fiche requirement pour les librairies:  pip freeze > requirements.txt
- création d'un projet django : django-admin startproject auth 
```

### install quelques librairies:  

```   
- pip install python-decouple==3.8
- pip install Unipath==1.1
- pip install dj-database-url==2.3.0 
- pip install django-allauth==65.9.0
- pip install requests>=2.14.2
- pip install mysqlclient==2.2.7
- pip install jwt==1.4.0
- pip install django-user-agents==0.4.0
- mettre le requirements a jour avec la cmd si dessus
```

### configuration de app conf       
Il faut regarder les configurations dans le dossier l'application conf.     
j'ai crée un settings.ini et modifier le fichier settings.py, urls.py.


### NB: Je vais importé les templates que j'ai deja motifier a avance
il est important d'installer le paquege django-cryspy, pour le disign des   
des formulaires(https://django-crispy-forms.readthedocs.io/en/latest/).

# Different configuration step
        
### Voici le lien pour les différents étape a suivre
- [ ]  https://django-allauth.readthedocs.io/         
                  - Introduction                   
         

