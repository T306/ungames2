from quart import Quart, render_template, send_from_directory
import sqlite3
import tomllib
import uvicorn
import os
import dbgen

app = Quart(__name__)

app.config.from_file("config.toml", load=tomllib.load, text=False)

# Recreate db if not present
is_db = os.path.exists("identifier.sqlite")
dbgen.db_gen(recreate=is_db)


connection = sqlite3.connect("identifier.sqlite")


@app.route('/')
async def home():
    games = []
    with connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Games")
        rows = cursor.fetchall()
        for row in rows:
            game = {'title': row['title'], 'description': row['description'], 'file': row['file'],
                    'image': row['image']}
            games.append(game)
    return await render_template("pages/home.html", title='Home', len=len(games), games=games)


@app.route('/game/<string:game>')
async def play(game):
    title = game.replace('-', ' ')
    game = str(str(game).lower() + '.swf')
    return await render_template('pages/player.html', game=game, title=title)


@app.route("/Games/<string:game>")
async def game_srv(game):
    return await send_from_directory('Games', game)


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
