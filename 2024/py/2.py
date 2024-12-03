import os
from collections import deque

def part1(L):
  safe = 0
  for R in L:
    row = R.split(" ")
    prev = int(row[0])
    if prev > int(row[1]):
      for n in row[1:]:
        if prev < int(n):
          break
        d = abs(prev - int(n))
        if d < 1 or d > 3:
          break

        prev = int(n)
      else:
        safe += 1
    else:
      for n in row[1:]:
        if prev > int(n):
          break
        d = abs(prev - int(n))
        if d < 1 or d > 3:
          break

        prev = int(n)
      else:
        safe += 1

  return safe

def part2(L):
  safe = 0
  for R in L:
    row = deque(map(int, R.split(" ")))
    prev = row.popleft()
    bad = 0
    if prev > row[0]:
      while len(row) > 0:
        d = abs(prev - row[0])
        if d < 1 or d > 3:
          row.popleft()
          bad += 1
          continue

        if bad > 1:
          break

        if len(row) == 0:
          safe += 1
          break

        if prev < row[0]:
          row.popleft()
          bad += 1

        if bad > 1:
          break

        if len(row) == 0:
          safe += 1

        if bad <= 1 and len(row) > 0:
          prev = row.popleft()

      else:
        if bad <= 1:
          safe += 1

    else:
      while len(row) > 0:
        d = abs(prev - row[0])
        if d < 1 or d > 3:
          row.popleft()
          bad += 1
          continue

        if bad > 1:
          break

        if len(row) == 0:
          safe += 1
          break

        if prev > row[0]:
          row.popleft()
          bad += 1

        if bad > 1:
          break

        if len(row) == 0:
          safe += 1

        if bad <= 1 and len(row) > 0:
          prev = row.popleft()

      else:
        if bad <= 1:
          safe += 1

  return safe


print("Test 1")
r = part1([
  "7 6 4 2 1",
  "1 2 7 8 9",
  "9 7 6 2 1",
  "1 3 2 4 5",
  "8 6 4 4 1",
  "1 3 6 7 9",
])
print(r)
assert r == 2
print("Test 1 passed")

print("Test 2")
r = part2([
  "7 6 4 2 1",
  "1 2 7 8 9",
  "9 7 6 2 1",
  "1 3 2 4 5",
  "8 6 4 4 1",
  "1 3 6 7 9",
])
print(r)
assert r == 4
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/2.txt")
with open(path, "r") as f:
  F = f.readlines()
  L = [y.strip() for y in F]

  print("Part 1")
  r = part1(L)
  print(r)
  assert r == 213
  print("Part 1 passed")

  print("Part 2")
  r = part2(L)
  print(r)
  assert r == 285
  print("Part 2 passed")