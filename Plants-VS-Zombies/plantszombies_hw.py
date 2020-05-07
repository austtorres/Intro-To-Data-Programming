import random
def plant_power(heroes):
  """creates random values for plants p, q, and r; adds the sum of their factorials to generate their total power level"""

  p = random.randint(1, 10)
  q = random.randint(1, 10)
  r = random.randint(1, 10)
  n = 0
  total_power= 0
  for power in heroes:
    result = 0
    if power == 'p':
      n = p-1
      result = p
      while n > 0:
        result *= n
        n -= 1
      total_power += result
    elif power == 'q':
      n = q - 1
      result = q
      while n > 0:
        result *= n
        n -= 1
      total_power += result
    elif power == 'r':
      n = r-1
      result = r
      while n > 0:
        result *= n
        n -= 1
      total_power += result
  return total_power



def zombie_power(villains):
  """generates random power levels for zombies x, y, and z; adds the sum of their factorials to calculate their total power level"""

  x = random.randint(1, 10)
  y = random.randint(1, 10)
  z = random.randint(1, 10)
  n = 0
  total_power= 0
  for power in villains:
    result = 0
    if power == 'x':
      n = x-1
      result = x
      while n > 0:
        result *= n
        n -= 1
      total_power += result
    elif power == 'y':
      n = y - 1
      result = y
      while n > 0:
        result *= n
        n -= 1
      total_power += result
    elif power == 'z':
      n = z-1
      result = z
      while n > 0:
        result *= n
        n -= 1
      total_power += result
  return total_power

def war_begins(hero, villain, seed):
  """Checks to see if the plants or zombies have the higher power level and declares the one with the highest level the winner; if they tie it prints 'draw'"""

  random.seed(seed)
  plant_sum = plant_power(hero)
  zombie_sum = zombie_power(villain)
  if plant_sum > zombie_sum:
    print "Plants save the day!"
  elif zombie_sum > plant_sum:
    print "Zombies are here to stay!"
  else:
    print "IT'S A DRAW!"
