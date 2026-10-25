import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def find_club_by_email(email, clubs_list):
    """Retourne le club qui a cet email, ou None s'il n'existe pas."""
    for club in clubs_list:
        if club['email'] == email:
            return club
    return None


def book_places(club, competition, places):
    """Retire les places de la competition et les points du club (1 point = 1 place)."""
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places
    club['points'] = int(club['points']) - places


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def showSummary():
    club = find_club_by_email(request.form.get('email', ''), clubs)
    if club is None:
        flash("Sorry, this email is not registered.")
        return render_template('index.html')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    book_places(club, competition, placesRequired)
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)




@app.route('/logout')
def logout():
    return redirect(url_for('index'))