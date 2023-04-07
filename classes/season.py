class Season:
    def __init__(self, name, flavor_text, season_effect):
        self.name = name
        self.flavor_text = flavor_text
        self.season_effect = season_effect

    def getSeasonText(self):
        return self.name

spring = Season("Spring",'It is now spring! The birds have started chirping, and the sun peeks through the clouds. Energy production is not affected this round, as there is not enough sun to really power our solar cells more than usual. \n', 0)
summer = Season("Summer", 'It is now summer! The flowers are in bloom, and we are really feeling the heat. Energy production is increased by 3 energy units, as our solar cells can capture all the sun\' s rays, and Lake May Hospital\'s water mill spins. \n', 3)
fall = Season("Fall",'It is now fall! That means it is getting colder, and there is less sun. Energy production is decreased by 3 energy units in this season, as we now have less sun to rely on. \n', -3)
winter = Season("Winter",'It is now winter! The days have become a lot shorter, and we are starting to huddle up inside. Energy production is decreased by 6 energy units, as our communtiy battery is less effective in cold weather and we have very little sun for our solar cells. \n', -6)

season_list = [spring, summer, fall, winter]