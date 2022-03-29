class Dinosaur:

    def __init__(self, name, attack_power):
        self.name  = name
        self.health = 100
        self.energy = 200
        self.attack_power = 100
        self.attack_type = ['bite', 'claw', 'swipe']
        
    def attack_robot(self, dinosaur_to_attack):
        if self.energy >20:
            while True:
                attack_choice =  int(input(f'choose attack type: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}'))
                if attack_choice == 1:
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.attack_type[0]}')
                elif attack_choice == 2:
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.attack_type[1]}')
                elif attack_choice == 1:
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.attack_type[2]}')

            self.energy -= 20
            dinosaur_to_attack.health -= self.attack_power
            print(f'{self.name} energy is now {self.energy}') 
            print(f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')       
