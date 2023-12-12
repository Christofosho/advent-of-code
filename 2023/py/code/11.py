import os
from itertools import combinations

sample1 = [
"...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."
]

def part1(L):
  i = 1
  matrix = [] * len(L)
  ycounts = [0] * len(L)
  xcounts = [0] * len(L[0])
  for y, row in enumerate(L):
    matrix.append([])
    for x, cell in enumerate(row):
      if cell == "#":
        ycounts[y] += 1
        xcounts[x] += 1
        matrix[y].append(i)
        i += 1
      else:
        matrix[y].append(-1)

  matrix2 = [m[:] for m in matrix]
  for x in range(len(xcounts) - 1, -1, -1):
    if xcounts[x] == 0:
      xcounts.insert(x, 0)
      for y in range(len(matrix)):
        matrix2[y].insert(x, -1)

  for y in range(len(ycounts) - 1, -1, -1):
    if ycounts[y] == 0:
      matrix2.insert(y, [-1] * len(matrix2[y]))

  galaxies = []
  for y, row in enumerate(matrix2):
    for x, cell in enumerate(row):
      if cell != -1:
        galaxies.append((x, y))

  combined = list(combinations(galaxies, 2))

  distance = 0
  for c in combined:
    distance += abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])

  return distance

def part2(L, multiplier):
  ycounts = [0] * len(L)
  xcounts = [0] * len(L[0])
  for y, row in enumerate(L):
    for x, cell in enumerate(row):
      if cell == "#":
        ycounts[y] += 1
        xcounts[x] += 1

  # running totals
  xcount = 0
  for i, x in enumerate(xcounts):
    if x == 0:
      xcount += multiplier - 1
    xcounts[i] = xcount

  ycount = 0
  for i, y in enumerate(ycounts):
    if y == 0:
      ycount += multiplier - 1
    ycounts[i] = ycount

  galaxies = []
  for y, row in enumerate(L):
    for x, cell in enumerate(row):
      if cell == "#":
        galaxies.append((x + xcounts[x], y + ycounts[y]))

  combined = list(combinations(galaxies, 2))

  distance = 0
  for c in combined:
    distance += abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])

  return distance

print("Test 1")
assert part1(sample1) == 374
print("Test 1 passed")

print("Test 2")
assert part2(sample1, 10) == 1030
print("Test 2 passed")

print("Test 2")
assert part2(sample1, 100) == 8410
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/11.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 9609130
  print("assert part1(L) == 9609130 passed")

  print("Begin Part 2:")
  assert part2(L, 1000000) == 702152204842
  print("assert part2(L) == 702152204842 passed")
