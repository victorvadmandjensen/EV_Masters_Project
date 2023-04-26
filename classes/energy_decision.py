class Energy_Decision:
    def __init__(self, severity_min, severity_max, flavor_text, tokens_consequence):
        self.severity_min = severity_min
        self.severity_max = severity_max
        self.flavor_text = flavor_text
        self.tokens_consequence = tokens_consequence

# excess

severe_excess = Energy_Decision(21, 100, 'This is a severe excess! This means we sell the energy, but we also lose 1 environment point on the community meter. This is due to repair costs from the battery being overloaded. \n', 0)
moderate_excess = Energy_Decision(11, 20, 'This is a moderate excess! This means we sell the energy and get some returns. Everybody receives 3 tokens as a bonus; thank you for your good work. You also get the following points on the community meter: 1 morale, 1 environmental, and 2 economic. \n', 3)
mild_excess = Energy_Decision(1, 10, 'This is a mild excess! This means we sell the energy. These profits will be used to cover upkeep of the battery. You get the folloing points on the community meter: 1 economic, and 1 morale. \n', 0)

# equilibrium
equilibrium = Energy_Decision(0, 0, 'This is an equilibirum! Everything is as it should be. You neither lose nor gain tokens or community meter points this time. \n', 0)

# deficit
mild_deficit = Energy_Decision(-3, -1, 'This is a mild deficit! In order to make up for this, we implement a curfew to restrict energy use in Energy City until the situation has stabilized. You lose 1 morale point on the community meter.\n', 0)
moderate_deficit = Energy_Decision(-8, -4, 'This is a moderate deficit! We are able to make up for this by shutting off lights in all private households from 8pm to 5am, and by buying some energy from nearby energy communities. You lose the following points on the community meter: 1 environmental, 1 morale, and 1 economic. \n', 0)
severe_deficit = Energy_Decision(-100, -9, 'This is a servere deficit! In order to have enough energy for everyone in the community, I had to buy energy from the national grid. As a result, you lose the following points on the community meter: 2 environmental, 2 social, and 2 economic. You can only use either an action card or a player action in the next round. \n', 0)

energy_decision_list = [severe_excess, moderate_excess, mild_excess, equilibrium, mild_deficit, moderate_deficit, severe_deficit]