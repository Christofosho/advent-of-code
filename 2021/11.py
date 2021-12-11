# Advent of Code: Day 9

## Helpers
def flash(L, i, j):
  if L[i][j] > 9:
    flashed = 1
    L[i][j] = 0
    if i != 0:
      if j != 0 and L[i-1][j-1] > 0: # Top left
        L[i-1][j-1] += 1
        flashed += flash(L, i-1, j-1)

      if j != len(L[i]) - 1 and L[i-1][j+1] > 0: # Top right
        L[i-1][j+1] += 1
        flashed += flash(L, i-1, j+1)

      if L[i-1][j] > 0: # Top
        L[i-1][j] += 1
        flashed += flash(L, i-1, j) 

    if i != len(L) - 1:
      if j != 0 and L[i+1][j-1] > 0: # Bottom left
        L[i+1][j-1] += 1
        flashed += flash(L, i+1, j-1)

      if j != len(L[i]) - 1 and L[i+1][j+1] > 0: # Bottom right
        L[i+1][j+1] += 1
        flashed += flash(L, i+1, j+1)

      if L[i+1][j] > 0:
        L[i+1][j] += 1
        flashed += flash(L, i+1, j) # Bottom

    if j != 0 and L[i][j-1] > 0:
      L[i][j-1] += 1
      flashed += flash(L, i, j-1) # Bottom

    if j != len(L[0]) - 1 and L[i][j+1] > 0:
      L[i][j+1] += 1
      flashed += flash(L, i, j+1) # Bottom

    return flashed

  return 0

## Test 1
def test1():
  L = [
    [7, 9, 3],
    [6, 8, 4],
    [1, 2, 5]
  ]
  return part1(L, 5)

## Part 1
def part1(L, steps):
  total = 0
  for _ in range(0, steps):
    for i in range(0, len(L)):
      for j in range(0, len(L[0])):
        L[i][j] += 1

    for i in range(0, len(L)):
      for j in range(0, len(L[0])):
        flashed = flash(L, i, j)
        total += flashed

    for i in range(0, len(L)):
      for j in range(0, len(L[0])):
        if L[i][j] >= 10:
          L[i][j] = 0

  return total

## Part 2
def part2(L):
  total = 0
  while True:
    print(L)
    if all([all(octo == 0 for octo in row) for row in L]):
      return total

    for i in range(0, len(L)):
      for j in range(0, len(L[0])):
        L[i][j] += 1

    for i in range(0, len(L)):
      for j in range(0, len(L[0])):
        flash(L, i, j)

    for i in range(0, len(L)):
      for j in range(0, len(L[0])):
        if L[i][j] >= 10:
          L[i][j] = 0
    
    total += 1

with open("2021/input/11.txt", "r") as F:
  L = [list(map(int, list(x.rstrip()))) for x in F.readlines()]

  #assert test1() == 8
  assert part1([Q[:] for Q in L], 100) == 1681

  #assert test2() == 2
  assert part2([Q[:] for Q in L]) == 276