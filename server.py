import json
from datetime import datetime
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
    for club in clubs_list:
        if club['email'] == email:
            return club
    return None


def find_by_name(items, name):
    for item in items:
        if item['name'] == name:
            return item
    return None

MAX_PLACES_PER_CLUB = 12
bookings = {}


def get_booked_places(club, competition):
    return bookings.get(competition['name'], {}).get(club['name'], 0)


def book_places(club, competition, places):
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places
    club['points'] = int(club['points']) - places
    competition_bookings = bookings.setdefault(competition['name'], {})
    competition_bookings[club['name']] = get_booked_places(club, competition) + places


def is_past_competition(competition):
    competition_date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    return competition_date < datetime.now()


def parse_places(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def validate_booking(club, competition, places):
    if places <= 0:
        return "Sorry, the number of places must be greater than 0."
    if is_past_competition(competition):
        return "Sorry, this competition has already taken place."
    if get_booked_places(club, competition) + places > MAX_PLACES_PER_CLUB:
        return "Sorry, you cannot book more than 12 places per competition."
    if places > int(competition['numberOfPlaces']):
        return "Sorry, there are not enough places left in this competition."
    if places > int(club['points']):
        return "Sorry, you do not have enough points."
    return None


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.context_processor
def template_helpers():
    return {'is_past_competition': is_past_competition}

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
def book(competition, club):
    foundClub = find_by_name(clubs, club)
    foundCompetition = find_by_name(competitions, competition)
    if foundClub is None:
        flash("Something went wrong-please try again")
        return render_template('index.html')
    if foundCompetition is None:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub, competitions=competitions)
    return render_template('booking.html', club=foundClub, competition=foundCompetition)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = parse_places(request.form.get('places', ''))
    if placesRequired is None:
        flash("Sorry, please enter a valid number of places.")
        return render_template('booking.html', club=club, competition=competition)
    error = validate_booking(club, competition, placesRequired)
    if error:
        flash(error)
        return render_template('booking.html', club=club, competition=competition)
    book_places(club, competition, placesRequired)
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)




@app.route('/logout')
def logout():
    return redirect(url_for('index'))