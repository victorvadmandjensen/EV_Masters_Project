import random

class Event:
    def __init__(self, id, name, flavor_text, event_effect, season):
        self.id = id
        self.name = name
        self.flavor_text = flavor_text
        self.event_effect = event_effect
        # season is a number - 0 for spring, 1 for summer, 2 for fall, 3 for winter
        self.season = season
        self.chosen_this_game = False

    def getEventText(self):
        return self.flavor_text

    # static method for the Event class to identify a random event
    @staticmethod
    def randomize_event(event_list, season):
        event_index = random.randint(0, len(event_list)-1)
        # this while loop breaks after there are no events with chosen_this_game == False
        # while loop to get events that are neither chosen nor in another season
        while event_list[event_index].chosen_this_game == True or event_list[event_index].season != season:
            event_index = random.randint(0, len(event_list)-1)
        # if event_list[event_index.season] == season:
            # get the event_list index item and set chosen this game to True
            # return the item
        # else:
            #Event.randomize_event()
        event_list[event_index].chosen_this_game = True        
        return event_list[event_index]
    
    @staticmethod
    def reset_events(event_list):
        for i in range(0, len(event_list)):
            event_list[i].chosen_this_game = False

event_blizzard = Event(0, 'Bilzzard in spring!', 'There has been an unexpected blizzard in the energy community! The community now needs 4 more energy units stored in the community battery at the end of this round.', -4, 0)
event_allergy = Event(1, 'Allergy in the community!', 'There has been an allergy outbreak in the energy community! The hospital requires 5 more energy units stored in the community battery at the end of this round.', -5, 0)
event_algorithm = Event(2, 'Sorry!', 'The algorithm has made a mistake! CoDI-2 has sold some energy prematurely, and the community battery requires one more energy stored in the community battery at the end of this round.', -1, 0)

event_list = [event_blizzard, event_allergy, event_algorithm]