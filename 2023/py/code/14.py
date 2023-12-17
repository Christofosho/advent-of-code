import os
import math
from functools import cache
from collections import deque

sample1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def part1(L):
  cols = list(map(list, zip(*L)))
  total = 0
  for col in cols:
    openings = deque([])
    for pos, rock in enumerate(col):
      if rock == "O":
        if len(openings) > 0:
          newPos = openings.pop()
          col[newPos] = "O"
          col[pos] = "."
          openings.appendleft(pos)
          total += len(col) - newPos
        else:
          total += len(col) - pos

      elif rock == ".":
        openings.appendleft(pos)

      else:
        openings.clear()

  return total

@cache
def rotate(cols):
  for _ in range(4):
    cols = [list(c) for c in zip(*cols[::-1])]
    for col in cols:
      openings = deque([])
      for pos, rock in list(enumerate(col))[::-1]:
        if rock == "O":
          if len(openings) > 0:
            newPos = openings.pop()
            col[newPos] = "O"
            col[pos] = "."
            openings.appendleft(pos)

        elif rock == ".":
          openings.appendleft(pos)

        else:
          openings.clear()

  return tuple(tuple(col) for col in cols)

def getTotal(T):
  total = 0
  for y, row in enumerate(T):
    total += row.count("O") * (len(row) - y)

  return total

def part2(L):
  memo = {}
  T = tuple(tuple(col) for col in map(list, L))
  i = 0 # i starts at 1, but the += is immediately in the loop
  while i < 1_000_000_000:
    i += 1
    T = rotate(T)

    if T in memo:
      cycle = i - memo[T]
      hope = (1_000_000_000 - i) // cycle
      i += hope * cycle

    memo[T] = i

  val = getTotal(T)
  return val 

print("Test 1")
assert part1(sample1.split("\n")) == 136
print("Test 1 passed")

print("Test 2")
assert part2(sample1.split("\n")) == 64
print("Test 2 passed")

# print("Test 3")
# assert part2(sample1.split("\n")) == 400
# print("Test 3 passed")

# print("Test 4")
# assert part2(sample2.split("\n")) == 6
# print("Test 4 passed")

path = os.path.join(os.path.dirname(__file__), "../input/14.txt")
with open(path, "r") as f:
  L = list(f)

  print("Begin Part 1:")
  assert part1(L) == 107053
  print("assert part1(L) == 107053 passed")

  print("Begin Part 2:")
  assert part2(L) == 88371
  print("assert part2(L) == 88371 passed")
