import os

# sample1 = [
# "R 6 (#70c710)",
# "D 5 (#0dc571)",
# "L 2 (#5713f0)",
# "D 2 (#d2c081)",
# "R 2 (#59c680)",
# "D 2 (#411b91)",
# "L 5 (#8ceee2)",
# "U 2 (#caa173)",
# "L 1 (#1b58a2)",
# "U 2 (#caa171)",
# "R 2 (#7807d2)",
# "U 3 (#a77fa3)",
# "L 2 (#015232)",
# "U 2 (#7a21e3)",
# ]

# sample2 = [
# "R 6 (#70c710)",
# "D 5 (#0dc571)",
# "L 2 (#5713f0)",
# "D 2 (#d2c081)",
# "R 2 (#59c680)",
# "D 2 (#411b91)",
# "L 1 (#8ceee2)",
# "U 1 (#8ceee2)",
# "L 1 (#8ceee2)",
# "D 1 (#8ceee2)",
# "L 1 (#8ceee2)",
# "U 1 (#8ceee2)",
# "L 1 (#8ceee2)",
# "D 1 (#8ceee2)",
# "L 1 (#8ceee2)",
# "U 2 (#caa173)",
# "L 1 (#1b58a2)",
# "U 2 (#caa171)",
# "R 2 (#7807d2)",
# "U 3 (#a77fa3)",
# "L 2 (#015232)",
# "U 2 (#7a21e3)"
# ]

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

dirs = {
  "D": 1,
  "U": -1
}

def rewriteHistory(history, dx, dy):
  rewrite = []
  for x, y, direction in history:
    x += dx
    y += dy

    rewrite.append((x, y, direction))

  return rewrite

def getCoords(rewrite):
  # Accrue side walls for calculating interception
  coords = {}
  coord = [rewrite[0][X], rewrite[0][Y]]
  for x, y, direction in rewrite[1:]:
    if direction in {"R","L"}:
      coord = [x, y]
      continue

    while coord != [x, y]:
      if coord[Y] not in coords:
        coords[coord[Y]] = []

      coords[coord[Y]].append((coord[X], 1 if direction == "D" else 0))

      coord = [coord[X], coord[Y] + dirs[direction]]

    if coord[Y] not in coords:
      coords[coord[Y]] = []

    coords[coord[Y]].append((coord[X], 1 if direction == "D" else 0))

  return coords

def calc(c):
  total = 0
  front = None
  back = None
  while True:
    if c:
      x, d = c.pop()
    else:
      d = 0

    if d == 0:
      if back != None:
        total += back - front + 1
        front = None
        if not c:
          break

      if front == None:
        front = x
        back = None

    elif d == 1:
      if front != None:
        back = x

  return total

def part1(L):
  coord = (0, 0)
  minX, minY = 0, 0
  history = [(0, 0, "R")]
  for instruction in L:
    direction, count, _ = instruction.split()
    x, y = coord
    if direction == "R":
      x = x + int(count)
    elif direction == "D":
      y = y + int(count)
    elif direction == "U":
      y = y - int(count)
    else:
      x = x - int(count)

    minX = min(x, minX)
    minY = min(y, minY)

    coord = (x, y)

    history.append((x, y, direction))

  # Range min should be 0, and colour needs parsing.
  rewrite = rewriteHistory(history, abs(minX), abs(minY))

  coords = getCoords(rewrite)

  total = 0
  for y, c in coords.items():
    c.sort(key=lambda x: -x[0])

    total += calc(c)

  return total

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

# print("Test 1")
# assert part1(sample1) == 62
# print("Test 1 passed")

# print("Test 2")
# assert part1(sample2) == 62
# print("Test 2 passed")

print("Test 3")
assert part1(sample3) == 61
print("Test 3 passed")

# print("Test 3")
# assert part2(sample1) == 952408144115
# print("Test 3 passed")


path = os.path.join(os.path.dirname(__file__), "../input/18.txt")
with open(path, "r") as f:
  L = list(f)

  print("Begin Part 1:")
  assert part1(L) == 61865
  print("assert part1(L) == 61865 passed")

  print("Begin Part 2:")
  assert part2(L) == 1073
  print("assert part2(L) == 1073 passed")

#73936
#64674
#62848
#61944
#61442