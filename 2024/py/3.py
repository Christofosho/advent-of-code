import os
import re

def part1(L):
  L = [row.split("mul(") for row in L]
  total = 0
  p = re.compile(r"^(\d+),(\d+)\)")
  d = re.compile(r"don't\(\).*do")
  for row in L:

    for entry in row:
      matches = p.match(entry)
      if matches and matches.group(1) is not None and matches.group(2) is not None:
        total += int(matches.group(1)) * int(matches.group(2))

  return total

def part2(L):
  total = 0
  p = re.compile(r"^(\d+),(\d+)\)")
  d = re.compile(r"don\'t\(\).*?(?:do\(\)|\Z)")

  row = "".join(L)
  row = d.split(row)
  row = "".join(row)
  for entry in row.split("mul("):
      matches = p.match(entry)
      if matches and matches.group(1) is not None and matches.group(2) is not None:
        total += int(matches.group(1)) * int(matches.group(2))

  return total

print("Test 1")
r = part1(["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"])
print(r)
assert r == 161
print("Test 1 passed")

print("Test 2")
r = part2(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"])
print(r)
assert r == 48
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/3.txt")
with open(path, "r") as f:
  F = f.readlines()
  L = [y.strip() for y in F]

  print("Part 1")
  r = part1(L)
  print(r)
  assert r == 159892596
  print("Part 1 passed")

  print("Part 2")
  r = part2(L)
  print(r)
  # 99812796
  assert r == 92626942
  print("Part 2 passed")