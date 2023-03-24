from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# below we only important strings, integers and submissions from wtforms, and we have to import more options
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

import classes.game as game, classes.codi2 as codi2, classes.energy_decision as energy_decision, classes.event as event, classes.player as player, classes.season as season, time, classes.town_hall_upgrades as town_hall_upgrades, classes.data_collection_module as data_collection_module


app = Flask(__name__)

app.config["SECRET_KEY"] = "AOlTC1BKqkaOjwUbMKrdNlTSzm2FQymg"

Bootstrap(app)

# to run Flask so others can access it while on the same network type the below in the CLI
# python -m flask --no-debug run --host=0.0.0.0

# create form template for players
# all IntegerFields have to be non-zero to be valid
class NameForm(FlaskForm):
    tokens_action_cards = IntegerField('How many tokens have you spent on action cards?', validators=[DataRequired()])
    tokens_battery = IntegerField('How many tokens will you send to the battery?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# initialize game object
game = game.Game()

@app.route("/server", methods=["GET", "POST"])
def show_tokens():
    tokens_in_battery = game.total_to_battery
    return render_template("server.html", tokens_in_battery = tokens_in_battery)

# route to show season and get it based on the game objects current_season
@app.route("/season", methods=["GET", "POST"])
def show_season():
    season = game.set_season(game.current_season)
    return render_template("season.html", season = season)


# route for the blue player
@app.route("/blue", methods=["GET", "POST"])
def blue_player():
    form = NameForm()
    name_of_player = "blue"
    if form.validate_on_submit():
        tokens_for_action_cards = form.tokens_action_cards.data
        tokens_for_battery = form.tokens_battery.data
        game.receive_tokens_battery(tokens_for_battery)
        #print(tokens_for_battery)
        #print(game.total_to_battery)
    return render_template("player.html", form=form, name_of_player=name_of_player)

# route for the red player
@app.route("/red", methods=["GET", "POST"])
def red_player():
    form = NameForm()
    name_of_player = "red"
    if form.validate_on_submit():
        tokens_for_action_cards = form.tokens_action_cards.data
        tokens_for_battery = form.tokens_battery.data
        game.receive_tokens_battery(tokens_for_battery)
        #print(tokens_for_battery)
        #print(game.total_to_battery)
    return render_template("player.html", form=form, name_of_player=name_of_player)
