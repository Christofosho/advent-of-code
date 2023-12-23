import os
from collections import deque

sample1 = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

X = 0
Y = 1

D = {
  (0, 1),
  (0, -1),
  (1, 0),
  (-1, 0)
}

def part1(L, steps):
  grid = [list(l) for l in L.split("\n")]
  dist = [[1000 for _ in row] for row in grid]
  visited = [[0 for _ in row] for row in grid]
  start = [0, 0]
  for y, row in enumerate(grid):
    for x, cell in enumerate(row):
      if cell == "S":
        start = [x, y]

      if cell == "#":
        grid[y][x] = 1

      else:
        grid[y][x] = 0

  q = deque([[*start, 0]])
  while q:
    x, y, step = q.pop()
    if visited[y][x]:
      continue

    dist[y][x] = step
    for dx, dy in D:
      if (
        y + dy >= len(grid)
        or x + dx >= len(grid[y])
        or x + dx < 0
        or y + dy < 0
      ):
        continue

      if grid[y + dy][x + dx]:
        dist[y + dy][x + dx] = 127
        continue

      q.appendleft([x + dx, y + dy, step + 1])

    visited[y][x] = 1

  stops = 0
  for y, row in enumerate(dist):
    for x, cell in enumerate(row):
      if cell % 2 == 0 and cell <= steps:
        stops += 1

  return stops

def part2(L):
  pass

print("Test 1")
assert part1(sample1, 6) == 16
print("Test 1 passed")

# print("Test 2")
# assert part2(sample2) == 0
# print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/21.txt")
with open(path, "r") as f:
  L = f.read()

  print("Begin Part 1:")
  assert part1(L, 64) == 3658
  print("assert part1(L) == 3658 passed")

  # print("Begin Part 2:")
  # assert part2(L) == 0
  # print("assert part2(L) == 0 passed")
