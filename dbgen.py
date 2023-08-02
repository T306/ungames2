import sqlite3
import json
import base64

connection = sqlite3.connect("game.db")
cursor = connection.cursor()
statement = "INSERT INTO Games VALUES (?, ?, ?, ?)"

with open('gaems.json') as gameFile:
    games = json.load(gameFile)
    gameFile.close()

print(games)
for x in games:
    if str(x['image']):
        image = str("static/images/" + x['image'])
        image = open(image, 'rb').read()
        image = base64.b64encode(image)
    else:
        image = " "
    file = x['file'].replace(' ', '-') + '.swf'
    cursor.execute(statement, (x['title'], x['description'], file, image))

print(connection.total_changes)
connection.commit()
connection.close()
