import energy_decision

class CoDI2:
    def __init__(self):
        self.energy_amount = 0
        self.energy_required = 21
    

    def determine_energy_amount(self, tokens_recieved, event_effect, season_effect):
        self.energy_amount = self.energy_amount + int(tokens_recieved) + event_effect + season_effect

    def distribute_energy(self):
        self.energy_amount = self.energy_amount - self.energy_required
        return self.energy_amount

    def determine_energy_decision():
        

codi2 = CoDI2()