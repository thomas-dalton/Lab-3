from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')


@app.route('/artists')
def artists():
    artists = ["John Brown's Body", "Gunpoets", "Donna The Buffalo", "The Blind Spots"]
    return render_template('artists.html', title='Artists', artists=artists)


@app.route('/artist')
def artist():
    name = "Gunpoets"
    hometown = "Ithaca"
    description = "Voice as a weapon, words as bullets, spreading the universal message of peace, love, " \
                  "and justice through music. Sure, there's a cynical cultural tendency to make certain assumptions " \
                  "when you hear the word 'gun' associated with rap music, " \
                  "but this seven-member live hip-hop band from Ithaca, NY, runs contrary to that image " \
                  "with their positive message and uplifting performances."

    events = ["The Commons on Thursday 9/6", "The Haunt next Friday 9/14"]

    return render_template('artist.html', title='Artist', name=name, hometown=hometown,
                           description=description, events=events)


@app.route('/new_artist', methods=['GET', 'POST'])
def new_artist():
    form = LoginForm()

    if form.validate_on_submit():
        flash('New artist created: '+ form.name.data)
        return render_template("artist.html", title="Artist", name=form.name.data, hometown=form.hometown.data,
                               description=form.description.data)

    return render_template('new_artist.html', title='New Artist', form=form)
