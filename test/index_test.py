import unittest2 as unittest
import sqlite3
connection = sqlite3.connect('sports.db')
cursor = connection.cursor()

class TestSqlLearnCompatability(unittest.TestCase):

    def test_leagues_table(self):
        leagues = cursor.execute("SELECT * FROM leagues;").fetchall()
        self.assertEqual(len(leagues), 2)
