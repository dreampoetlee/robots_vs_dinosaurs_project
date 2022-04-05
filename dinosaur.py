# As a developer, I want to make a class for each of the following: #^Dinosaur
from robot import Robot

class Dinosaur:
  def __init__(self, name, attack_power ):
    self.name = name
    self.attack_power = attack_power
    self.health = 250
  
  def attack(self, robot):
  # As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.


  #! While Loop: if robot's health != 0, hit robot with energy blast decreasing robot's health 35 pts with each strike
    while robot.health > 0 :
      print(f'{self.name} hit {robot.name} with energy blast from his mouth which has an attack power of {self.attack_power} points.')

      #todo if damage from dino's attack power is less than current robot health, subtract dino attack power from current robot health

      #^ Need to display dino's attack power & robot's current health maybe in a variable?

    pass