class Energy_Decision:
    def __init__(self, severity_min, severity_max, flavor_text, tokens_consequence):
        self.severity_min = severity_min
        self.severity_max = severity_max
        self.flavor_text = flavor_text
        self.tokens_consequence = tokens_consequence

# excess

severe_excess = Energy_Decision(21, 100, 'This is a severe excess!', 0)
moderate_excess = Energy_Decision(11, 20, 'This is a moderate excess!', 5)
mild_excess = Energy_Decision(1, 10, 'This is a mild excess!', 0)

# equilibrium
equilibrium = Energy_Decision(0, 0, 'This is an equilibirum!', 0)

# deficit
mild_deficit = Energy_Decision(-3, -1, 'This is a mild deficit!', 0)
moderate_deficit = Energy_Decision(-8, -4, 'This is a moderate deficit!', 0)
severe_deficit = Energy_Decision(-100, -9, 'This is a servere deficit!', 0)

energy_decision_list = [severe_excess, moderate_excess, mild_excess, equilibrium, mild_deficit, moderate_deficit, severe_deficit]