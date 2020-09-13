import pickle
import numpy as np

# *********** INSERT YOUR PLAYER NAME HERE ***********
player_name = 'Wakamar'
# ******** INSERT LIST OF AVAILABLE HEROES HERE ******
front_line = ['Ash', 'Barik', 'Inara', 'Ruckus']
dps = ['Tyra', 'Lian', 'Cassie', 'Buck', 'Moji', 'Lex']
support = ['Ying', 'Jenos', 'Grover', 'Furia', 'Pip']
# ****************************************************

# Get the list of past matches.
with open('match_list.pkl', 'rb') as f:
    match_list = pickle.load(f)
f.close()

team_hero_dict = {}
enemy_hero_dict = {}
map_dict = {}

# Iterates through past matches to process information. Records for each map, 
# teammate hero, and enemy hero the players wins and losses for each player hero.
for match in match_list:

    # Gets the champion of the player, the map, and whether they won.
    for i in match:
        if i['playerName'] == player_name:
            win_mult = 0
            if i['Win_Status'] == 'Winner':
                win = 1
                win_mult = 1
            elif i['Win_Status'] == 'Loser':
                win = 0
                win_mult = -1
            champion = i['Reference_Name']
            map_game = i['Map_Game']
            pts = abs(i['Team1Score'] - i['Team2Score']) * win_mult

    # Adds the map to the map dictionary and records under the player's hero
    # whether they won or lost on that map.
    map_list = map_game.split(' ')[1:]
    map_out = ' '
    map_out = map_out.join(map_list)
    if map_out not in map_dict:
        map_dict[map_out] = {}
    if champion not in map_dict[map_out]:
        map_dict[map_out][champion] = []
    map_dict[map_out][champion].append(pts)

    # Iterates through the non-player heroes.
    for i in match:
        if i['playerName'] != player_name:

            # Adds the teammate hero to the teammate hero dictionary and records
            # under the player's hero whether they won or lost with that teammate hero.
            if int(i['Win_Status'] == 'Winner') == win:
                if i['Reference_Name'] not in team_hero_dict:
                    team_hero_dict[i['Reference_Name']] = {}
                if champion not in team_hero_dict[i['Reference_Name']]:
                    team_hero_dict[i['Reference_Name']][champion] = []
                team_hero_dict[i['Reference_Name']][champion].append(pts)

            # Adds the enemy hero to the enemy hero dictionary and records
            # under the player's hero whether they won or lost with that enemy hero.
            if int(i['Win_Status'] == 'Winner') != win:
                if i['Reference_Name'] not in enemy_hero_dict:
                    enemy_hero_dict[i['Reference_Name']] = {}
                if champion not in enemy_hero_dict[i['Reference_Name']]:
                    enemy_hero_dict[i['Reference_Name']][champion] = []
                enemy_hero_dict[i['Reference_Name']][champion].append(pts)

this_map = ''
team_chars = []
enemy_chars = []

user_input = ''
# Gathers information on the in-progress draft and uses to make a recommendation.
# Makes a new recommendation each time a new piece of information is added.
while user_input != 'finish':

    # Get information on the map and picked heroes.
    print('Input new data:')
    print('For map: m map_name')
    print('For team hero: t hero_name')
    print('For enemy hero: e hero_name')
    print('To finish: finish')
    user_input = input()

    if user_input[0] == 'm':
        this_map = user_input[2:]
    elif user_input[0] == 't':
        team_chars.append(user_input[2:])
    elif user_input[0] == 'e':
        enemy_chars.append(user_input[2:])

    # Starts each available hero off at a 50% predicted win rate.
    char_dict = {}
    for i in front_line:
        char_dict[i] = [0]

    for i in dps:
        if i not in char_dict:
            char_dict[i] = [0]

    for i in support:
        if i not in char_dict:
            char_dict[i] = [0]

    # For each available hero, looks through that hero's history with the
    # current map, teammate heroes, and enemy heroes. Weights the map twice as
    # much as a single teammate or enemy hero.
    for i in char_dict:
        if this_map in map_dict:
            if i in map_dict[this_map]:
                for j in range(4):
                    char_dict[i].extend(map_dict[this_map][i])

        for j in team_chars:
            if j in team_hero_dict:
                if i in team_hero_dict[j]:
                    char_dict[i].extend(team_hero_dict[j][i])

        for j in enemy_chars:
            if j in enemy_hero_dict:
                if i in enemy_hero_dict[j]:
                    char_dict[i].extend(enemy_hero_dict[j][i])

    # Outputs the current situation for a sanity check.
    print(this_map, team_chars, enemy_chars)
    # Outputs the available characters, sorted by the historical points advantage with the
    # current map, teammate heroes, and enemy heroes.
    sorted_list = [(k, round(np.average(v), 1)) for k, v in \
                   sorted(char_dict.items(), key=lambda item: np.average(item[1]), \
                          reverse=True)]

    labels = ['1st place', '2nd place', '3rd place']
    reported = []
    count = 0
    while count < 3:
        for i in sorted_list:
            if i[0] not in reported and i[0] not in team_chars and i[0] not in enemy_chars:
                print(labels[count] + ' - ' + i[0] + ': ' + str(i[1]))
                count += 1
                reported.append(i[0])
                break

    for i in sorted_list:
        if i[0] in front_line and i[0] not in team_chars and i[0] not in enemy_chars:
            print('Top Front Line - ' + i[0] + ': ' + str(i[1]))
            break

    for i in sorted_list:
        if i[0] in dps and i[0] not in team_chars and i[0] not in enemy_chars:
            print('Top DPS - ' + i[0] + ': ' + str(i[1]))
            break

    for i in sorted_list:
        if i[0] in support and i[0] not in team_chars and i[0] not in enemy_chars:
            print('Top Support - ' + i[0] + ': ' + str(i[1]))
            break
