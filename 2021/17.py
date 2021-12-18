# Advent of Code: Day 17

## Tests
def test1():
  input = "target area: x=20..30, y=-10..-5".split()
  assert part1(input) == 45

def test2():
  input = "target area: x=20..30, y=-10..-5".split()
  assert part2(input) == 112

def checkProbe(x1, x2, y1, y2, x_velocity, y_velocity):
  high_y = y2
  probe = [0, 0]
  found = False
  while probe[0] <= x2 and probe[1] >= y2:
    if probe[1] <= y1 and probe[1] >= y2 and probe[0] >= x1 and probe[0] <= x2:
      # Break if we find a match
      found = True
      break

    if x_velocity != 0:
      probe[0] += x_velocity
      x_velocity += -1 if x_velocity > 0 else 1

    probe[1] += y_velocity
    y_velocity -= 1

    if probe[1] > high_y:
      high_y = probe[1]

  if not found:
    return False, 0

  return True, high_y

## Part 1
def part1(parameters):
  x = parameters[2].split("..")
  x1 = int(x[0].split("=")[1])
  x2 = int(x[1].split(",")[0])
  y = parameters[3].split("..")
  y2 = int(y[0].split("=")[1])
  y1 = int(y[1])

  y_velocity = y2
  best_y = -500
  while y_velocity < 500:
    x_velocity = x2
    while x_velocity > 0:
      if x_velocity == 6 and y_velocity == 9:
        print
      winner, high_y = checkProbe(x1, x2, y1, y2, x_velocity, y_velocity)
      if winner and high_y > best_y:
        best_y = high_y

      x_velocity -= 1
    y_velocity += 1

  return best_y

test1()


def checkProbe2(x1, x2, y1, y2, x_velocity, y_velocity):
  probe = [0, 0]
  found = False
  while probe[0] <= x2 and probe[1] >= y2:
    if probe[1] <= y1 and probe[1] >= y2 and probe[0] >= x1 and probe[0] <= x2:
      # Break if we find a match
      found = True
      break

    if x_velocity != 0:
      probe[0] += x_velocity
      x_velocity += -1 if x_velocity > 0 else 1

    probe[1] += y_velocity
    y_velocity -= 1

  if not found:
    return False

  return True

# Part 2
def part2(parameters):
  x = parameters[2].split("..")
  x1 = int(x[0].split("=")[1])
  x2 = int(x[1].split(",")[0])
  y = parameters[3].split("..")
  y2 = int(y[0].split("=")[1])
  y1 = int(y[1])

  y_velocity = y2
  pairs = set()
  while y_velocity < 500:
    x_velocity = x2
    while x_velocity > 0:
      winner = checkProbe2(x1, x2, y1, y2, x_velocity, y_velocity)
      if winner:
        pairs.add((x_velocity, y_velocity))

      x_velocity -= 1
    y_velocity += 1

  return len(pairs)

test2()

with open("2021/input/17.txt", "r") as F:
  L = F.readline().rstrip().split()
  assert part1(L[:]) == 13041
  assert part2(L[:]) == 1031