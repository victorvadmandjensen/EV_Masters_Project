import codi2, energy_decision, event, player, season, random

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
        print(self.outro)

    def set_season(self, index):
        self.current_season = season.season_list[index]
        print(self.current_season.name)

    def set_round(self, index):
        self.current_round = index
        self.current_event = self.randomize_event()
        print(self.current_event.flavor_text)
        self.total_to_battery = 0
        for player in self.current_players:
            tokens_spent_current_player = player.enter_tokens_spent()
            tokens_battery_current_player = player.enter_tokens_battery()
            self.total_to_battery = self.total_to_battery + tokens_battery_current_player
            player.update_tokens(tokens_spent_current_player, tokens_battery_current_player)

    def randomize_event(self):
        event_index = random.randint(0, len(event.event_list)-1)
        return event.event_list[event_index]

    def end_round(self):
        self.codi2.determine_energy_amount(self.total_to_battery, self.current_event.event_effect, self.current_season.season_effect)
        print(self.codi2.distribute_energy() )
        if self.codi2.energy_amount > 0 and self.current_round == 2:
            print(self.codi2.determine_energy_decision().flavor_text)
            print(self.codi2.sell_energy())
        elif self.codi2.energy_amount <= 0:
            print(self.codi2.determine_energy_decision().flavor_text)

