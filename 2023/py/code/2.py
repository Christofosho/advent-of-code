import os
import re

def part1(input) -> int:
  games = []
  skip = False
  for i, game in enumerate(input):
    draws = game.split(": ")[1]
    subsets = draws.split("; ")
    for subset in subsets:
      red = re.search(r'(\d+) red', subset)
      green = re.search(r'(\d+) green', subset)
      blue = re.search(r'(\d+) blue', subset)

      if red and int(red.group(1)) > 12:
        skip = True
      if green and int(green.group(1)) > 13:
        skip = True
      if blue and int(blue.group(1)) > 14:
        skip = True

      if skip:
        break
    if not skip:
      games.append(i + 1)

    skip = False

  return sum([int(game) for game in games])

def part2(input):
  games = []
  for game in input:
    draws = game.split(": ")[1]
    subsets = draws.split("; ")
    mins = {
      "red": 0,
      "green": 0,
      "blue": 0
    }
    for subset in subsets:
      red = re.search(r'(\d+) red', subset)
      green = re.search(r'(\d+) green', subset)
      blue = re.search(r'(\d+) blue', subset)

      if red and int(red.group(1)) > mins["red"]:
        mins["red"] = int(red.group(1))
      if green and int(green.group(1)) > mins["green"]:
        mins["green"] = int(green.group(1))
      if blue and int(blue.group(1)) > mins["blue"]:
        mins["blue"] = int(blue.group(1))

    games.append(mins["red"] * mins["green"] * mins["blue"])

  return sum(games)

sample = [
  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
  "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
  "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

print("Test 1")
assert part1(sample) == 8
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 2286
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/2.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 2439
  print("assert part1(L) == 2439 passed")

  print("Begin Part 2:")
  assert part2(L) == 63711
  print("assert part2(L) == 63711 passed")