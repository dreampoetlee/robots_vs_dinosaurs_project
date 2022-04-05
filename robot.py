# As a developer, I want to make a class for each of the following: #^Robot
from weapon import Weapon
class Robot:
  def __init__(self, name):
    # As a developer, I want a Robot to have a name, health, and active_weapon.
    self.name = name
    self.health = 200
    self.active_weapon = Weapon('plasma cannon', 40)
  
  def attack(self, dinosaur):
    # As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.

    #! While Loop: if dino's health !=0, hit dino with plasma cannon decreasing dino's health 40pts with each strike

    #todo if damage from robot's attack power is less than current dino's health, subtract robot's attack power from current dino's health

    #^ Need to display robot's attack power & dino's current health


    pass