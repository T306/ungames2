import os
import sqlite3
from natsort import natsorted


def title_gen(f):
    name = f.replace('Games\\', '')
    name = name.replace('.swf', '')
    name = name.replace('-', ' ')
    return name.title()


def main():
    game_list = []
    game2dict = []

    connection = sqlite3.connect("identifier.sqlite")
    cursor = connection.cursor()
    statement = "INSERT INTO Games VALUES (?, ?, ?, ?)"

    cursor.execute("drop table if exists Games")
    cursor.execute("create table Games (title TEXT, description TEXT, file TEXT, image TEXT)")

    # Implement natsort
    for game in os.listdir('Games'):
        game = game.replace('.swf', '').replace('-', ' ')
        game_list.append(game)

    game_list = natsorted(game_list)

    for game in game_list:
        index = game_list.index(game)
        game = game.replace(' ', '-') + '.swf'
        game_list[index] = game

    # Converts games to dict
    for game in game_list:
        game_name = title_gen(game)
        # game_desc = game_name
        game_img = game.replace(' ', '-').replace('.swf', '') + '.webp'
        game_file = '/Games/' + game
        game = dict(title=game_name, description=game_name, image=game_img, file=game_file)
        game2dict.append(game)

    del game_list

    for x in game2dict:
        file = x['file'].replace(' ', '-') + '.swf'
        cursor.execute(statement, (x['title'], x['description'], x['image'], file))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    print("Generating Games Database ")
    main()
    print("Games Database Generated!!")
