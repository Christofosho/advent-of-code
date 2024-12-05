import os

def scan(L, x, y):
  total = 0

  # Measure
  xR = x + 3
  xRL = xR < len(L[y])
  xL = x - 3
  xLL = xL > -1
  yD = y + 3
  yDL = yD < len(L)
  yU = y - 3
  yUL = yU > -1

  # R
  total += (
    xRL and
    L[y][x+1] == "M" and
    L[y][x+2] == "A" and
    L[y][xR] == "S"
  )

  # RD
  total += (
    xRL and yDL and
    L[y+1][x+1] == "M" and
    L[y+2][x+2] == "A" and
    L[yD][xR] == "S"
  )

  # D
  total += (
    yDL and
    L[y+1][x] == "M" and
    L[y+2][x] == "A" and
    L[yD][x] == "S"
  )

  # LD
  total += (
    xLL and yDL and
    L[y+1][x-1] == "M" and
    L[y+2][x-2] == "A" and
    L[yD][xL] == "S"
  )

  # L
  total += (
    xLL and
    L[y][x-1] == "M" and
    L[y][x-2] == "A" and
    L[y][xL] == "S"
  )

  # LU
  total += (
    xLL and yUL and
    L[y-1][x-1] == "M" and
    L[y-2][x-2] == "A" and
    L[yU][xL] == "S"
  )

  # U
  total += (
    yUL and
    L[y-1][x] == "M" and
    L[y-2][x] == "A" and
    L[yU][x] == "S"
  )

  # RU
  total += (
    xRL and yUL and
    L[y-1][x+1] == "M" and
    L[y-2][x+2] == "A" and
    L[yU][xR] == "S"
  )

  return total

def part1(L):
  total = 0
  for y, row in enumerate(L):
    for x, c in enumerate(row):
      if c == "X":
        total += scan(L, x, y)

  return total

def scan2(L, x, y):
  total = 0

  # Measure
  xR = x + 1
  xRL = xR < len(L[y])
  xL = x - 1
  xLL = xL > -1
  yD = y + 1
  yDL = yD < len(L)
  yU = y - 1
  yUL = yU > -1

  if not(xRL and xLL and yDL and yUL):
    return 0

  # LD -> RU + LU -> RD
  # M.S
  # .A.
  # M.S
  total += (
    (L[yD][xL] == "M" and L[yU][xR] == "S") and
    (L[yU][xL] == "M" and L[yD][xR] == "S")
  )

  # RD -> LU + LD -> RU
  # S.S
  # .A.
  # M.M
  total += (
    (L[yD][xR] == "M" and L[yU][xL] == "S") and
    (L[yD][xL] == "M" and L[yU][xR] == "S")
  )

  # RU -> LD + LU -> RD
  # M.M
  # .A.
  # S.S
  total += (
    (L[yU][xR] == "M" and L[yD][xL] == "S") and
    (L[yU][xL] == "M" and L[yD][xR] == "S")
  )

  # RU -> LD + RD -> LU
  # S.M
  # .A.
  # S.M
  total += (
    (L[yU][xR] == "M" and L[yD][xL] == "S") and
    (L[yD][xR] == "M" and L[yU][xL] == "S")
  )

  return total

def part2(L):
  total = 0
  for y, row in enumerate(L):
    for x, c in enumerate(row):
      if c == "A":
        total += scan2(L, x, y)

  return total

print("Test 1")
r = part1([
  "MMMSXXMASM",
  "MSAMXMSMSA",
  "AMXSXMAAMM",
  "MSAMASMSMX",
  "XMASAMXAMM",
  "XXAMMXXAMA",
  "SMSMSASXSS",
  "SAXAMASAAA",
  "MAMMMXMMMM",
  "MXMXAXMASX",
])
print(r)
assert r == 18
print("Test 1 passed")

print("Test 2")
r = part2([
  "MMMSXXMASM",
  "MSAMXMSMSA",
  "AMXSXMAAMM",
  "MSAMASMSMX",
  "XMASAMXAMM",
  "XXAMMXXAMA",
  "SMSMSASXSS",
  "SAXAMASAAA",
  "MAMMMXMMMM",
  "MXMXAXMASX",
])
print(r)
assert r == 9
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/4.txt")
with open(path, "r") as f:
  F = f.readlines()
  L = [y.strip() for y in F]

  print("Part 1")
  r = part1(L)
  print(r)
  assert r == 2557
  print("Part 1 passed")

  print("Part 2")
  r = part2(L)
  print(r)
  # 99812796
  assert r == 1854
  print("Part 2 passed")