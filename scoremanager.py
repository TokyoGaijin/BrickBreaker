import sqlite3
from datetime import date

class ScoreManager(object):
    def __init__(self):
        # Create and/or connect to db
        self.conn = sqlite3.connect("high_score_registry.db")
        self.c = self.conn.cursor()

        # Create the table
        self.c.execute("CREATE TABLE IF NOT EXISTS HighScores(score INTEGER)")

        self.high_score = 0
        self.posX = 0
        self.posY = 0
       

    # Submit score into db
    def register_score(self,score):
        self.c.execute("INSERT INTO HighScores(score) VALUES (?)", (score,))
        self.conn.commit()


    def show_scores(self):
        try:
            # if registries exist
            score_out = self.c.execute("SELECT * FROM HighScores").fetchall()
            score_out.sort(reverse=True)
            self.high_score = score_out[0][0]
        except:
            # if registries don't exist
            self.high_score = 0

        