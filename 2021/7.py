# Advent of Code: Day 7

## Helpers
def so_rt(L):
  L.sort()
  low = L[0]
  return [x - low for x in L]

def checkGas(mid):
  avg = L[mid]
  return sum(abs(avg - x) for x in L)

## Part 1
def part1(L):
  L = so_rt(L)
  return checkGas(len(L)//2)

## Part 2
def part2(L):
  L = so_rt(L)
  R = [0] * L[-1]
  for r in range(0, L[-1]):
    new = 0
    for crab in L:
      distance = abs(crab - r)
      if distance != 0:
        new += distance * (distance + 1) // 2
    R[r] = new
  print(min(R))
  return min(R)

with open("2021/input/7.txt", "r") as F:
  L = [int(x) for x in F.readline().split(",")]

  assert part1(L) == 331067
  assert part2(L) == 92881128