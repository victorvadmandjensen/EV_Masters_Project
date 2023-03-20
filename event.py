class Event:
    def __init__(self, name, flavor_text, event_effect, season):
        self.name = name
        self.flavor_text = flavor_text
        self.event_effect = event_effect
        self.season = season


event_blizzard = Event('Bilzzard in spring!', 'There has been an unexpected blizzard in the energy community! The community now needs 4 more energy unites stored in the community battery at the end of this round.', -4, 'Spring')