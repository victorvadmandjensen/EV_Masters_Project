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
            player.enter_tokens_spent()
            self.total_to_battery = self.total_to_battery + int(player.enter_tokens_battery())
            player.update_tokens()


    def randomize_event(self):
        event_index = random.randint(0, len(event.event_list))
        return event.event_list[event_index]

    def end_round(self):
        codi2.determine_energy_amount(self.total_to_battery, self.current_event.event_effect, self.current_season.season_effect)
        codi2.distribute_energy()
        print(codi2.determine_energy_decision().flavor_text)

