"""
    Todo
        - Make program cleaner
        - Remove backslashes from export
"""

import os
from natsort import natsorted

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json


# Generates Game Titles
def title_gen(file):
    name = file.replace('Games\\', '')
    name = name.replace('.swf', '')
    name = name.replace('-', ' ')
    return name


gameList = []
game2Dict = []
directory = 'Games'

# Implement natsort
for game in os.listdir('Games'):
    temp = game.replace('.swf', '')
    game = temp.replace('-', ' ')
    gameList.append(game)

gameList = natsorted(gameList)

print(gameList)

for game in gameList:
    index = gameList.index(game)
    game = game.replace(' ', '-')
    game = game + '.swf'
    gameList[index] = game

print(gameList)


# Converts games to dict
for game in gameList:
    # print(game)
    game_name = title_gen(game).title()
    game_desc = game_name
    game_img = ""
    game_file = '/Games/' + game
    # print(game_file)
    game = dict(title=game_name, description=game_desc, image=game_img, file=game_file)
    game2Dict.append(game)
# print(game2Dict)

# Dict to  JSON
with open('gaems.json', 'w') as fp:
    json.dump(game2Dict, fp, indent=4)
