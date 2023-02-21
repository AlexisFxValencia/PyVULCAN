import tkinter as tk
from Neutrons import *

width = 800
height = 600
global dt
dt = int(1000/100)  # in msec
vx = 20.0 #in points/sec
vy = 50.0 #in points/sec
radius = 5.0
nb_neutrons = 80
neutrons_speed = 50.0
neutrons = Neutrons()

def update():
    if not on_pause.get():
        neutrons.check_if_rebound()
        neutrons.take_a_step(dt)
        neutrons.update_circles(myCanvas, dt)
    myCanvas.after(dt, update)

def click():
    print("clic")
    if on_pause.get():
        on_pause.set('false')
        print("mybv1 : " + str(on_pause.get()))
    else:
        on_pause.set('true')
        print("mybv1 : " + str(on_pause.get()))

if __name__ == '__main__':
    window = tk.Tk()
    on_pause = tk.BooleanVar(window)  # declare Boolean Variable
    on_pause.set('false')

    pause_button = tk.Button(window, text="Pause", command=click)
    pause_button.pack(side="right")

    myCanvas = tk.Canvas(window, bg="white", width=width, height=height)
    myCanvas.pack()

    neutrons = Neutrons(width_window=width, height_window=height,
                        nb_neutrons=nb_neutrons, radius=radius, neutrons_speed=neutrons_speed)
    neutrons.init_disks(myCanvas)
    update()
    window.mainloop()
