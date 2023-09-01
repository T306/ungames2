from quart import Quart, render_template, send_from_directory
import sqlite3
import os

app = Quart(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'  # os.environ['SECRET_KEY']

connection = sqlite3.connect("identifier.sqlite")
cursor = connection.cursor()
games = []


@app.route('/')
async def home():
    with connection:
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()
        cur.execute("SELECT * FROM Games")
        rows = cur.fetchall()
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


app.run(host='0.0.0.0', port=81)
