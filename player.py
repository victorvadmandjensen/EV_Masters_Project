class Player:
    def __init__(self, role):
        self.role = role
        self.tokens = 0

    def enter_tokens_spent(self):
        to_actions = input('Spend tokens on action cards or player actions for the ' + self.role + ' player: ')
        #print('I spent ' + to_actions + ' tokens!')
        return to_actions
    
    def enter_tokens_battery(self):
        to_battery = input('Send tokens to battery for the ' + self.role + ' player: ')
        #print('I sent ' + to_battery + ' tokens!')
        return to_battery

    def update_tokens(self):        
        self.tokens = self.tokens - int(self.enter_tokens_spent()) - int(self.enter_tokens_battery())
        #print('Total: ' + str(self.tokens))

# define player objects
red = Player('Red')
green = Player('Green')
blue = Player('Blue')
yellow = Player('Yellow')

player_list = [red, green, blue, yellow]