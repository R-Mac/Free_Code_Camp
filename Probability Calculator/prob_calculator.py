import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**balls):
    self.contents=[]
    for ball_type,ball_num in balls.items():
      for num in range(ball_num):
        self.contents.append(ball_type)


  def draw(self,draw_num:int) -> list:
    #random.shuffle(self.contents)
    drawn_balls = []
    if draw_num > len(self.contents):
      drawn_balls = self.contents
      self.contents = []
    else:
      for draw in range(draw_num):
        #For some reason, scrambling the list and popping the end of the list is not random enough and requires the generation of a random number to pop from instead.
        drawn_balls.append(self.contents.pop(random.randrange(len(self.contents))))
        #drawn_balls.append(self.contents.pop())
    return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> int:
  success_rate = 0
  for experiment_num in range(num_experiments):
    draw_count = {}
    experiment_hat = copy.deepcopy(hat)
    draw_result = experiment_hat.draw(num_balls_drawn)
    for ball in draw_result:
      draw_count[ball] = draw_count.get(ball,0) + 1
    #we assume we have the expected draw to start
    expected = 1
    for ball_type,ball_count in expected_balls.items():
      try:
        if draw_count[ball_type] < ball_count:
          print("{2} Expected: {0} Drawn: {1}".format(ball_count, draw_count[ball_type],ball_type))
          #if we find an entry in our draw count of the same type as an entry in the expected draw, compare their associated value pairs to make sure the draw is not less than the expected amount. If it is, it is no longer the expected pair and we can exit the loop.
          expected = 0
          break
      except KeyError:
          #if we made a call from the expected ball type to the draw count and it results in a keyerror, we can assume our draw is not the expected draw
          expected = 0
          break
      #print("Expected: {0} Drawn: {1}".format(expected_balls,draw_count))
    if expected:
      success_rate += 1
    #print("successes {0} in attempt {1}".format(success_rate,num_experiments))



  return success_rate/num_experiments
