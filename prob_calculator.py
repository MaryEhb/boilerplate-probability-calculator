import copy
import random

# Consider using the modules imported above.
class Hat:
  contents = []

  def __init__(self,**data):
    self.data = data
    self.contents = []
    for key,value in data.items():
      for i in range(0,value):
        self.contents.append(str(key))
      
  def draw(self,num):
    
    if num > len(self.contents):
      return self.contents

    # Use random.sample to select elements without modifying the list
    drawn_balls = random.sample(self.contents, num)  

    # Remove the selected balls from the contents
    for ball in drawn_balls:
        self.contents.remove(ball)  

    return drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successful_experiments  = 0

  for i in range(0,num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    success = True

    for key,value in expected_balls.items():
      if drawn_balls.count(key) < value:
        success = False
        break
    
    if success: 
      num_successful_experiments  += 1 
    
  # Calculate the probability based on the formula
  probability = num_successful_experiments / num_experiments

  return probability
