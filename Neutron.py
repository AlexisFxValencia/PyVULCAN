import numpy as np

class Neutron:
    def __init__(self, myCanvas, vx, vy):
        self.position = np.array([30.0, 30.0])
        self.velocity = np.array([vx, vy]) #points/sec
        self.limits = np.array([300, 300])
        self.radius = 10.0
        self.scale = 5
        self.circle = myCanvas.create_oval(int(self.position[0] - self.radius), int(self.position[1] - self.radius),
                                           int(self.position[0] + self.radius), int(self.position[1] + self.radius),
                                           fill = "orange")

    def check_if_rebound(self):
        if self.position[0] > self.limits[0] - self.radius:
            self.velocity[0] = - abs(self.velocity[0])
        if self.position[0] < self.radius:
            self.velocity[0] = abs(self.velocity[0])
        if self.position[1] > self.limits[1] - self.radius:
            self.velocity[1] = - abs(self.velocity[1])
        if self.position[1] < self.radius:
            self.velocity[1] = abs(self.velocity[1])

    def take_a_step(self, myCanvas, dt):
        self.position += self.velocity * dt / 1000
        myCanvas.move(self.circle, self.velocity[0] * dt/1000, self.velocity[1] * dt/1000)

