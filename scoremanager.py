import sqlite3
from datetime import date

class ScoreManager(object):
    def __init__(self):
        # Create and/or connect to db
        self.conn = sqlite3.connect("high_scores.db")
        self.c = self.conn.cursor()

        # Create the table
        self.c.execute("CREATE TABLE IF NOT EXISTS HighScores(score INTEGER, initials TEXT)")

        self.high_score = 0
        self.posX = 0
        self.posY = 0
        self.first_place = None
        self.second_place = None
        self.third_place = None
        self.score_list = []


    # Submit score into db
    def register_score(self,score, initials):
        self.c.execute("INSERT INTO HighScores(score, initials) VALUES (?, ?)", (score, initials))
        self.conn.commit()



    def show_scores(self):
        score_out = []
        rank_out = self.c.execute("SELECT * FROM HighScores").fetchall()
        scoreList = self.c.execute("SELECT SCORE FROM HighScores").fetchall()
        for i in range(0, len(scoreList)):
            score_out.append(scoreList[i][0])

        score_out.sort(reverse=True)
        rank_out.sort(reverse=True)
        self.high_score = score_out[0]
        self.first_place = rank_out[0]
        self.second_place = rank_out[1]
        self.third_place = rank_out[2]
        self.score_list.append(f"1...{self.first_place[1]}...{self.first_place[0]}")
        self.score_list.append(f"2...{self.second_place[1]}...{self.second_place[0]}")
        self.score_list.append(f"3...{self.third_place[1]}...{self.third_place[0]}")

        

