class Player:
    def __init__(self, role, base_tokens):
        self.role = role
        self.tokens = 0
        self.base_tokens = base_tokens

    def update_tokens(self, tokens_spent, tokens_battery):        
        self.tokens = self.tokens - tokens_spent - tokens_battery
        #print('Total: ' + str(self.tokens))

    def receive_tokens(self):
        self.tokens = self.tokens + self.base_tokens

# define player objects
red = Player('red', 5)
green = Player('green', 6)
blue = Player('blue', 5)
yellow = Player('yellow', 6)

player_list = [yellow, red, blue, green]