import os
from collections import Counter

def part1(L):
  L = [list(map(int, x.split('   '))) for x in L]
  a = sorted(L, key=lambda x: x[0])
  b = sorted(L, key=lambda x: x[1])
  return sum(abs(a[i][0] - b[i][1]) for i in range(len(a)))

def part2(L):
  L = [list(map(int, x.split('   '))) for x in L]
  a = map(lambda x: x[0], L)
  b = Counter(map(lambda x: x[1], L))
  t = 0
  for n in a:
    if n not in b:
      continue

    t += n * b[n]

  return t


print("Test 1")
r = part1([
  "3   4",
  "4   3",
  "2   5",
  "1   3",
  "3   9",
  "3   3"
])
print(r)
assert r == 11
print("Test 1 passed")

print("Test 2")
r = part2(
[
  "3   4",
  "4   3",
  "2   5",
  "1   3",
  "3   9",
  "3   3"
]
)
print(r)
assert r == 31
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/1.txt")
with open(path, "r") as f:
  F = f.readlines()
  L = [y.strip() for y in F]

  print("Part 1")
  r = part1(L)
  print(r)
  assert r == 2192892
  print("Part 1 passed")

  print("Part 2")
  r = part2(L)
  print(r)
  assert r == 22962826
  print("Part 2 passed")