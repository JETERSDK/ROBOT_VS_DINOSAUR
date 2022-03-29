from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = ("Lizard", 5)
        dino2 = ("T_Rex", 15)
        dino3 = ("Rino", 10)
        
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
        