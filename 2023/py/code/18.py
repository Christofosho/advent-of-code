import os

sample1 = [
"R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 5 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)",
]

sample2 = [
"R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 1 (#8ceee2)",
"U 1 (#8ceee2)",
"L 1 (#8ceee2)",
"D 1 (#8ceee2)",
"L 1 (#8ceee2)",
"U 1 (#8ceee2)",
"L 1 (#8ceee2)",
"D 1 (#8ceee2)",
"L 1 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)"
]

sample3 = [
"R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 1 (#8ceee2)",
"U 1 (#8ceee2)",
"L 2 (#8ceee2)",
"D 1 (#8ceee2)",
"L 2 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)"
]

X = 0
Y = 1

directionsToCoordinates = {
  "D": (0, 1),
  "U": (0, -1),
  "R": (1, 0),
  "L": (-1, 0)
}

# Note: I solved part 1 with a different method.
# Part 2 stumped me, so I did research and rewrote part 1.
def part1(L):
  # Step 1: Trace the perimeter
  perimeter = 0
  history = [(0, 0)]
  for instruction in L:
    direction, paces, _ = instruction.split()
    dx, dy = directionsToCoordinates[direction]
    x, y = history[-1]
    paces = int(paces)
    perimeter += paces
    history.append((
      x + (paces * dx),
      y + (paces * dy),
    ))

  # Step 2: Shoelace Formula
  area = 0
  for step, point in enumerate(history):
    nextStep = (step + 1) % len(history)
    area += point[Y] * (history[step - 1][X] - history[nextStep][X])

  # Step 3: Pick's Theorem
  interior = (abs(area) // 2) - (perimeter // 2) + 1

  # Step 4: Add the interior and perimeter to get the total value.
  total = interior + perimeter

  return total

# I did write this part myself, however..
def makeInstructions(L):
  newInstructions = []
  dirs = ["R", "D", "L", "U"]
  for instruction in L:
    _, _, colour = instruction.split()
    intermediary = list(colour[2:len(colour) - 1])
    direction = int(intermediary.pop())
    distance = int(f"0x{''.join(intermediary)}", 16)
    newInstructions.append(f"{dirs[direction]} {distance} (#FFFFFF)")
  return newInstructions

def part2(L):
  return part1(makeInstructions(L))

print("Test 1")
assert part1(sample1) == 62
print("Test 1 passed")

print("Test 2")
assert part1(sample2) == 62
print("Test 2 passed")

print("Test 3")
assert part1(sample3) == 61
print("Test 3 passed")

print("Test 3")
assert part2(sample1) == 952408144115
print("Test 3 passed")


path = os.path.join(os.path.dirname(__file__), "../input/18.txt")
with open(path, "r") as f:
  L = list(f)

  print("Begin Part 1:")
  assert part1(L) == 61865
  print("assert part1(L) == 61865 passed")

  print("Begin Part 2:")
  assert part2(L) == 40343619199142
  print("assert part2(L) == 40343619199142 passed")
