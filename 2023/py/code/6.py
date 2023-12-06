import os

sample = [
"Time:      7  15   30",
"Distance:  9  40  200"
]

def part1(L):
  times = map(int, L[0].split(":")[1].split())
  distances = map(int, L[1].split(":")[1].split())

  total = 1
  for time, distance in zip(times, distances):
    count = 0
    for t in range(1, time + 1):
      if t * (time - t) > distance:
        count += 1

    total *= count

  return total

def part2(L):
  time = int(L[0].split(":")[1].replace(" ", ""))
  distance = int(L[1].split(":")[1].replace(" ", ""))

  total = 0
  for t in range(1, time + 1):
    if t * (time - t) > distance:
        total += 1

  return total

print("Test 1")
assert part1(sample) == 288
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 71503
print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/6.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 588588
  print("assert part1(L) == 588588 passed")

  print("Begin Part 2:")
  assert part2(L) == 34655848
  print("assert part2(L) == 34655848 passed")