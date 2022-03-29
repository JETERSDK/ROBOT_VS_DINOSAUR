from Robot import Robot
from Weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        weapon1 = Weapon("Gun", 10)
        weapon2 = Weapon("Missle", 20)
        weapon3 = Weapon("Fist", 5)

        robot1 = Robot("Maximize", weapon1)
        robot2 = Robot("Eraser", weapon2)
        robot3 = Robot("Blitz", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
      