class Player:
    def __init__(self, role):
        self.role = role
        self.tokens = 0

    def enter_tokens_spent(self):
        to_actions = int(input('Spend tokens on action cards or player actions for the ' + self.role + ' player: ') )
        #print('I spent ' + to_actions + ' tokens!')
        return to_actions
    
    def enter_tokens_battery(self):
        to_battery = int(input('Send tokens to battery for the ' + self.role + ' player: ') )
        #print('I sent ' + to_battery + ' tokens!')
        return to_battery

    def update_tokens(self, tokens_spent, tokens_battery):        
        self.tokens = self.tokens - tokens_spent - tokens_battery
        #print('Total: ' + str(self.tokens))

# define player objects
red = Player('Red')
green = Player('Green')
blue = Player('Blue')
yellow = Player('Yellow')

player_list = [red, green, blue, yellow]