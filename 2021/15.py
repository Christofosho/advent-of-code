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

def getCost(cave, node, costs={}, visited={}):
  x = node[0]
  y = node[1]
  key = f"{x}-{y}"
  visited[key] = True
  cost = costs.get(key, None)
  if cost != None: # Cache
    return cost

  if x+len(cave[0]) < 0 or y+len(cave) < 0:
    return 0

  compare = []
  if y-1 > 0 and not visited.get(f"{x}-{y-1}", False):
    compare.append(getCost(cave, [x, y-1], costs, visited))
  if x-1 > 0 and not visited.get(f"{x-1}-{y}", False):
    compare.append(getCost(cave, [x-1, y], costs, visited))
  if x+1 < len(cave[0]) and not visited.get(f"{x+1}-{y}", False):
    compare.append(getCost(cave, [x+1, y], costs, visited))
  if y+1 < len(cave) and not visited.get(f"{x}-{y+1}", False):
    compare.append(getCost(cave, [x, y+1], costs, visited))

  if len(compare) > 0:
    costs[key] = cave[y][x] + min(compare)
  else:
    costs[key] = cave[y][x]
  return costs[key]

def getDistance(height, width, node):
  return abs(width - node[0]) + abs(height - node[1])

## Part 1
def part1(cave):
  x = 0
  y = 0
  height = len(cave)
  width  = len(cave[0])
  to_check = [[x, y]]
  checked  = []
  while len(to_check) > 0:
    cost = getCost(cave, to_check[-1]) - cave[0][0]
    dist = getDistance(height, width, to_check[-1])
    to_check.pop()

    total = cost + dist
  print(total)

test1()
test2()

def part2(cave):
  pass

#test2()

with open("2021/input/15.txt", "r") as F:
  L = [line.rstrip() for line in F.readlines()]
  L = [list(map(int,list(i))) for i in L]
  assert part1(L[:]) == 0
  #assert part2(L[:]) == 0