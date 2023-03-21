import codi2, energy_decision, event, player, season, random, time, town_hall_upgrades

class Game:
    def __init__(self):
        self.current_round = None
        self.current_season = None
        self.current_event = None
        self.intro = 'Intro text here'
        self.outro = 'Outro text here'
        self.current_players = player.player_list
        self.total_to_battery = 0
        self.codi2 = codi2.CoDI2()
        self.max_rounds = 3

    
    def run_game(self):
        print(self.intro)
        for i in range(0, len(season.season_list)):
            self.set_season(i)
            for j in range(0, self.max_rounds):
                self.set_round(j)
                self.end_round()
            self.town_hall_meeting()
        print(self.outro)

    def set_season(self, index):
        self.current_season = season.season_list[index]
        print(self.current_season.name + "\n")

    def set_round(self, index):
        self.current_round = index
        self.current_event = self.randomize_event()
        print(self.current_event.flavor_text)
        self.total_to_battery = 0
        self.player_data_entry()
    
    def player_data_entry(self):
        for player in self.current_players:
            player.receive_tokens()
            print("The " + player.role + " player receives: " + str(player.base_tokens) + ". Your total is now: " + str(player.tokens) )
            tokens_spent_current_player = player.enter_tokens_spent()
            # print("Your total is now: " + str(player.tokens) )
            tokens_battery_current_player = player.enter_tokens_battery()
            self.total_to_battery = self.total_to_battery + tokens_battery_current_player
            player.update_tokens(tokens_spent_current_player, tokens_battery_current_player)
            print("Your total is now: " + str(player.tokens) + "\n")

    def randomize_event(self):
        event_index = random.randint(0, len(event.event_list)-1)
        return event.event_list[event_index]

    def end_round(self):
        self.codi2.determine_energy_amount(self.total_to_battery, self.current_event.event_effect, self.current_season.season_effect)
        print(self.codi2.distribute_energy() )
        energy_decision = self.codi2.determine_energy_decision()
        if self.codi2.energy_amount > 0 and self.current_round == 2:
            print(energy_decision.flavor_text)
            print(self.codi2.sell_energy())
            for player in self.current_players:
                player.tokens = player.tokens + energy_decision.tokens_consequence
        elif self.codi2.energy_amount <= 0:
            print(energy_decision.flavor_text)

    def town_hall_meeting(self):
        print("Now the season is over! You should now discuss how you think it went, and what life in this energy community looked like.")
        time.sleep(4)
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