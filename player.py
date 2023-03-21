class Player:
    def __init__(self, role, base_tokens):
        self.role = role
        self.tokens = 0
        self.base_tokens = base_tokens

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

    def receive_tokens(self):
        self.tokens = self.tokens + self.base_tokens

# define player objects
red = Player('Red', 6)
green = Player('Green', 7)
blue = Player('Blue', 6)
yellow = Player('Yellow', 7)

player_list = [red, green, blue, yellow]