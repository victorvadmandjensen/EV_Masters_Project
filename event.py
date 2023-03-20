class Event:
    def __init__(self, name, flavor_text, event_effect, season):
        self.name = name
        self.flavor_text = flavor_text
        self.event_effect = event_effect
        self.season = season


event_blizzard = Event('Bilzzard in spring!', 'There has been an unexpected blizzard in the energy community! The community now needs 4 more energy unites stored in the community battery at the end of this round.', -4, 'Spring')
event_allergy = Event('Allergy in the community!', 'There has been an allergy outbreak in the energy community! The hospital requires 5 more energy unites stored in the community battery at the end of this round.', -5, 'Spring')
event_algorithm = Event('Sorry!', 'The algorithm has made a mistake! CoDI-2 has sold some energy prematurely, and the community battery requires one more energy stored in the community battery at the end of this round.', -1, 'Spring')

event_list = [event_blizzard, event_allergy, event_algorithm]