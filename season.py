class Season:
    def __init__(self, name, season_effect):
        self.name = name
        self.season_effect = season_effect

spring = Season('Spring', 0)
summer = Season('Summer', 3)
fall = Season('Fall', 0)
winter = Season('Winter', -3)

season_list = [spring, summer, fall, winter]