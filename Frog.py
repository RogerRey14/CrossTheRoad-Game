from tkinter import *
import time
import keyboard

class Frog:
    width = 20
    height = 20
    step = 40
    score = 100
    alive = True
    def __init__(self, x, y, wx1, wy1, wx2, wy2,speed ):
        self.x = x
        self.y = y
        self.speed = speed
        self.window_x1 = wx1
        self.window_y1 = wy1
        self.window_x2 = wx2
        self.window_y2 = y + self.height
        self.start = time.time()
        self.end = 0



    def draw(self, w):
        w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = "green")

    def move(self):
        if keyboard.is_pressed("up arrow"):
            self.y -= self.speed
            if self.y < self.window_y1:
                self.y = self.window_y1
        if keyboard.is_pressed("down arrow"):
            self.y += self.speed
            if self.y > self.window_y2 - self.height:
                self.y = self.window_y2 - self.height
        if keyboard.is_pressed("left arrow"):
            self.x -= self.speed
            if self.x < self.window_x1:
                self.x = self.window_x1
        if keyboard.is_pressed("right arrow"):
            self.x += self.speed
            if self.x > self.window_x2 - self.width:
                self.x = self.window_x2 - self.width

    def finishReached(self):
        if self.y <= self.window_y1:
            print("Congratulations you win the game! 0 reached by the frog")
            if self.score == 100:
                self.end = self.score - (time.time() - self.start)
                print(self.end)
            return True

    def collision(self, c):
        if c.y != self.y:
            return False
        if (self.x>=c.x and self.x <= c.x + c.width) or (self.x + self.width >= c.x and self.x+self.width <= c.x + c.width):
            return True
        return False

    def notAlive(self):
        self.alive = False

