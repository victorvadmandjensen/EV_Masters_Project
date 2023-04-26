class Player:
    def __init__(self, role, base_tokens, title_color, bg_color):
        self.role = role
        self.tokens = 0
        self.base_tokens = base_tokens
        self.title_color = title_color
        self.bg_color = bg_color

    def update_tokens(self, tokens_spent, tokens_battery):        
        self.tokens = self.tokens - tokens_spent - tokens_battery
        #print('Total: ' + str(self.tokens))

    def receive_tokens(self):
        self.tokens = self.tokens + self.base_tokens

# define player objects
red = Player('red', 5, "#903E33", "#DE7162")
green = Player('green', 6, "#035E1E", "#2F8E4B")
blue = Player('blue', 5, "#26889D", "#A7E8F1")
yellow = Player('yellow', 6, "#E6AB26", "#F0E963")

player_list = [yellow, red, blue, green]