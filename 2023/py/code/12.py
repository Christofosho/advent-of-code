import os
from collections import deque

sample1 = [
"???.### 1,1,3",
".??..??...?##. 1,1,3",
"?#?#?#?#?#?#?#? 1,3,1,6",
"????.#...#... 4,1,1",
"????.######..#####. 1,6,5",
"?###???????? 3,2,1"
]

def part1(L):
  arrangements = 0
  for row in L:
    springs, damages = row.split()
    damages = list(map(int, damages.split(",")))

    stack = [(0, 0, 0)]
    while stack:
      spring, damage, seen = stack.pop()
      # Reached the end of the springs list
      if spring == len(springs):

        # Add 1 more to arrangements if past final damages,
        # only when there are no hashes currently counted.
        if damage == len(damages) and seen == 0:
          arrangements += 1

        # Or add one more if at the end of the
        # final group of damaged springs.
        elif damage == len(damages) - 1 and damages[damage] == seen:
          arrangements += 1

        continue

      for symbol in ["#", "."]:

        # Must calculate permutations as matches are found.
        if springs[spring] == symbol or springs[spring] == "?":

          # A gap has been located, move forward through
          # the springs to the next spring.
          if symbol == "." and seen == 0:
            stack.append((spring + 1, damage, 0))

          # A damage has been matched.
          elif symbol == "." and seen > 0:
            if damage < len(damages) and damages[damage] == seen:
              stack.append((spring + 1, damage + 1, 0))

          # A damaged spring has been spotted,
          # so add to the seen count.
          elif symbol == "#":
            stack.append((spring + 1, damage, seen + 1))

  return arrangements

memo = {}
def calcRow(spring, damage, seen, springs, damages):
    if (spring, damage, seen) in memo:
      return memo[(spring, damage, seen)]

    # Reached the end of the springs list
    elif spring == len(springs):

      # Add 1 more to arrangements if past final damages,
      # only when there are no hashes currently counted.
      # Or add one more if at the end of the
      # final group of damaged springs.
      if damage == len(damages) and seen == 0:
        return 1

      elif damage == len(damages) - 1 and damages[damage] == seen:
        return 1

      return 0

    current = 0
    for symbol in ["#", "."]:

      # Must calculate permutations as matches are found.
      if springs[spring] == symbol or springs[spring] == "?":

        if symbol == ".":
          # A gap has been located, move forward through
          # the springs to the next spring.
          if seen == 0:
            current += calcRow(spring + 1, damage, 0, springs, damages)

          # A damage has been matched.
          elif damage < len(damages) and damages[damage] == seen:
            current += calcRow(spring + 1, damage + 1, 0, springs, damages)

        # A damaged spring has been spotted,
        # so add to the seen count.
        elif symbol == "#":
          current += calcRow(spring + 1, damage, seen + 1, springs, damages)

    memo[(spring, damage, seen)] = current
    return current

def part2(L):
  arrangements = 0
  for row in L:
    memo.clear()

    springs, damages = row.split()
    springs, damages = "?".join([springs] * 5), ",".join([damages] * 5)

    damages = list(map(int, damages.split(",")))

    arrangements +=  calcRow(0, 0, 0, springs, damages)

  return arrangements

print("Test 1")
assert part1(sample1) == 21
print("Test 1 passed")

print("Test 3")
assert part2(sample1) == 525152
print("Test 3 passed")

path = os.path.join(os.path.dirname(__file__), "../input/12.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 7857
  print("assert part1(L) == 7857 passed")

  print("Begin Part 2:")
  assert part2(L) == 28606137449920
  print("assert part2(L) == 28606137449920 passed")
