import os
import sqlite3
from natsort import natsorted


def title_gen(f):
    replacements = {"Games\\":  "", ".swf": "", "-": " "}
    for old, new in replacements.items():
        f = f.replace(old, new)
    return f.title()


def db_gen(recreate=False):
    connection = sqlite3.connect("identifier.sqlite")
    cursor = connection.cursor()
    statement = "INSERT INTO Games VALUES (?, ?, ?, ?)"

    if recreate:
        cursor.execute("drop table if exists Games")
        cursor.execute("create table Games (title TEXT, description TEXT, file TEXT, image TEXT)")

    for game in os.listdir("Games"):
        game_name = title_gen(game)
        game_img = game.replace(".swf", ".webp")
        game_file = "/Games/" + game
        # game_list.append(dict(title=game_name, description=game_name, image=game_img, file=game_file))
        cursor.execute(statement, (game_name, game_name, game_file, game_img))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    db_gen(recreate=True)
