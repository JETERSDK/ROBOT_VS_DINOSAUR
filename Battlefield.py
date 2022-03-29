from Herd import Herd 
from Fleet import Fleet
import random

class Battlefield:
    def __init__(self):
      self.herd = Herd()
      self.fleet = Fleet()
      
      

    def run_game(self):
        self.display_welcome
        self.battle
        

    def display_welcome(self):
        print("Welcome to the fight between Robots vs Dinosaurs!")
        

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass