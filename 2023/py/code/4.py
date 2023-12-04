import os
import re
from collections import defaultdict

sample = [
  "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
  "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
  "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
  "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
  "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
  "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

def getMatches(line, pattern):
    win, cur = line.split(": ")[1].split(" | ")
    win = set(pattern.findall(win))
    cur = set(pattern.findall(cur))

    return len(win & cur)

def part1(input):
  total = 0
  pattern = re.compile(r'(\d+)')
  for line in input:
    matches = getMatches(line, pattern) - 1
    if matches > -1:
      total += 2 ** matches

  return total

def part2(input):
  total = len(input)
  extra = {}
  pattern = re.compile(r'(\d+)')
  for i, line in enumerate(input):
    matches = getMatches(line, pattern)

    if matches > 0:
      total += matches * extra.get(i+1, 1)
      for match in range(matches):
        # Add one to i for the card number
        # Add one to match for the next card
        # because match begins at 0 when using range.
        nextCard = i + 1 + match + 1
        extra[nextCard] = extra.get(nextCard, 1) + extra.get(i + 1, 1)

  print(extra)
  print(total)
  return total

print("Test 1")
assert part1(sample) == 13
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 30
print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/4.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 25183
  print("assert part1(L) == 0 passed")

  print("Begin Part 2:")
  assert part2(L) == 5667240
  print("assert part2(L) == 0 passed")