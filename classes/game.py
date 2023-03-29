import classes.codi2 as codi2, classes.energy_decision as energy_decision, classes.event as event, classes.player as player, classes.season as season, time, classes.town_hall_upgrades as town_hall_upgrades, classes.data_collection_module as data_collection_module

class Game:
    def __init__(self):
        self.current_round = 0
        # current_season is an index for the season_list
        self.current_season = 0
        self.current_event = None
        self.event_list = event.event_list
        self.intro = 'Welcome to our energy community! We recently started and have just gotten everything set up. Now, it is your turn to be a part of the community and helps us reach a sustainable future. We have 1 year to prove to those around us that we can thrive as both a community and individuals. \n'
        self.outro = 'Thank you for working with our energy community! We enjoyed having you all, and hope you can help other energy communities thrive. \n'
        self.current_players = player.player_list
        self.total_to_battery = 0
        self.codi2 = codi2.CoDI2()
        # max_rounds is an attribute that considers the max number of rounds, it is 3 as we increment rounds from 0 to 1 when a season starts
        self.max_rounds = 3

    
    def run_game(self):
        print(self.intro)
        data_module = data_collection_module.Data_Collection_Module()
        data_module.initialize_workbook()
        for i in range(0, len(season.season_list)):
            # remember to move this outside to the start of the game when we have more events
            event.Event.reset_events(event.event_list)
            self.set_season(i)
            for j in range(0, self.max_rounds):
                self.set_round(j)
                data_module.add_energy_sent_to_battery(self.total_to_battery)
                data_module.add_event(self.current_event)
                self.end_round()
            self.town_hall_meeting()
        print(self.outro)
    
    # update total to battery with argument given
    def receive_tokens_battery(self, tokens_received):
        self.total_to_battery = self.total_to_battery + tokens_received

    # function to choose the season from the season_list based on a given int as index
    def set_season(self, season_counter):
        #season_to_show = season.season_list[season_counter]
        # if season is index 3 AKA winter we just return without incrementing
        if season_counter >= 3:
            return None
        self.current_season = self.current_season + 1 
        #return season_to_show
    
    def get_season(self):
        season_to_get = season.season_list[self.current_season]
        return season_to_get

    # method to start a round, reset relevant values and return events
    def start_round(self, round_counter):
        self.increment_round()
        self.total_to_battery = 0
        event_to_show = event.Event.randomize_event(self.event_list, self.current_season)
        self.current_event = event_to_show
        # if round is the third for a season then return the event - remember, we increment the round BEFORE this point
        if self.current_round > self.max_rounds:
            # set round to be 1 so that we can count correctly!
            self.current_round = 1
            return event_to_show
        return event_to_show
        #self.current_round = round_counter
        #self.current_event = event.Event.randomize_event(event.event_list,self.current_season)
        #print(self.current_event.getEventText())
        #self.total_to_battery = 0
        #self.player_data_entry()

    # method to increment the round counter - should be used in conjunction with other methods in the actual Flask app
    def increment_round(self):
        self.current_round = self.current_round + 1

    # method to end a round by distributing energy
    def end_round(self):
        self.codi2.determine_energy_amount(self.total_to_battery, self.event_list[self.current_event.id].event_effect, season.season_list[self.current_season].season_effect)
        return self.codi2.distribute_energy()

    # method to return an energy_decision based on the state of the CoDI2 object of the Game object
    def set_current_energy_decision(self):
        energy_decision = self.codi2.determine_energy_decision()
        # if statement to check if energy should be sold
        if self.codi2.energy_amount > 0 and self.current_round == 2:
            self.codi2.sell_energy()
            for player in self.current_players:
                player.tokens = player.tokens + energy_decision.tokens_consequence
            #self.increment_round()
            return energy_decision
        elif self.codi2.energy_amount <= 0:
            #self.increment_round()
            return energy_decision
        elif self.codi2.energy_amount >= 0 and self.current_round != 2:
            #self.increment_round()
            return None
        
    # method to apply inputted upgrade to attributes    
    def apply_upgrade(self, chosen_upgrade):
        upgrade = town_hall_upgrades.town_hall_upgrades_list[chosen_upgrade]
        for player in self.current_players:
            player.base_tokens = player.base_tokens + upgrade.token_effect
        self.codi2.energy_from_actors = self.codi2.energy_from_actors + upgrade.energy_effect
        print(upgrade.flavor_text)

    def town_hall_meeting(self):
        print("Now the season is over! You should now discuss how you think it went, and what life in this energy community looked like.")
        time.sleep(60)
        print("You can now vote for a community upgrade.")
        for i in town_hall_upgrades.town_hall_upgrades_list:
            print("Option " + str(i.ID) + ": " + i.name + ". " + i.flavor_text )
        upgrade_votes = []
        for j in self.current_players:
            chosen_upgrade = input("Type the ID of the option the " + j.role + " player wants to vote for: ")
            upgrade_votes.append(int(chosen_upgrade) )
        for k in town_hall_upgrades.town_hall_upgrades_list:
            #print(upgrade_votes.count(k.ID))
            if upgrade_votes.count(k.ID) >= 3:
                print("Option " + str(k.ID) + " won!")
                for player in self.current_players:
                    player.base_tokens = player.base_tokens + k.token_effect
                self.codi2.energy_from_actors = self.codi2.energy_from_actors + k.energy_effect
                break
        else:
            print("There was no majority, and you get no upgrades.")