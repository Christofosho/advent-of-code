import os
from collections import deque

sample = [
  "0 3 6 9 12 15",
  "1 3 6 10 15 21",
  "10 13 16 21 30 45"
]

def part1(L):
  L = [list(map(int, line.split())) for line in L]

  total = 0
  for line in L:
    rows = []
    while True:
      rows.append(line)
      nextL = []
      for n, m in zip(line, line[1:]):
        nextL.append(m - n)

      line = nextL

      if abs(nextL[-1]) == abs(nextL[0]):
        rows.append(nextL)
        break

    row = rows.pop()
    while rows:
      rows[-1].append(rows[-1][-1] + row[-1])
      row = rows.pop()

    total += row[-1]

  print(total)
  return total


def part2(L):
  L = [list(map(int, line.split())) for line in L]

  total = 0
  for line in L:
    rows = []
    while True:
      rows.append(deque(line))
      nextL = []
      for n, m in zip(line, line[1:]):
        nextL.append(m - n)

      line = nextL

      if abs(nextL[-1]) == abs(nextL[0]):
        rows.append(deque(nextL))
        break

    row = rows.pop()
    while rows:
      rows[-1].appendleft(rows[-1][0] - row[0])
      row = rows.pop()

    total += row[0]

  print(total)
  return total

print("Test 1")
assert part1(sample) == 114
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 2
print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/9.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 1479011877
  print("assert part1(L) == 1479011877 passed")

  print("Begin Part 2:")
  assert part2(L) == 973
  print("assert part2(L) == 973 passed")
