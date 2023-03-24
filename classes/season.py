class Season:
    def __init__(self, name, season_effect):
        self.name = name
        self.season_effect = season_effect

    def getSeasonText(self):
        return self.name

spring = Season('It is now spring! Energy production is not affected this round. \n', 0)
summer = Season('It is now summer! Energy production is increased by 3 energy units. \n', 3)
fall = Season('It is now fall! Energy production is not affected this round. \n', 0)
winter = Season('It is now winter! Energy production is decreased by 3 energy units. \n', -3)

season_list = [spring, summer, fall, winter]