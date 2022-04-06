# As a developer, I want to make a class for each of the following: #^Robot
from weapon import Weapon
class Robot:
  def __init__(self, name):
    # As a developer, I want a Robot to have a name, health, and active_weapon.
    self.name = name
    self.health = 100
    self.active_weapon = Weapon('plasma cannon', 20)
  
  def attack(self, dinosaur):
    # As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.
    dinosaur.health -= self.active_weapon.attack_power
    #^ Need to display robot's attack power & dino's current health
    print(f"{self.name} attacks {dinosaur.name} with his {self.active_weapon.name} for {self.active_weapon.attack_power} damage points. {dinosaur.name}'s current health is {dinosaur.health}")