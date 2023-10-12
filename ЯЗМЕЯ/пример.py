from tkinter import *
from random import randint

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
        self.score_display = self.canvas.create_text(10, 10, anchor=NW, fill="white", font=("Arial", 12), text="Score: 0")
        self.GAME()

    def set_apple(self):
        self.apple_coords = [randint(0, 29) for i in range(2)]
        if self.apple_coords in self.snake_coords:
            self.set_apple()

    def set_direction(self, event):
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]

    def coord_check(self, coord):
        return 0 if coord > 29 else 29 if coord < 0 else coord

    def draw(self):
        self.canvas.delete(ALL)
        x_apple, y_apple = self.apple_coords
        self.canvas.create_rectangle(x_apple * 10, y_apple * 10, (x_apple + 1) * 10, (y_apple + 1) * 10, fill="red", width=0)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x * 10, y * 10, (x + 1) * 10, (y + 1) * 10, fill="orange", width=0)

    def GAME(self):
        self.change_background_color()
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0]
        y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.apple_coords[0] and y == self.apple_coords[1]:
            self.set_apple()
            self.score += 10
            self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x, y])
        self.canvas.after(100, self.GAME)

        def change_background_color(self):
            color = self.colors[self.color_index]
            self.color_index = (self.color_index + 1) % len(self.colors)
            self.canvas.configure(bg=color)



root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

game = Game(canvas)

root.mainloop()

