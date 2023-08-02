import sqlite3

connection = sqlite3.connect("game.db")
cursor = connection.cursor()

games = cursor.execute("SELECT * FROM Games").fetchall()
print(games)
print(type(games))
