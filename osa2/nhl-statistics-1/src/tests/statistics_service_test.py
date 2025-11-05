import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.points, 16)
        player = self.stats.search("Lemieux")
        self.assertEqual(player.points, 99)
        player = self.stats.search("Kurri")
        self.assertEqual(player.points, 90)
        player = self.stats.search("Yzerman")
        self.assertEqual(player.points, 98)
        player = self.stats.search("Gretzky")
        self.assertEqual(player.points, 124)

    def test_search_fail(self):
        player = self.stats.search("Olematonpelaaja")
        self.assertEqual(player, None)

    def test_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(str(team[0]), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(str(team[1]), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(str(team[2]), "Gretzky EDM 35 + 89 = 124")

    def test_top_one(self):
        best = self.stats.top(1)
        self.assertEqual(best[0].points, 124)

    def test_top_enemman_kuin_pelaajia_on(self):
        with self.assertRaises(IndexError):
            self.stats.top(20)
