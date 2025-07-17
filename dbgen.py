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
    statement = "INSERT INTO Games VALUES (?, ?, ?, ?, ?)"

    if recreate:
        cursor.execute("drop table if exists Games")
        cursor.execute("create table Games (title TEXT, description TEXT, type TEXT, file TEXT, image TEXT)")

    for game in natsorted(os.listdir("Games")):
        game_name = title_gen(game)
        game_file = "/Games/" + game
        if ".swf" in game:
            game_img = game.replace(".swf", ".webp")
            game_type = "flash"
        elif ".html" in game:
            game_img = game.replace(".html", ".webp")
            game_type = "html"
        else:
            continue
        cursor.execute(statement, (game_name, game_name, game_type, game_file, game_img))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    db_gen(recreate=True)
