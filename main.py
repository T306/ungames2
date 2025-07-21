from quart import Quart, render_template, send_from_directory
import sqlite3
import tomllib
import uvicorn
import os
import dbgen

app = Quart(__name__)
app.config.from_file("config.toml", load=tomllib.load, text=False)
connection = sqlite3.connect("identifier.sqlite")


async def check_db():
    """Checks for db existence"""
    app.logger.info("Checking for DB")
    if not dbgen.is_db() or os.getenv("RECREATE_TABLE"):
        app.logger.info("Recreating DB")
        dbgen.db_gen(recreate=True)
        app.logger.info("DB Generation complete")
    else:
        app.logger.info("DB exists... Skipping Generation")


@app.before_serving
async def startup():
    await check_db()


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
