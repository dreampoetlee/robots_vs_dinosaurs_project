# As a developer, I want to make a class for each of the following: #^Robot
from weapon import Weapon
class Robot:
  def __init__(self, name):
    # As a developer, I want a Robot to have a name, health, and active_weapon.
    self.name = name
    self.health = 200
    self.active_weapon = Weapon('plasma cannon', 40)
  
  def attack(self, dinosaur):
    pass