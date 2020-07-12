from Car import *
class Lane:
    width = 600
    height = 40
    def __init__(self, x, y, type, numOfVehicles, numOfLanes, vehicleSpeed, height):
        self.x = x
        self.y = y
        self.height = height
        self.cars = []
        self.numOfLanes = numOfLanes
        if type ==1: #lane of cars
            for i in range(numOfVehicles):
                if i%2 == 0:
                    if vehicleSpeed >= 0:
                        c = Car(x + i * 60, y + self.height/4, vehicleSpeed)
                    else:
                        c = Lorry(x + self.width - i * 70, y + self.height/4, vehicleSpeed)
                else:
                    if vehicleSpeed >= 0:
                        c = Car(x + i * 60, y + self.height/4, vehicleSpeed)
                    else:
                        c = Car(x + self.width - i * 60, y + self.height/4, vehicleSpeed)
                self.cars.append(c)
        if type ==2: #lane of lorrys
            for i in range(numOfVehicles):
                if i%2 == 0:
                    if vehicleSpeed >= 0:
                        c = Lorry(x + i * 70, y + self.height/4, vehicleSpeed)
                    else:
                        c = Lorry(x + self.width - i * 70, y + self.height/4, vehicleSpeed)
                else:
                    if vehicleSpeed >= 0:
                        c = Lorry(x + i * 70, y + self.height/4, vehicleSpeed)
                    else:
                        c = Lorry(x + self.width - i * 70, y + self.height/4, vehicleSpeed)
                self.cars.append(c)

    def moveCars(self):
        for c in self.cars:
            c.move()

    def draw(self, w):
        w.create_rectangle(self.x, self.y, self.width + 200, self.height + self.height * self.numOfLanes, fill = "gray")
        for c in self.cars:
            c.draw(w)
        #w.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="gray")
        #w.create_line(self.x + self.width+200, self.y, self.x, self.y, fill ="red")
