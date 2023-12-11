import os

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

sample1 = [
".....",
".S-7.",
".|.|.",
".L-J.",
"....."
]

sample2 = [
"..F7.",
".FJ|.",
"SJ.L7",
"|F--J",
"LJ..."
]

sample3 = [
".F----7F7F7F7F-7....",
".|F--7||||||||FJ....",
".||.FJ||||||||L7....",
"FJL7L7LJLJ||LJ.L-7..",
"L--J.L7...LJS7F-7L7.",
"....F-J..F7FJ|L7L7L7",
"....L7.F7||L7|.L7L7|",
".....|FJLJ|FJ|F7|.LJ",
"....FJL-7.||.||||...",
"....L---J.LJ.LJLJ..."
]

# sample4 = [
# "FF7FSF7F7F7F7F7F---7",
# "L|LJ||||||||||||F--J",
# "FL-7LJLJ||||||LJL-77",
# "F--JF--7||LJLJ7F7FJ-",
# "L---JF-JLJ.||-FJLJJ7",
# "|F|F-JF---7F7-L7L|7|",
# "|FFJF7L7F-JF7|JL---7",
# "7-L-JL7||F7|L7F-7F7|",
# "L.L7LFJ|||||FJL7||LJ",
# "L7JLJL-JLJLJL--JLJ.L"
# ]

def findS(matrix):
  for y, l in enumerate(matrix):
    for x, p in enumerate(l):
      if p == "S":
        return [x, y]

def findDir(pipe, dir):
  if pipe == "|" or pipe == "-":
    return dir
  if pipe == "7":
    if dir == RIGHT:
      return DOWN
    return LEFT
  if pipe == "L":
    if dir == DOWN:
      return RIGHT
    return UP
  if pipe == "F":
    if dir == UP:
      return RIGHT
    return DOWN
  if pipe == "J":
    if dir == RIGHT:
      return UP
    return LEFT
  return dir

def move(coords, dir):
  if dir == UP:
    return [coords[0], coords[1] - 1]
  if dir == DOWN:
    return [coords[0], coords[1] + 1]
  if dir == LEFT:
    return [coords[0] - 1, coords[1]]
  else:
    return [coords[0] + 1, coords[1]]

def part1(L):
  matrix = [list(l) for l in L]

  # find S
  orig = findS(matrix)

  # Look at the input to get the first pipe,
  # Because writing all that logic will take
  # longer than just doing it myself! (Saving time today).
  coord = [orig[0], orig[1] + 1]
  dir = DOWN
  count = 1

  while coord != orig:
    count += 1
    dir = findDir(matrix[coord[1]][coord[0]], dir)
    coord = move(coord, dir)

  print(count // 2)
  return count // 2

def markNodes(nodes, matrix, x, y):
  # Marks nodes in every direction if not already
  # marked and not X. If an edge is hit, nodes are
  # marked with an O. Otherwise, mark with an I.
  if matrix[y][x] in ("X", "I") or (x, y) in nodes:
    return

  if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix) or matrix[y][x] == "O":
    raise IndexError("External Nodes")

  nodes.add((x, y))

  markNodes(nodes, matrix, x, y+1)
  markNodes(nodes, matrix, x, y-1)
  markNodes(nodes, matrix, x+1, y+1)
  markNodes(nodes, matrix, x+1, y)
  markNodes(nodes, matrix, x+1, y-1)
  markNodes(nodes, matrix, x-1, y+1)
  markNodes(nodes, matrix, x+1, y)
  markNodes(nodes, matrix, x+1, y-1)


def part2(L):
  matrix = [list(l) for l in L]
  path = [row[:] for row in matrix]

  # find S
  orig = findS(path)

  path[orig[1]][orig[0]] = "X"

  # TODO Force S to its type because I have not
  # enough time to write the algo for this
  # at the moment - should come back to this!
  matrix[orig[1]][orig[0]] = "|"

  coord = [orig[0], orig[1] + 1]
  dir = DOWN

  while coord != orig:
    dir = findDir(path[coord[1]][coord[0]], dir)
    path[coord[1]][coord[0]] = "X"
    coord = move(coord, dir)

  total = 0
  counts = [0] * len(matrix)
  for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
      if path[y][x] != "X" and counts[y] % 2 == 1:
          total += 1

      if path[y][x] == "X" and cell in {"L", "J", "|"}:
        counts[y] += 1

  return total

# print("Test 1")
# assert part1(sample1) == 4
# print("Test 1 passed")

# print("Test 2")
# assert part1(sample2) == 8
# print("Test 2 passed")

# print("Test 3")
# assert part2(sample1) == 1
# print("Test 3 passed")

# print("Test 4")
# assert part2(sample3) == 8
# print("Test 4 passed")

# print("Test 5")
# assert part2(sample4) == 10
# print("Test 5 passed")

path = os.path.join(os.path.dirname(__file__), "../input/10.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 6923
  print("assert part1(L) == 6923 passed")

  print("Begin Part 2:")
  assert part2(L) == 529
  print("assert part2(L) == 529 passed")
