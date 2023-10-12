import unittest
from tkinter import Tk, Canvas
from ЗМЕЯ import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.game = Game(self.canvas)

    def tearDown(self):
        self.root.destroy()

    def test_initial_score(self):
        self.assertEqual(self.game.score, 0)

    def test_initial_snake_length(self):
        self.assertEqual(len(self.game.snake_coords), 1)

    def test_set_direction(self):
        self.game.set_direction("<Up>")
        self.assertEqual(self.game.direction, (0, -1))

    def test_coord_check(self):
        self.assertEqual(Game.coord_check(-1), 0)
        self.assertEqual(Game.coord_check(30), 29)
        self.assertEqual(Game.coord_check(15), 15)

    def test_set_apple(self):
        self.game.set_apple()
        self.assertNotEqual(self.game.apple_coords, None)

if __name__ == '__main__':
    unittest.main()
