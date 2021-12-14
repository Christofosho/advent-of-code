# Advent of Code: Day 13

## Constants
x = 0
y = 1
sample = [
  "6,10",
  #"0,14",
  "9,10",
  "0,3",
  "10,4",
  "4,11",
  "6,0",
  "6,12",
  "4,1",
  "0,13",
  "10,12",
  "3,4",
  "3,0",
  "8,4",
  "1,10",
  #"2,14",
  "8,10",
  "9,0",
  "",
]

## Helpers
def generatePaper(points):
  height = 0
  width  = 0
  for point in points:
    height = max(height, point[y])
    width  = max(width,  point[x])

  L = [
    [0 for _ in range(width + 1)]
    for _ in range(height + 1)
  ]
  
  for point in points:
    L[point[y]][point[x]] = 1

  return L

def foldPaper(paper, fold):
  axis = fold[x]
  row  = int(fold[y])
  new = []

  if axis == "y":
    new = [list(r) for r in paper[:row]]
    overlap = [list(r) for r in paper[row+1:]]
    looping = len(new) if len(overlap) > len(new) else len(overlap)
    inner = len(new[0])
    for i in range(looping):
      for j in range(inner):
        new[-1-i][j] = max(overlap[i][j], new[-1-i][j])

  else: # x-axis
    new = [piece[:row] for piece in paper]
    overlap = [piece[row+1:] for piece in paper]
    inner = len(new[0]) if len(overlap[0]) > len(new[0]) else len(overlap[0])
    for i in range(len(new)):
      for j in range(inner):
        new[i][-1-j] = max(overlap[i][j], new[i][-1-j])


  return new

def countDots(L):
  count = 0
  for row in L:
    for cell in row:
      if cell > 0:
        count += 1
  return count

## Tests
def test1(callback):
  assert callback([*sample, "fold along y=7"]) == 15
  assert callback([*sample, "fold along x=5"]) == 15

def test2(callback):
  return callback([*sample, "fold along y=7", "fold along x=5", "fold along y=3"])

## Part 1
def part1(L):
  A = [[int(num) for num in row.split(",")] for row in L if row[0:4] != "fold" and row != ""]
  B = [row.split()[2].split("=") for row in L[len(A)+1:]]

  paper = generatePaper(A)
  for fold in B:
    new = foldPaper(paper, fold)
    break

  return countDots(new)

test1(part1)

## Part 2
def part2(L):
  A = [[int(num) for num in row.split(",")] for row in L if row[0:4] != "fold" and row != ""]
  B = [row.split()[2].split("=") for row in L[len(A)+1:]]

  paper = generatePaper(A)
  for fold in B:
    paper = foldPaper(paper, fold)

  return paper

print(test2(part2))

with open("2021/input/13.txt", "r") as F:
  L = [line.rstrip() for line in F.readlines()]
  assert part1(L[:]) == 708
  print(part2(L[:]))