import codi2, energy_decision, event, game, player, season

# define player objects
red = player.Player('Red')
green = player.Player('Green')
blue = player.Player('Blue')
yellow = player.Player('Yellow')

player_list = [red, green, blue, yellow]

# print(red.role)
# print(green.tokens)
# print(event.event_blizzard.event_effect)
# print(season.summer.season_effect)

codi2 = codi2.codi2

for j in range(0,3):
    current_event = event.event_list[j]
    print(current_event.flavor_text)
    total_to_battery = 0
    for i in player_list:
        total_to_battery = total_to_battery + int(i.enter_tokens_battery())
    codi2.determine_energy_amount(total_to_battery, current_event.event_effect, season.spring.season_effect)
    print(codi2.energy_amount)
    print(codi2.distribute_energy())
    print(codi2.determine_energy_decision().flavor_text)