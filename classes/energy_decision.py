class Energy_Decision:
    def __init__(self, severity_min, severity_max, flavor_text, tokens_consequence):
        self.severity_min = severity_min
        self.severity_max = severity_max
        self.flavor_text = flavor_text
        self.tokens_consequence = tokens_consequence

# excess

severe_excess = Energy_Decision(21, 100, 'This is a severe excess! This means we sell the energ, but you also lose 1 environmental point on the community meter, because we have to keep the battery in good shape without it being overloaded. \n', 0)
moderate_excess = Energy_Decision(11, 20, 'This is a moderate excess! This means we sell the energy and get some returns. Everybody receives 3 tokens, and you get the following points on the community meter: 1 morale, 1 environmental, and 2 economic. \n', 3)
mild_excess = Energy_Decision(1, 10, 'This is a mild excess! This means we sell the energy, but not enough to get any returns. You get the folloing points on the community meter: 1 economic, and 1 morale. \n', 0)

# equilibrium
equilibrium = Energy_Decision(0, 0, 'This is an equilibirum! You get neither tokens nor community meter points this time. \n', 0)

# deficit
mild_deficit = Energy_Decision(-3, -1, 'This is a mild deficit! You get 0 tokens, but you lose 1 morale point on the community meter, as morale in the community drops from the implemented curfew. \n', 0)
moderate_deficit = Energy_Decision(-8, -4, 'This is a moderate deficit! As you are now forced by the system to turn of appliances, you lose the following points on the community meter: 1 environmental, 1 morale, and 1 economic. \n', 0)
severe_deficit = Energy_Decision(-100, -9, 'This is a servere deficit! You can now only use either a action card or a player action in the next round. Due to the community having to buy energy from the national grid, you also lose the following points on the community meter: 2 environmental, 2 social, and 2 economic. \n', 0)

energy_decision_list = [severe_excess, moderate_excess, mild_excess, equilibrium, mild_deficit, moderate_deficit, severe_deficit]