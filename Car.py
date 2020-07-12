from tkinter import *
import time
import keyboard

class Vehicle:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x += self.speed
        self.restartCars()

    def restartCars(self):
        if self.speed >= 0:
            if self.x >= 800:
                self.x = 0
        else:
            if self.x <= 0:
                self.x = 800

class Car(Vehicle):
    width = 30
    height = 20
    color1 = "red"
    color2 = "yellow"
    def __init__(self,x, y, speed=5):
        super().__init__(x, y, speed)

    def draw(self, w):
        if self.speed >= 0:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color1)
            w.create_line(self.x + self.width * 0.75, self.y, self.x + self.width * 0.75, self.y + self.height)
        else:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill =self.color2)
            w.create_line(self.x + self.width * 0.25, self.y, self.x + self.width * 0.25, self.y + self.height)


class Lorry(Vehicle):
    width = 60
    height = 20
    color1 = "purple"
    color2 = "cyan"
    def __init__(self,x, y, speed=5):
        super().__init__(x, y, speed)

    def draw(self, w):
        if self.speed >= 0:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = self.color1)
            w.create_line(self.x + self.width * 0.80, self.y, self.x + self.width * 0.80, self.y + self.height)
        else:
            w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = self.color2)
            w.create_line(self.x + self.width * 0.20, self.y, self.x + self.width * 0.20, self.y + self.height)


