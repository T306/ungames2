import sqlite3
import json

connection = sqlite3.connect("identifier.sqlite")
cursor = connection.cursor()
statement = "INSERT INTO Games VALUES (?, ?, ?, ?)"

with open('gaems.json') as gameFile:
    games = json.load(gameFile)
    gameFile.close()

print(games)
for x in games:
    file = x['file'].replace(' ', '-') + '.swf'
    cursor.execute(statement, (x['title'], x['description'], file, x['image']))

print(connection.total_changes)
connection.commit()
connection.close()
