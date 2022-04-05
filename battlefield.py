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

    # Bumblebee hits Stygimoloch with plasma cannon which has an attack power of 40pts.
    # Stygimoloch health decreases 40pts from 250pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch health decreases 40pts from 210pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch health decreases 40pts from 170pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch health decreases 40pts from 130pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch health decreases 40pts from 90pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch health decreases 40pts from 50pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch health decreases 40pts from 10pts

    # Bumblebee hits Stygimolch with plasma cannon which has an attack power of 40pts
    # Stygimoloch has lost the battle to Bumblebee

    #todo Stygimoloch attaks
    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee health decreases 35pts from 200pts

    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee health decreases 35pts from 165pts

    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee health decreases 35pts from 130pts

    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee health decreases 35pts from 95pts

    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee health decreases 35pts from 60pts

    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee health decreases 35pts from 25pts   

    # Stygimoloch hits Bumblebee with energy blast from his mouth which has an attack power of 35pts
    # Bumblebee has lost the battle to Stygimoloch 

      pass

  def display_winner(self):
    pass