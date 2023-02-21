import numpy as np
from random import randrange, uniform
from math import pi, cos, sin

class Neutrons:
    def __init__(self, width_window = 800, height_window = 600, nb_neutrons = 50, radius = 10.0, neutrons_speed = 20):
        self.position_limits = (width_window, height_window)
        self.radius = radius
        self.scale = 5
        self.nb_neutrons = nb_neutrons
        self.speed = neutrons_speed

        #self.positions = np.array([[30.0, 60.0, 90.0], [30.0, 60.0, 90.0]])
        self.positions = np.zeros((2, self.nb_neutrons))
        self.set_random_positions()

        #self.velocities = np.array([[vx, vx, -vx], [vy, -vy, vy]])  # points/sec
        self.velocities = np.zeros((2, self.nb_neutrons))
        self.set_random_velocities()

        self.disks = [None] * self.nb_neutrons

    def set_random_positions(self):
        for i in range(self.nb_neutrons):
            self.positions[0][i] = randrange(self.position_limits[0])
            self.positions[1][i] = randrange(self.position_limits[1])

    def set_random_velocities(self):
        for i in range(self.nb_neutrons):
            theta = uniform(0, 2*pi)
            self.velocities[0][i] = self.speed * cos(theta)
            self.velocities[1][i] = self.speed * sin(theta)

    def init_disks(self, myCanvas):
        for i in range(self.nb_neutrons):
            self.disks[i] = myCanvas.create_oval(int(self.positions[0][i] - self.radius), int(self.positions[1][i] - self.radius),
                                                 int(self.positions[0][i] + self.radius), int(self.positions[1][i] + self.radius),
                                                 fill = "orange")


    def check_if_rebound(self):
        for i in range(self.nb_neutrons):
            if self.positions[0][i] > self.position_limits[0] - self.radius:
                self.velocities[0][i] = - abs(self.velocities[0][i])
            if self.positions[0][i] < self.radius:
                self.velocities[0][i] = abs(self.velocities[0][i])
            if self.positions[1][i] > self.position_limits[1] - self.radius:
                self.velocities[1][i] = - abs(self.velocities[1][i])
            if self.positions[1][i] < self.radius:
                self.velocities[1][i] = abs(self.velocities[1][i])

    def take_a_step(self, dt):
        #self.positions += self.velocities * dt / 1000
        np.add(self.positions, self.velocities * dt / 1000, out=self.positions)

    def update_circles(self, myCanvas, dt):
        for i in range(self.nb_neutrons):
            myCanvas.move(self.disks[i], self.velocities[0][i] * dt / 1000, self.velocities[1][i] * dt / 1000)

