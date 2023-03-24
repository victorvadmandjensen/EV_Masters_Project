class Season:
    def __init__(self, name, flavor_text, season_effect):
        self.name = name
        self.flavor_text = flavor_text
        self.season_effect = season_effect

    def getSeasonText(self):
        return self.name

spring = Season("Spring",'It is now spring! Energy production is not affected this round. \n', 0)
summer = Season("Summer", 'It is now summer! Energy production is increased by 3 energy units. \n', 3)
fall = Season("Fall",'It is now fall! Energy production is not affected this round. \n', 0)
winter = Season("Winter",'It is now winter! Energy production is decreased by 3 energy units. \n', -3)

season_list = [spring, summer, fall, winter]