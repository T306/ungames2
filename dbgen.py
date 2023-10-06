import os
import sqlite3
from natsort import natsorted


def title_gen(file):
    name = file.replace('Games\\', '')
    name = name.replace('.swf', '')
    name = name.replace('-', ' ')
    return name


gameList = []
game2Dict = []
directory = 'Games'

if os.path.exists("../../!Downloads/UnGames2/identifier.sqlite"):
    connection = sqlite3.connect("../../!Downloads/UnGames2/identifier.sqlite")
    cursor = connection.cursor()
    statement = "INSERT INTO Games VALUES (?, ?, ?, ?)"
else:
    connection = sqlite3.connect("../../!Downloads/UnGames2/identifier.sqlite")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Games (title TEXT, description TEXT, images TEXT, file TEXT)")
    statement = "INSERT INTO Games VALUES (?, ?, ?, ?)"


cursor.execute("DELETE FROM Games;")

# Implement natsort
for game in os.listdir('../../!Downloads/UnGames2/Games'):
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

print(game2Dict)

for x in game2Dict:
    file = x['file'].replace(' ', '-') + '.swf'
    cursor.execute(statement, (x['title'], x['description'], file, x['image']))

print(connection.total_changes)
connection.commit()
connection.close()
