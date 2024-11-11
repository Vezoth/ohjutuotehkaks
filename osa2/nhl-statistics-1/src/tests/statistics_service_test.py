import unittest
from player import Player
from statistics_service import StatisticsService

players = [
            Player("Mika", "P", 10, 0),
            Player("Saara", "M", 13, 1),
            Player("Äiti", "foobar", 0, 16),
            Player("Isä", "foobar", 1, 15),
            Player("vauva vaara", "P", 0, 0)
        ]

sorted_players = sorted(
            players,
            reverse=True,
            key=lambda player: player.points
        )

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(StubReader("https://jyu.fi/"))

    def test_search(self):
        haettu = self.stats.search('Mika')
        self.assertEqual(haettu, players[0])

        haettu = self.stats.search('hattivatti')
        self.assertEqual(haettu, None)
    
    def test_team(self):
        haettu = self.stats.team('foobar')
        self.assertEqual(haettu, [players[2], players[3]])
        haettu = self.stats.team('P')
        self.assertEqual(haettu, [players[0], players[4]])
        haettu = self.stats.team('M')
        self.assertEqual(haettu, [players[1]])
        haettu = self.stats.team('hattivatti')
        self.assertEqual(haettu, list())
    
    def test_top(self):
        haettu = self.stats.top(-1)
        self.assertEqual(haettu, list())

        haettu = self.stats.top(0)
        self.assertEqual(haettu, [sorted_players[0]])

        for i in range(0, len(sorted_players)-1):
            haettu = self.stats.top(i)
            self.assertEqual(haettu, sorted_players[:(i+1)])


class StubReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        return players
