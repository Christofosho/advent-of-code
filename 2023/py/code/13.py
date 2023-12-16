import os
from collections import deque

sample1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

sample2 = """..#......#...
###.####.####
.#..#..#.##..
.#..#..#..#..
##..####..###
##..####..###
.....##......
.###.##.###..
##..####..###
#.########.##
.##......##..
.#..#..#..#..
#...####...##"""

def part1(L):
  fields = [[]]
  for row in L:
    row = row.strip("\n")
    if row == "":
      fields.append([])
    else:
      fields[-1].append(row)

  current = 0
  for field in fields:
    prev = field[0]
    for y, row in list(enumerate(field))[1:]:
      if row == prev:
        s1, s2 = 0, len(field) - 1
        if y > s2 / 2:
          diff = len(field) - y
          s1 = y - diff
        else:
          s2 = y * 2 - 1

        found = True
        while s1 < s2:
          if field[s1] != field[s2]:
            found = False
            break

          s1 += 1
          s2 -= 1

        if found:
          current += y * 100
          break

      prev = field[y]


    else:
      prev = [field[y][0] for y in range(len(field))]
      for x in range(len(field[0]))[1:]:
        col = [row[x] for row in field]
        if col == prev:
          s1, s2 = 0, len(field[0]) - 1
          if x > s2 / 2:
            diff = len(field[0]) - x
            s1 = x - diff
          else:
            s2 = x * 2 - 1

          found = True
          while s1 < s2:
            col1 = [row[s1] for row in field]
            col2 = [row[s2] for row in field]
            if col1 != col2:
              found = False
              break

            s1 += 1
            s2 -= 1

          if found:
            current += x
            break

        prev = col

  return current

def part2(L):
  fields = [[]]
  for row in L:
    row = row.strip("\n")
    if row == "":
      fields.append([])
    else:
      fields[-1].append(row)

  current = 0
  for field in fields:
    prev = field[0]
    for y, row in list(enumerate(field))[1:]:
      initialSmudges = 0
      for i, cell in enumerate(field[y]):
        if cell != prev[i]:
          initialSmudges += 1

      if initialSmudges < 2:
        s1, s2 = 0, len(field) - 1
        if y > s2 / 2:
          diff = len(field) - y
          s1 = y - diff
        else:
          s2 = y * 2 - 1

        found = True
        smudges = 0
        while s1 < s2:
          if field[s1] != field[s2]:
            for i, cell in enumerate(field[s1]):
              if cell != field[s2][i]:
                smudges += 1

            if smudges > 1:
              found = False
              break

          s1 += 1
          s2 -= 1

        if found and smudges == 1:
          current += y * 100
          break

      prev = field[y]


    else:
      prev = [field[y][0] for y in range(len(field))]
      for x in range(len(field[0]))[1:]:
        col = [row[x] for row in field]
        initialSmudges = 0
        for i, cell in enumerate(col):
          if cell != prev[i]:
            initialSmudges += 1

        if initialSmudges < 2:
          s1, s2 = 0, len(field[0]) - 1
          if x > s2 / 2:
            diff = len(field[0]) - x
            s1 = x - diff
          else:
            s2 = x * 2 - 1

          found = True
          smudges = 0
          while s1 < s2:
            col1 = [row[s1] for row in field]
            col2 = [row[s2] for row in field]

            if col1 != col2:
              for i, cell in enumerate(col1):
                if cell != col2[i]:
                  smudges += 1

              if smudges > 1:
                found = False
                break

            s1 += 1
            s2 -= 1

          if found and smudges == 1:
            current += x
            break

        prev = col

  return current

print("Test 1")
assert part1(sample1.split("\n")) == 405
print("Test 1 passed")

print("Test 2")
assert part1(sample2.split("\n")) == 12
print("Test 2 passed")

print("Test 3")
assert part2(sample1.split("\n")) == 400
print("Test 3 passed")

print("Test 4")
assert part2(sample2.split("\n")) == 6
print("Test 4 passed")

path = os.path.join(os.path.dirname(__file__), "../input/13.txt")
with open(path, "r") as f:
  L = list(f)

  print("Begin Part 1:")
  assert part1(L) == 34918
  print("assert part1(L) == 34918 passed")

  print("Begin Part 2:")
  assert part2(L) == 33054
  print("assert part2(L) == 33054 passed")
