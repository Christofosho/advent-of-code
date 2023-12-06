import os
import re

sample = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."
]

numbers = {
  "0": 0,
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  # "zero": 0,
  # "one": 1,
  # "two": 2,
  # "three": 3,
  # "four": 4,
  # "five": 5,
  # "six": 6,
  # "seven": 7,
  # "eight": 8,
  # "nine": 9
}

# Given the start and end coordinates of a number,
# check for symbols around the edge.
def matcher(L, y, s, e, pattern):
  # Check all squares around N in the 2D array
  startX = max(0, s - 1)
  startY = max(0, y - 1)
  endX   = min(len(L[startY]) - 1, e)
  endY   = min(len(L) - 1, y + 1)
  while startY <= endY:
    currX = startX
    while currX <= endX:
      m = pattern.match(L[startY][currX])
      if bool(m):
        return True

      currX += 1

    startY += 1

  return False

def part1(L):
  pattern = re.compile(r'[^0-9\.]+')
  nums = []
  for y, line in enumerate(L):
    x = 0
    while x < len(line):
      e = x
      try:
        while line[e] in numbers:
          e += 1
      except:
        pass

      matched = matcher(L, y, x, e, pattern)

      if matched and line[x:e]:
        nums.append(int(line[x:e]))

      x = e + 1 if e == x else e

  return sum(nums)


# Given the start and end coordinates of a number,
# check for symbols around the edge.
def matcher2(L, y, s, e, pattern):
  # Check all squares around N in the 2D array
  startX = max(0, s - 1)
  startY = max(0, y - 1)
  endX   = min(len(L[startY]) - 1, e)
  endY   = min(len(L) - 1, y + 1)
  ret = []
  while startY <= endY:
    currX = startX
    while currX <= endX:
      m = pattern.match(L[startY][currX])
      if bool(m) and L[startY][currX] == "*":
        ret.append(f"{currX},{startY}")

      currX += 1

    startY += 1

  return ret

def part2(L):
  pattern = re.compile(r'[^0-9\.]+')
  matched = {}
  for y, line in enumerate(L):
    x = 0
    while x < len(line):
      e = x
      try:
        while line[e] in numbers:
          e += 1
      except:
        pass

      m = matcher2(L, y, x, e, pattern)

      if m and line[x:e]:
        for n in m:
          curr = matched.get(n, [])
          curr.append(line[x:e])
          matched[n] = curr

      x = e + 1 if e == x else e

  return sum(int(n[0]) * int(n[1]) for n in matched.values() if len(n) == 2)

print("Test 1")
assert part1(sample) == 4361
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 467835
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/3.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 535078
  print("assert part1(L) == 0 passed")

  print("Begin Part 2:")
  assert part2(L) == 75312571
  print("assert part2(L) == 0 passed")