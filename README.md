# Intro
```
Hey,

Je viens de recevoir le rapport de QA pour la phase 1 du projet. Il y a plusieurs bogues, dont un qui fait planter l'application ! 
Malheureusement, je ne suis pas au bureau pour les prochains jours (un de mes enfants est tombé malade ce week-end). 
Je ne sais pas encore quand je pourrai être là dans la semaine. Pourriez-vous prendre en charge la mise en œuvre du projet ? 
Vous devrez régler les bogues de la phase 1 et mettre en œuvre les éléments de la phase 2 (j'ai ajouté le travail de la phase 2 et les bogues de la section “issues” du repo). 

Vous devrez cloner et forker le repo et le mettre en place sur votre machine locale (tout ce dont vous avez besoin se trouve dans le fichier README). 
Ensuite, passez en revue les bogues dans la section des problèmes, puis essayez de reproduire les problèmes sur votre machine locale pour résoudre les bogues et ajouter la gestion des erreurs. 
Pour gagner du temps de configuration, nous utilisons Flask et JSON pour éviter d'utiliser une base de données. 
La plupart des outils dont vous aurez besoin se trouvent dans le fichier requirements.txt dans le repo, 
mais vous devrez installer Flask et notre framework de test préféré, pytest, ainsi que notre outil de test de performance, Locust. 

Vous devrez également préparer un rapport de test et un rapport de performances, 
conformément au guide de développement à la fin des spécifications fonctionnelles ci-jointes. 
Veillez à suivre toutes les directives, car le QA nous reproche de ne pas respecter les normes. 
Vous devez tester de manière approfondie les résultats requis (à la fois les happy paths et les sad paths) pour toutes les fonctionnalités de l'application.  
Je vous encourage également à adopter une approche de TDD, car cela vous aidera à rationaliser votre travail. 

Une fois que vous aurez terminé, nous ferons un examen de ce que vous avez dans la branche QA du code. 
Nous examinerons les rapports et la manière dont vous avez résolu les problèmes, 
nous examinerons votre code et nous testerons la couverture de la nouvelle fonctionnalité. 

Merci !

```
1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.
   
 6. Flake8 Report 

    Le rapport flake8 se trouve dans rapports/flake8/index.html : aucune erreur dans les 29 fichiers analyses.
    Pour le regenerer (dans env_outils) : flake8 --format=html --htmldir=rapports/flake8
    Documentation : [flake8](https://flake8.pycqa.org/)

7. Configurations particulieres (Windows)

    * Python 3.11 obligatoire : les versions du requirements.txt (Werkzeug 1.0.1) ne fonctionnent pas
      avec Python 3.12 et plus (erreur "module 'ast' has no attribute 'Str'", constatee avec Python 3.15)
    * Creer l'environnement virtuel : py -3.11 -m virtualenv env
    * L'activer : env\Scripts\activate (equivalent Windows de source bin/activate)
    * Installer les paquets : pip install -r requirements.txt
    * Lancer l'application : $env:FLASK_APP="server.py" puis python -m flask run
    * Locust et flake8 ont besoin d'un Flask recent, incompatible avec Flask 1.1.2.
      Ils sont donc installes dans un second environnement, env_outils :
      py -3.11 -m virtualenv env_outils
      env_outils\Scripts\activate
      pip install -r requirements-outils.txt

8. Tests et rapports

    * Framework de test : [pytest](https://docs.pytest.org/) avec [pytest-cov](https://pytest-cov.readthedocs.io/)
    * Lancer les tests (dans env) : python -m pytest
    * Emails acceptes pour se connecter (fichier clubs.json) :
        - john@simplylift.co (Simply Lift, 13 points)
        - admin@irontemple.com (Iron Temple, 4 points)
        - kate@shelifts.co.uk (She Lifts, 12 points)
    * Organisation des tests :
        - tests/unit : 61 tests unitaires
        - tests/integration : 28 tests d'integration
        - tests/functional : 3 tests fonctionnels
        - tests/performance : scenario Locust
    * Rapport de tests et de couverture (dans env) :
      python -m pytest --cov=server --cov-report=html:rapports/couverture
      Resultat : rapports/couverture/index.html (couverture de 100 %)
    * Rapport de performance avec [Locust](https://docs.locust.io/) (dans env_outils, application lancee) :
      locust -f tests/performance/locustfile.py --host http://127.0.0.1:5000 --users 6 --spawn-rate 6 --run-time 1m --headless --html rapports/rapport_performance.html
      Resultat : rapports/rapport_performance.html
      (6 utilisateurs, temps maximum : 40 ms pour un chargement, 13 ms pour une mise a jour)

9. Conventions de nommage

    * Branche principale : main (equivalent de master dans le guide de developpement)
    * Branches : bug/nom-du-bogue, amelioration/nom-de-l-amelioration, fonctionnalite/nom-de-la-fonctionnalite
    * Messages de commit :
        - test : test ecrit avant la correction (TDD)
        - fix : correction d'un bogue
        - feat : nouvelle fonctionnalite
        - style, perf, data, config, docs : qualite du code, performance, donnees, configuration, documentation
    * La branche QA est creee depuis main pour la revue, et n'est jamais fusionnee dans main.

10. Apparence

    * Une feuille de style simple se trouve dans static/style.css. Elle est reliee aux 4 pages HTML du dossier templates.    
    


