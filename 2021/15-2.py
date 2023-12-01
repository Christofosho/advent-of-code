# Advent of Code: Day 14

## Tests
def test1():
  input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
  ]
  assert part1([list(map(int,list(i))) for i in input]) == 40

def test2():
  input = [
    "19111",
    "11191",
    "99991",
    "99991",
    "99991",
  ]
  assert part1([list(map(int,list(i))) for i in input]) == 10

def checkCost(cave, y, x, costs, visited):
  key = f"{y}-{x}"
  visited[key] = True
  cost = costs.get(key, None)
  if cost != None: # Cache
    return cost

  if x+len(cave[0]) < 0 or y+len(cave) < 0:
    return 0

  compare = []
  if y-1 > 0 and not visited.get(f"{y-1}-{x}", False):
    compare.append(checkCost(cave, y-1, x, costs, visited))
  if x-1 > 0 and not visited.get(f"{y}-{x-1}", False):
    compare.append(checkCost(cave, y, x-1, costs, visited))
  if x+1 < len(cave[0]) and not visited.get(f"{y}-{x+1}", False):
    compare.append(checkCost(cave, y, x+1, costs, visited))
  if y+1 < len(cave) and not visited.get(f"{y+1}-{x}", False):
    compare.append(checkCost(cave, y+1, x, costs, visited))

  if len(compare) > 0:
    costs[key] = cave[y][x] + min(compare)
  else:
    costs[key] = cave[y][x]
  return costs[key]

## Part 1
def part1(cave):
  newMatrix = []
  costs = {}
  visited = {}
  cost = checkCost(cave, 0, 0, costs, visited)
  print(cost)
  row = len(cave) - 1
  col = len(cave[0]) - 1
  path = []
  while True:
    path.append(cave[row][col])
    below = None
    beside = None
    if row - 1 >= 0:
      below = newMatrix[row-1][col]
    if col - 1 >= 0:
      beside = newMatrix[row][col-1]

    if below != None:
      if beside != None and beside < below:
        col -= 1
      else:
        row -= 1
    elif beside != None:
      col -= 1
    else:
      break

  print(sum(path) - cave[-1][-1])
  return sum(path) - cave[-1][-1]


#test1()
test2()

def part2(cave):
  pass

#test2()

with open("2021/input/15.txt", "r") as F:
  L = [line.rstrip() for line in F.readlines()]
  L = [list(map(int,list(i))) for i in L]
  assert part1(L[:]) == 0
  #assert part2(L[:]) == 0