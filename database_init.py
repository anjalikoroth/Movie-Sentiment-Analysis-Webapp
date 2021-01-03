import sqlite3

connection = sqlite3.connect('database.db',check_same_thread=False)
# with open('schema.sql') as f:
#     connection.executescript(f.read())
cur = connection.cursor()
connection.row_factory = sqlite3.Row
cur.execute("CREATE TABLE IF NOT EXISTS movieReview(Review text,Prediction text, Userfeedback text);")
# cur.execute("INSERT INTO movieReview (Review, Prediction) VALUES ('Great movie', 'Positive');")
# print(cur.execute('SELECT * from movieReview').fetchall())

def get_connection():

    return (connection, cur)

def close_connection():
    connection.close()

