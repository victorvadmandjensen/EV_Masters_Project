import energy_decision

class CoDI2:
    def __init__(self):
        self.energy_amount = 0
        self.energy_required = 21
        self.energy_from_actors = 15
    
    def determine_energy_amount(self, tokens_recieved, event_effect, season_effect):
        self.energy_amount = self.energy_amount + int(tokens_recieved) + event_effect + season_effect + self.energy_from_actors

    def distribute_energy(self):
        self.energy_amount = self.energy_amount - self.energy_required
        statement_distribution = "The current energy in the community battery is: " + str(self.energy_amount)
        return statement_distribution

    def determine_energy_decision(self):
        for i in energy_decision.energy_decision_list:
            if i.severity_min <= self.energy_amount <= i.severity_max:
                return i
        
    def sell_energy(self):
        self.energy_amount = 0
        statement_sell = "I have now sold the excess energy in the community battery. The current energy in the battery is: " + str(self.energy_amount)
        return statement_sell

codi2 = CoDI2()
