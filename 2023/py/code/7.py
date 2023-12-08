import os
from collections import Counter
from itertools import chain

sample = [
"32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"
]

cards = {
  "A": "a",
  "K": "b",
  "Q": "c",
  "J": "d",
  "T": "e",
  "9": "f",
  "8": "g",
  "7": "h",
  "6": "i",
  "5": "j",
  "4": "k",
  "3": "l",
  "2": "m"
}

def part1(L):
  hands = [l.split() for l in L]

  ranks = {
    "5": [],
    "4": [],
    "FH": [],
    "3": [],
    "2": [],
    "1": [],
    "H": []
  }

  # Counters
  for i, hand in enumerate(hands):
    top = Counter(hand[0]).most_common()
    mapped = [cards[c] for c in hand[0]]
    if top[0][1] == 5:
      ranks["5"].append([mapped, int(hand[1])])

    elif top[0][1] == 4:
      ranks["4"].append([mapped, int(hand[1])])

    elif top[0][1] == 3 and top[1][1] == 2:
      ranks["FH"].append([mapped, int(hand[1])])

    elif top[0][1] == 3:
      ranks["3"].append([mapped, int(hand[1])])

    elif top[0][1] == 2 and top[1][1] == 2:
      ranks["2"].append([mapped, int(hand[1])])

    elif top[0][1] == 2:
      ranks["1"].append([mapped, int(hand[1])])

    else:
      ranks["H"].append([mapped, int(hand[1])])

  for rank in ranks.values():
    rank.sort(key=lambda r: r[0])

  total = 0
  for i, r in enumerate(reversed(list(chain(*list(ranks.values()))))):
    total += r[1] * (i + 1)
  print(total)
  return total

cards2 = {
  "A": "a",
  "K": "b",
  "Q": "c",
  "T": "e",
  "9": "f",
  "8": "g",
  "7": "h",
  "6": "i",
  "5": "j",
  "4": "k",
  "3": "l",
  "2": "m",
  "J": "n",
}

def part2(L):
  hands = [l.split() for l in L]

  ranks = {
    "5": [],
    "4": [],
    "FH": [],
    "3": [],
    "2": [],
    "1": [],
    "H": []
  }

  # Counters
  for i, hand in enumerate(hands):
    mapped = [cards2[c] for c in hand[0] if c != "J"]
    J = hand[0].count("J")

    if J == 5:
      ranks["5"].append([["n"] * 5, int(hand[1])])
      continue

    count = Counter(mapped)

    top = count.most_common()
    mapped = [cards2[c] for c in hand[0]]

    if top[0][1] + J == 5:
      ranks["5"].append([mapped, int(hand[1])])

    elif top[0][1] + J == 4:
      ranks["4"].append([mapped, int(hand[1])])

    elif top[0][1] + J == 3 and top[1][1] == 2 \
      or top[0][1] == 3 and top[1][1] + J == 2:
      ranks["FH"].append([mapped, int(hand[1])])

    elif top[0][1] + J == 3:
      ranks["3"].append([mapped, int(hand[1])])

    elif top[0][1] + J == 2 and top[1][1] == 2 \
      or top[0][1] == 2 and top[1][1] + J == 2:
      ranks["2"].append([mapped, int(hand[1])])

    elif top[0][1] + J == 2:
      ranks["1"].append([mapped, int(hand[1])])

    else:
      ranks["H"].append([mapped, int(hand[1])])

  for rank in ranks.values():
    rank.sort(key=lambda r: r[0])

  total = 0
  for i, r in enumerate(reversed(list(chain(*list(ranks.values()))))):
    total += r[1] * (i + 1)

  print(total)
  return total

print("Test 1")
assert part1(sample) == 6440
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 5905
print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/7.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 250946742
  print("assert part1(L) == 250946742 passed")

  print("Begin Part 2:")
  assert part2(L) == 251824095
  print("assert part2(L) == 251824095 passed")