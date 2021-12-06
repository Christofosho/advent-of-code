# Advent of Code: Day 1

## Part 1
def part1(L):
  count = 0
  depth = L[0]
  for next_depth in L[1:]:
    if next_depth > depth:
      count += 1
    depth = next_depth

  return count

## Part 2
def part2(L):
  count = 0
  depth = L[0] + L[1] + L[2]
  for a, b, c in zip(L[1:], L[2:], L[3:]):
    next_depth = a + b + c
    if next_depth > depth:
      count += 1
    depth = next_depth

  return count

print("Begin Test Part 1:")
print("assert part1([2, 4, 5, 3, 3, 4, 7, 1]) == 4")
assert part1([2, 4, 5, 3, 3, 4, 7, 1]) == 4
print("Test Part 1 successful\n")

print("Begin Test Part 2:")
print("assert part1([2, 4, 5, 3, 3, 4, 7, 1]) == 4")
assert part2([2, 4, 5, 3, 3, 4, 7, 1]) == 2
print("Test Part 2 Successful\n")

with open("2021/input/1.txt", "r") as f:
  F = f.readlines()
  L = [int(y) for y in F]

  print("Begin Part 1:")
  print("assert part1(L) == 1676")
  assert part1(L) == 1676
  print("Part 1 Successful\n")

  print("Begin Part 2:")
  print("assert part2(L) == 1706")
  assert part2(L) == 1706
  print("Part 2 Successful\n")