from tkinter import *
from random import randint
import tkinter


class Game:
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[14, 14]]
        self.apple_coords = [randint(0, 29) for i in range(2)]
        self.vector = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.score = 0
        self.score_label = tkinter.Label(root, text="Счет: 0", font=("Arial", 12))
        self.score_label.pack()
        self.GAME()
        self.pause_button = tkinter.Button(root, text="Pause", command=self.pause_game)
        self.restart_button = tkinter.Button(root, text="Restart", command=self.restart_game)
        self.exit_button = tkinter.Button(root, text="Exit", command=root.quit)

        self.pause_button.pack(side=tkinter.LEFT, padx=10)
        self.restart_button.pack(side=tkinter.LEFT, padx=10)
        self.exit_button.pack(side=tkinter.LEFT, padx=10)

        self.GAME()

    def game_over(self):
        self.canvas.delete(ALL)
        game_over_label = tkinter.Label(root, text="Game Over", font=("Expressway free", 12))
        game_over_label.pack()

    def add_score(self):
        self.score += 1
        self.score_label.config(text="Счет: {}".format(self.score))

    def set_apple(self):
        self.apple_coords = [randint(0, 29) for i in range(2)]
        if self.apple_coords in self.snake_coords:
            self.set_apple()

    def set_direction(self, event):
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]

    def draw(self):
        self.canvas.delete(ALL)
        x_apple, y_apple = self.apple_coords
        self.canvas.create_rectangle(x_apple * 10, y_apple * 10, (x_apple + 1) * 10, (y_apple + 1) * 10, fill="red",
                                     width=0)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="green", width=0)

    @staticmethod
    def coord_check(coord):
        return 0 if coord > 29 else 29 if coord < 0 else coord

    def GAME(self):
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0]
        y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)

        if [x, y] in self.snake_coords:
            self.game_over()
            return

        # Keep the tail segment when snake eats an apple
        if x == self.apple_coords[0] and y == self.apple_coords[1]:
            self.add_score()
            self.set_apple()
        else:
            self.snake_coords.pop()

        self.snake_coords.insert(0, [x, y])

        self.canvas.after(200, self.GAME)

    def pause_game(self):
        pass

    def restart_game(self):
        pass


root = tkinter.Tk()
root.title("Snake Game")

canvas = tkinter.Canvas(root, width=300, height=300)
canvas.pack()

background_image = tkinter.PhotoImage(file="b9af9220dd85f069b1c61dd5d72bdfd1.png")
canvas.create_image(0, 0, anchor=tkinter.NW, image=background_image)

game = Game(canvas)


root.mainloop()