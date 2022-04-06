# As a developer, I want to make a class for each of the following: #^Dinosaur
class Dinosaur:
  def __init__(self, name, attack_power):
    self.name = name
    self.attack_power = attack_power
    self.health = 100
  
  def attack(self, robot):
    # As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.
    robot.health -= self.attack_power
    #^ Need to display dino's attack power & robot's current health maybe in a variable?
    print(f"{self.name} attacks {robot.name} with energy blast from his mouth for {self.attack_power} damage. {robot.name}'s current health is {robot.health}")