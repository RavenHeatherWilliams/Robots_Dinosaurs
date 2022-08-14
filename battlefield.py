from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Velociraptor")
        self.robot = Robot("Humanoid")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        # self.display_winner()

    def display_welcome(self):
        # user_confirmed =(False)
        # while user_confirmed == (False):
        #   user_input = input()   
        print("Get ready for the death match! Who will be victorious?")
        

    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        self.robot.attack(self.dinosaur)
      
       
            
              
    # def battle_phase(self):
    #     self.dinosaur.attack(self.robot)
    #     self.robot.attack(self.dinosaur)
    #     battle_phase = False
    #     while battle_phase == (False):
    #         if self.dinosaur == "10":
    #              print(f'{self.dinosaur} was attacked by {self.name} and did {self.attack_power} damaged leaving  the dinosaur with {self.health} health')
    #              return battle_phase
    #         elif self.dinosaur == "0":
    #             print(f'You have claimed the victory!')

    def display_winner():
        battle_phase = False
        if Robot == "0":
            print(f'You have claimed the victory!') 
        elif Dinosaur == "0":
                print(f'You have claimed the victory!')

    result = display_winner()
    print(display_winner)
