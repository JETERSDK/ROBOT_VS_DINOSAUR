from Weapon import Weapon
class Robot:

    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.energy = 200
        self.weapon = Weapon
        self.weapon_type = ['gun', 'missle', 'fist'] 

    def attack_dinosaur(self, robot_to_attack):
        if self.energy >20:
            while True:
                attack_choice =  int(input(f'choose attack type: (1) {self.weapon_type[0]}, (2) {self.weapon_type[1]}'))
                if attack_choice == 1:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.weapon_type[0]}')
                elif attack_choice == 2:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.weapon_type[1]}')
                elif attack_choice == 1:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.weapon_type[2]}')

            self.energy -= 20
            robot_to_attack.health -= self.attack_power
            print(f'{self.name} energy is now {self.energy}') 
            print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')  
