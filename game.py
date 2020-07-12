"""
He de dir que he programat mai interficies gràfiques en jocs que no siguin per Android,
pot ser estic una mica equivocat amb la idea del diagrama de classes, que per cert es una idea genèrica.

Class Element. Aquesta classe conté les característiques comúnns entre elements com pot ser x, y, widht height i
    objectes d altres classes com movement o altres característiques necesaries per a cada element.
Class Frogg extended Element: Moviment propi, disseny etc...
Class Car extended Element: Aquesta classe hereda tots els atributs i mètodes de la classe ELement.
    Esta més enfocada per a les característiques que no comparteix amb la classe Frogg, com pot  ser el seu tipus de moviment o disseny.
Class NormalCar extended Car: Disseny diferent i dimensions.
Class Truck extended Car: Disseny diferent a NormalCar i dimensions més grans (per variar una mica amb els elements del joc).

Class Movement: Conté els metodes amb els moviments dels diferents elements, es relacionara amb class Frogg i Car.
Class KeyBoard: Llegira les accions introduides per l'usuari
Class Screen: Printará i dissenyara la screen on hi hauran els elements.
Class Game: Inicialitzarà la partida, comprovara si es guanya, detectara col·lisions entre elements, etc
Class Main: run.game().
Class Styles: Guardará alguns parametres, colors, imatges i més atributs per el disseny d'elements o screen.

DONE - apply movement of the frog in all the directrions, left ,right, up, down
DONE - instead of changing y directly in the main loop, call a move function in the frog
DONE - detect when the frog reaches the top of the screen (y=0). Run a print just to show that your program detected it
DONE - move class Lane to another file
DONE  - implement the draw function of lane: draw the existing cars and draw the decoration you prefer
DONE  - int he main loop draw all the lanes instead of all the cars of only the 1st lane
DONE  - detect when a car goes outside a lane, put it at the starting position of the lane
DONE - implement a score for the game. The score = 100 - seconds(decimals) to needed to reach the 2nd side of the road (ms)
DONE - show the score at the top of the window (display a string)
DONE - find by yourself a function to get if 2 objects collided. collision()


 - implementa uno de los dos:
    - problem with keys: too fast -> leave 0.2s -> game.y
    - Pause when pressing "p" alternate between pause/no pause -> game.y
 - save scores and records in a file, and read the file when the game starts placing all the scores into a list.
    - function open , etc. to save/read the scores/records. -> read/write from a list of scores
    - optional: to have the records sorted, lists in python have a function named "sort" to sort a list
    - optional: save the records with an associated name. The content of the file may be:
        Jhon,33
        Doe,44
        ...
        Dictionary
 """

from Frog import *
from Lane import *
from Car import *
from tkinter import *
import time
import keyboard


tk = Tk()
WIDTH = 800
HEIGHT = 400
w = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Frogger Game (by Roger Rey)")
w.pack()

LANE_HEIGHT=40
TOP_WINDOW_SPACE=40
speeds=[7,-5,10,-9,3]
lanes=[None]*5

for i in range(len(lanes)):
    if i == 4: #lorrys
        lanes[i] = Lane(0, TOP_WINDOW_SPACE + LANE_HEIGHT * i, 2, 6, len(lanes), speeds[i], LANE_HEIGHT)
    else: #cars
        lanes[i] = Lane(0, TOP_WINDOW_SPACE + LANE_HEIGHT*i, 1, 4, len(lanes),speeds[i], LANE_HEIGHT)

frog = Frog(WIDTH/2, lanes[-1].y+LANE_HEIGHT+LANE_HEIGHT/4, 0, 0, WIDTH, HEIGHT,LANE_HEIGHT)

while not frog.finishReached() and frog.alive:

    for lane in lanes:
        lane.moveCars()

    #move the frog
    frog.move()

    #frog cross the road y = 0
    #frog.finishReached(w)

    #drawScreen
    w.delete("all")
    w.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")

    #Draw lanes and the cars of every lane
    for lane in lanes:
        lane.draw(w)
    frog.draw(w)
    w.update()

    for lane in lanes:
        for c in lane.cars:
            if frog.collision(c):
                frog.notAlive()


    time.sleep(50/1000)

w.delete("all")
w.create_rectangle(0, 0, WIDTH, HEIGHT, fill="white")
score = "Score: " + str(frog.end)
w.create_text(150,20, text=score, fill = "blue", font = "Roboto 15 italic")
if (frog.alive):
    w.create_text(600, 20, text="Congratulations, you win the game!", fill="Red", font="Roboto 15 italic")
else:
    w.create_text(600, 20, text="You lose!", fill="Red", font="Roboto 15 italic")
for lane in lanes:
    lane.draw(w)
frog.draw(w)
w.update()
time.sleep(5)
