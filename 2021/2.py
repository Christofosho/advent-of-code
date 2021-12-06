# Advent of Code: Day 2

## Part 1
def part1(L):
  H = 0
  D = 0
  for line in L:
    direction, q = line.split()
    q = int(q)
    if direction == "forward":
      H += q

    elif direction == "down":
      D += q

    elif direction == "up":
      D -= q

  return H * D

## Part 2
def part2(L):
  H = 0
  D = 0
  A = 0
  for line in L:
    direction, q = line.split()
    q = int(q)

    if direction == "forward":
      H += q
      D += A * q

    elif direction == "down":
      A += q

    elif direction == "up":
      A -= q

  return H * D

with open("2021/input/2.txt") as F:
  L = F.readlines()

  print("Begin Part 1:")
  print("assert part1(L) == 1727835")
  assert part1(L) == 1727835
  print("Part 1 Successful\n")

  print("Begin Part 2:")
  print("assert part2(L) == 1544000595")
  assert part2(L) == 1544000595
  print("Part 2 Successful\n")
