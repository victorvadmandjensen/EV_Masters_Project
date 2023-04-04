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
    
    # static method to get list of events that have passed in a season
    @staticmethod
    # take the game object's event_list and a season index as parameters
    def get_events(event_list, season):
        chosen_events = []
        for event in event_list:
            if event.chosen_this_game == True and event.season == season:
                chosen_events.append(event)
        # return the list of chosen events
        return chosen_events


# event objects are created
event_blizzard = Event(0, 'Bilzzard in spring!', 'There has been an unexpected blizzard in the energy community! The community now needs 4 more energy units stored in the community battery at the end of this round.', -4, 0)
event_allergy = Event(1, 'Allergy in the community!', 'There has been an allergy outbreak in the energy community! The hospital requires 5 more energy units stored in the community battery at the end of this round.', -5, 0)
event_algorithm = Event(2, 'Sorry!', 'The algorithm has made a mistake! CoDI-2 has sold some energy prematurely, and the community battery requires one more energy stored in the community battery at the end of this round.', -1, 0)

event_heatwave = Event(3, 'Heatwave!', 'Summer is hot - much hotter than expected. As a result, a bunch of solar panels in the community have overheated and the community now needs 3 more energy units stored in the community battery at the end of this round to make up for this.', -3, 1)
event_icecream = Event(4, 'Ice cream fun!', 'It is the perfect weather for ice cream and many in the community has taken to spending time outside. This means that the community battery will need 2 less energy this round.', 2, 1)
event_eriksen = Event(5, 'Community member in need!', 'The Eriksen family recently had their energy production means destroyed, so CoDI-2 has decided to prioritize keeping their lights on. Since it is summer, it has decided to turn off heating units all over the community to ensure we have enough energy for everyone.', 0, 1)

event_saving = Event(6, 'Saving week!', 'Since it is getting darker and winter is approaching, the community has decided to host a saving week. Everyone is encouraged participate by limiting their energy and token use.', 0, 2)
event_gas = Event(7, 'Gas leak!', 'There has been a gas leak at the local school! In order to take care of this as quickly as possible, the community battery requires 5 additional energy stored in it at the end of this round.', -5, 2)
event_algorithm2 = Event(8, 'Another mistake!', 'The algorithm has unfortunately made another mistake! CoDI-2 has sold some energy prematurely, and the community battery requires three more energy stored in the community battery at the end of this round.', -3, 2)

event_newyear = Event(9, 'New Year, new injuries!', 'With New Year coming up, the hospital will need more energy to ensure they can treat any injuries that may arise. The community now needs 4 more energy units stored in the community battery at the end of this round.', -4, 3)
event_christmas = Event(10, 'Merry Christmas!', 'Christmas lights are up and electricity demands are high! The community requires 3 more energy units stored in the community battery at the end of this round.', -3, 3)
event_wind = Event(11, 'Wind!', 'It has been especially windy lately and windmills all over the energy community are thriving. The community requires 2 less energy at the end of this round.', 2, 3)

# add all event objects to the event_list
event_list = [event_blizzard, event_allergy, event_algorithm, event_heatwave, event_icecream, event_eriksen, event_algorithm2, event_saving, event_gas, event_newyear, event_christmas, event_wind]