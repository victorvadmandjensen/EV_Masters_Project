from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# below we only important strings, integers and submissions from wtforms, and we have to import more options
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

import classes.game as game, classes.codi2 as codi2, classes.energy_decision as energy_decision, classes.event as event, classes.player as player, classes.season as season, time, classes.town_hall_upgrades as town_hall_upgrades, classes.data_collection_module as data_collection_module


app = Flask(__name__)

app.config["SECRET_KEY"] = "AOlTC1BKqkaOjwUbMKrdNlTSzm2FQymg"

Bootstrap(app)

# to run Flask so others can access it while on the same network type the below in the CLI
# python -m flask --no-debug run --host=0.0.0.0

# create form template for players
# all NumberRange fields have to be minimum zero to be valid
class NameForm(FlaskForm):
    tokens_action_cards = IntegerField('How many tokens have you spent on action cards and/or player actions?', validators=[NumberRange(min=0,max=20, message="")])
    tokens_battery = IntegerField('How many tokens will you send to the battery?', validators=[NumberRange(min=0,max=20, message="")])
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

# route to show an event and start a round
@app.route("/event", methods=["GET", "POST"])
def show_event():
    event = game.start_round(game.current_round)
    return render_template("event.html", event = event, current_round = game.current_round, season = game.current_season)

# route to end a round show energy_decisions 
@app.route("/energy_decision", methods=["GET", "POST"])
def show_energy_decision():
    energy_distribution_statement = game.end_round()
    energy_decision = game.set_current_energy_decision()
    return render_template("energy_decision.html", energy_distribution_statement = energy_distribution_statement, energy_decision = energy_decision)

# route to show town hall meeting text
@app.route("/town_hall_meeting", methods=["GET", "POST"])
def town_hall_meeting():
    return render_template("town_hall_meeting.html")

# route to show upgrades and let the players vote
@app.route("/upgrades", methods=["GET", "POST"])
def upgrades():
    # if the user gets data then render the page
    if request.method == "GET":
        return render_template("upgrades.html", upgrade_list = town_hall_upgrades.town_hall_upgrades_list)
    # else process form data
    else:
        # get value from the chosen radio button
        chosen_upgrade = int(request.form.get("radio_choice") )
        game.apply_upgrade(chosen_upgrade)
        #return redirect(url_for("show_season"))


# route for the red player
@app.route("/red", methods=["GET", "POST"])
def red_player():
    red_player_object = game.current_players[1]
    red_player_object.receive_tokens()
    form = NameForm()
    # if form is valid then send and update tokens
    if form.validate_on_submit():
        tokens_for_action_cards = form.tokens_action_cards.data
        tokens_for_battery = form.tokens_battery.data
        game.receive_tokens_battery(tokens_for_battery)
        red_player_object.update_tokens(tokens_for_action_cards,tokens_for_battery)
        #print(tokens_for_battery)
        #print(game.total_to_battery)
    return render_template("player.html", form=form, player_object = red_player_object)

# route for the blue player
@app.route("/blue", methods=["GET", "POST"])
def blue_player():
    # set up form
    form = NameForm()
    # get blue player based on index
    blue_player_object = game.current_players[2]
    blue_player_object.receive_tokens()
    if form.validate_on_submit():
        tokens_for_action_cards = form.tokens_action_cards.data
        tokens_for_battery = form.tokens_battery.data
        game.receive_tokens_battery(tokens_for_battery)
        blue_player_object.update_tokens(tokens_for_action_cards,tokens_for_battery)
        #print(tokens_for_battery)
        #print(game.total_to_battery)
    return render_template("player.html", form=form, player_object = blue_player_object)

