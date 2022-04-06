# As a developer, I want to make a class for each of the following: #^ Battlefield.
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
  def __init__(self):
    self.robot = Robot('Bumblebee')
    self.dinosaur = Dinosaur('Stygimolach', 25)
  
  def run_game(self):
    # Welcome section
    # Print welcome message
    # Print fighters name
    self.display_welcome()

    # Fight sequence
    self.battle_phase()
    # Bumblebee attacks
    # Stygimoloch attacks

    # Battle ending
    self.display_winner()

  def display_welcome(self):
    print(f'Welcome to the ultimate smack down between {self.robot.name} & {self.dinosaur.name}')
    
  def battle_phase(self):
    # if self.robot.health >= 0 :
    #   self.robot.attack(self.dinosaur)
    # else:
    #   self.dinosaur.attack(self.robot)
    
    while self.robot.health >= 0 and self.dinosaur.health >= 0 :
      self.robot.attack(self.dinosaur)
      self.dinosaur.attack(self.robot)

  def display_winner(self):
    if self.robot.health == 0 :
      print(f'{self.dinosaur.name} is the Winner of the Match!!')
    else:
      print(f'{self.robot.name} is the Winner of the Match!!')
    pass



   #! While Loop: if robot's health != 0, hit robot with energy blast decreasing robot's health 35 pts with each strike
    # while robot.health > 0 :
    #   print(f'{self.name} hit {robot.name} with energy blast from his mouth which has an attack power of {self.attack_power} points.')

      #todo if damage from dino's attack power is less than current robot health, subtract dino attack power from current robot health

      #! While Loop: if dino's health !=0, hit dino with plasma cannon decreasing dino's health 40pts with each strike

    #todo if damage from robot's attack power is less than current dino's health, subtract robot's attack power from current dino's health

        #! While Loop: if dino's health !=0, hit dino with plasma cannon decreasing dino's health 40pts with each strike

    #todo if damage from robot's attack power is less than current dino's health, subtract robot's attack power from current dino's health