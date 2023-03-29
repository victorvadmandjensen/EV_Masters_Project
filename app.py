from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# below we only important strings, integers and submissions from wtforms, and we have to import more options
from wtforms import StringField, SubmitField, IntegerField, ValidationError
from wtforms.validators import InputRequired, NumberRange, StopValidation

import classes.game as game, classes.codi2 as codi2, classes.energy_decision as energy_decision, classes.event as event, classes.player as player, classes.season as season, time, classes.town_hall_upgrades as town_hall_upgrades, classes.data_collection_module as data_collection_module

# if we want to change the base Bootstrap template check venv/Lib\site-packages/flask_bootstrap/templates\boostrap to find it

app = Flask(__name__)

app.config["SECRET_KEY"] = "AOlTC1BKqkaOjwUbMKrdNlTSzm2FQymg"

Bootstrap(app)

# to run Flask so others can access it while on the same network type the below in the CLI
# python -m flask --no-debug run --host=0.0.0.0

# create form template for players
# all NumberRange fields have to be minimum zero to be valid - we use InputRequired() (and not DataRequired()), as the former
# just looks for input, while the latter looks for non-zero input
class NameForm(FlaskForm):
    tokens_action_cards = IntegerField('How many tokens have you spent on action cards and/or player actions?', validators=[NumberRange(min=0,max=20, message=""), InputRequired()])
    tokens_battery = IntegerField('How many tokens will you send to the battery?', validators=[NumberRange(min=0,max=20, message=""), InputRequired()])
    submit = SubmitField('Submit')

    # custom validation method - right now it does not quite work, because it for some reason does not let the player lose tokens
    #def check_for_token_validation(form, max_tokens):
     #   if (int(form.tokens_action_cards.data) + int(form.tokens_battery.data)) > max_tokens:
            #print(form.tokens_action_cards.data + form.tokens_battery.data)
      #      raise ValidationError(message="FUCK OFF")
       # else:
        #    return True

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
    return render_template("energy_decision.html", energy_distribution_statement = energy_distribution_statement, energy_decision = game.set_current_energy_decision())

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
        return redirect(url_for("show_season"))


# route for the red player
@app.route("/red", methods=["GET", "POST"])
def red_player():
    # set up form
    form = NameForm()
    # get red player based on index
    red_player_object = game.current_players[1]
    # set tokens_spent as 0 by default
    tokens_spent = 0
    # check if the form is valid
    if form.validate_on_submit():
        tokens_for_action_cards = form.tokens_action_cards.data
        tokens_for_battery = form.tokens_battery.data
        print(f"Player has {red_player_object.tokens} tokens, and the sum is { sum( [tokens_for_action_cards, tokens_for_battery] ) }" )
        # if the sum of tokens entered is larger than the player's tokens then raise a StopValidation error
        if sum( [tokens_for_action_cards, tokens_for_battery] ) > red_player_object.tokens:
            raise StopValidation(message="TURN BACK")
        tokens_spent = tokens_for_action_cards + tokens_for_battery
        # provide game object tokens and update the player object's tokens
        game.receive_tokens_battery(tokens_for_battery)
        red_player_object.update_tokens(tokens_for_action_cards, tokens_for_battery)
        # create a form object with formdata = None to clear the fields
        form = NameForm(formdata = None)
    # run the receive_tokens() method on the player object - we do that here because if it is above the form validation statement
    # then the player would receive tokens BEFORE the form validation, meaning they would always have 7 more tokens than shown
    red_player_object.receive_tokens()
    # render the tame plate with arguments we want to display for the client
    return render_template("player.html", form=form, player_object = red_player_object, tokens_spent = tokens_spent)


# route for the blue player
@app.route("/blue", methods=["GET", "POST"])
def blue_player():
    # set up form
    form = NameForm()
    # get blue player based on index
    blue_player_object = game.current_players[2]
    # set tokens_spent to 0 as default
    tokens_spent = 0
    # check if the form is valid
    if form.validate_on_submit():
        tokens_for_action_cards = form.tokens_action_cards.data
        tokens_for_battery = form.tokens_battery.data
        print(f"Player has {blue_player_object.tokens} tokens, and the sum is { sum( [tokens_for_action_cards, tokens_for_battery] ) }" )
        # if the sum of tokens entered is larger than the player's tokens then raise a StopValidation error
        if sum( [tokens_for_action_cards, tokens_for_battery] ) > blue_player_object.tokens:
            raise StopValidation(message="TURN BACK")
        tokens_spent = tokens_for_action_cards + tokens_for_battery
        # provide game object tokens and update the player object's tokens
        game.receive_tokens_battery(tokens_for_battery)
        blue_player_object.update_tokens(tokens_for_action_cards, tokens_for_battery)
        # create a form object with formdata = None to clear the fields
        form = NameForm(formdata = None)
    # run the receive_tokens() method on the player object - we do that here because if it is above the form validation statement
    # then the player would receive tokens BEFORE the form validation, meaning they would always have 7 more tokens than shown
    blue_player_object.receive_tokens()
    # render the tame plate with arguments we want to display for the client
    return render_template("player.html", form=form, player_object = blue_player_object, tokens_spent = tokens_spent)
