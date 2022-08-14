from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Velociraptor")
        self.robot = Robot("Humanoid")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Get ready for the death match! Who will be victorious?")
        

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health >0:
            self.dinosaur.attack(self.robot)
            if self.robot.health >0:
                self.robot.attack(self.dinosaur)
      
       
            
              
    
    def display_winner(self):
        if self.robot.healt <= 0:
            print(f'{self.dinosaur.name} has claimed the victory!') 
        elif self.dinosaur.health <= 0:
                print(f'{self.robot.name} has claimed the victory!')


   
