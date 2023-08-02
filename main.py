from quart import Quart, render_template, send_from_directory

try:
    import ujson as json
except ImportError:
    print('No U Json')
    import json

app = Quart(__name__)


@app.route('/')
async def home():
    with open('gaems.json') as gameFile:
        games = json.load(gameFile)
        gameFile.close()
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
