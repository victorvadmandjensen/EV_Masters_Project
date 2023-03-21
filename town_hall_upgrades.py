class Town_Hall_Upgrades:
    def __init__(self, ID, name, flavor_text, energy_effect, token_effect):
        self.ID = ID
        self.name = name
        self.flavor_text = flavor_text
        self.energy_effect = energy_effect
        self.token_effect = token_effect

token_upgrade = Town_Hall_Upgrades(1, "Token upgrade", "Every player gets an extra token in every turn for the rest of the game.", 0, 1)
energy_upgrade = Town_Hall_Upgrades(2, "Energy upgrade", "All public institutions and private companies produce 1 more energy each round, for a total of 4 energy units.", 4, 0)

town_hall_upgrades_list = [token_upgrade, energy_upgrade]