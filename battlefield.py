# As a developer, I want to make a class for each of the following: #^ Battlefield.
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
  def __init__(self):
    self.robot = Robot('Bumblebee')
    self.dinosaur = Dinosaur('Stygimolach', 25)
  
  def run_game(self):
    self.display_welcome()
    self.battle_phase()
    self.display_winner()

  def display_welcome(self):
    print(f'Welcome to the ultimate smack down between {self.robot.name} & {self.dinosaur.name}')
    
  def battle_phase(self):
    while self.robot.health >= 0 and self.dinosaur.health >= 0 :
      self.robot.attack(self.dinosaur)
      self.dinosaur.attack(self.robot)
  # As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.
  def display_winner(self):
    if self.robot.health == 0 :
      print(f'{self.dinosaur.name} is the Winner of the Match!!')
    else:
      print(f'{self.robot.name} is the Winner of the Match!!')
    pass