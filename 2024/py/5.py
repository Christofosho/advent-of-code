import os
from collections import defaultdict, deque

def part1(L):
  # parse input
  L = deque(L)
  d = defaultdict(set)
  row = L.popleft()
  while len(row) != 0:
    n, m = row.split("|")
    d[int(m)].add(int(n))
    row = L.popleft()

  # pop off list of pages, add to set, check set, add to total
  total = 0
  for row in L:
    s = set()
    row = row.split(",")
    mid = int(row[len(row) // 2])
    while row:
      c = int(row.pop())
      if c in d and d[c] & s:
        row = True
        break

      s.add(c)

    if not row:
      total += mid

  return total

def part2(L):
  # parse input
  L = deque(L)
  d = defaultdict(set)
  row = L.popleft()
  while len(row) != 0:
    n, m = row.split("|")
    d[int(m)].add(int(n))
    row = L.popleft()

  # pop off list of pages, add to set, check set, add bad
  bad = []
  for row in L:
    s = set()
    row = row.split(",")
    og = deque(map(int, row[:]))

    while row:
      c = int(row.pop())
      if c in d and d[c] & s:
        bad.append(og)
        break

      s.add(c)

  # reorder

  total = 0
  for row in bad:
    q = deque([row.pop()])
    while row:
      x = row.pop()
      mid = q[len(q) // 2]
      if mid not in d or (mid in d and x in d[mid]):
        q.append(x)
      else:
        q.appendleft(x)

    total += q[len(q) // 2]

  return total

print("Test 1")
r = part1([
  "47|53",
  "97|13",
  "97|61",
  "97|47",
  "75|29",
  "61|13",
  "75|53",
  "29|13",
  "97|29",
  "53|29",
  "61|53",
  "97|53",
  "61|29",
  "47|13",
  "75|47",
  "97|75",
  "47|61",
  "75|61",
  "47|29",
  "75|13",
  "53|13",
  "",
  "75,47,61,53,29",
  "97,61,53,29,13",
  "75,29,13",
  "75,97,47,61,53",
  "61,13,29",
  "97,13,75,29,47"
])
print(r)
assert r == 143
print("Test 1 passed")

print("Test 2")
r = part2([
  "47|53",
  "97|13",
  "97|61",
  "97|47",
  "75|29",
  "61|13",
  "75|53",
  "29|13",
  "97|29",
  "53|29",
  "61|53",
  "97|53",
  "61|29",
  "47|13",
  "75|47",
  "97|75",
  "47|61",
  "75|61",
  "47|29",
  "75|13",
  "53|13",
  "",
  "75,47,61,53,29",
  "97,61,53,29,13",
  "75,29,13",
  "75,97,47,61,53",
  "61,13,29",
  "97,13,75,29,47"
])
print(r)
assert r == 123
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/5.txt")
with open(path, "r") as f:
  F = f.readlines()
  L = [y.strip() for y in F]

  print("Part 1")
  r = part1(L)
  print(r)
  assert r == 7074
  print("Part 1 passed")

  print("Part 2")
  r = part2(L)
  print(r)
  # 99812796
  assert r == 1854
  print("Part 2 passed")