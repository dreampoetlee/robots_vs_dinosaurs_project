# As a developer, I want to make a class for each of the following: #^ Battlefield.
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
  def __init__(self):
    self.robot = Robot
    self.dinosaur = Dinosaur
  
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
    pass

  def display_welcome(self):
    print(f'Welcome to the ultimate smack down between Bumblebee & Stygimoloch')
    pass

  def battle_phase(self):
    #todo Bumblebee attacks

    

    #todo Stygimoloch attaks
    

      pass

  def display_winner(self):
    pass