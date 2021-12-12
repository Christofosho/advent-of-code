# Advent of Code: Day 12

## Helpers
def isBigCave(char):
  return (char[0] >= "A" and char[0] <= "Z")

## Test 1
def test1(callback):
  caves = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
  ]
  caves = [cave.split("-") for cave in list(caves)]
  return callback(caves)

def test2(callback):
  caves = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
  ]
  caves = [cave.split("-") for cave in list(caves)]
  return callback(caves)

def test3(callback):
  caves = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
  ]
  caves = [cave.split("-") for cave in caves]
  return callback(caves)

class Node:
  def __init__(self, name):
    self.name = name
    self.isBig = isBigCave(name)
    self.paths = []

  def __repr__(self):
    return (
      ("Big " if self.isBig else "small ")
      + "cave with "
      + f"{len(self.paths)} "
      + "paths"
    )

  def addPath(self, node):
    self.paths.append(node)

def findPaths(paths):
  total = 0
  node = paths[-1]
  for path in node.paths:
    if path.name == "end":
      total += 1
    else:
      # Small path can only be visited once
      if not(path.isBig) and path in paths:
        continue

      total += findPaths([*paths, path])
    
  return total

def findPaths2(paths):
  total = 0
  node = paths["nodes"][-1]
  for path in node.paths:
    if path.name == "end":
      total += 1
    elif path.name == "start":
      continue
    else:
      small = {**paths["small"]}
      if not(path.isBig):
        # Small path can only be visited once
        # Unless it is our "double" choice
        hasDouble = len([count for count in small.values() if count > 1]) > 0
        if path.name in small.keys() and hasDouble:
          continue

        # Track smalls to force only 1 doubled
        small[path.name] = small.get(path.name, 0) + 1

      total += findPaths2({
        # Add to small if we found another small
        "small": small,
        "nodes": [*paths["nodes"], path]
      })
    
  return total

def prepNodes(L):
  nodes = {}

  for path in L:
    # Add a node object to our dict
    if not nodes.get(path[0], False):
      nodes[path[0]] = Node(path[0])

    if not nodes.get(path[1], False):
      nodes[path[1]] = Node(path[1])

  for path in L:
    nodes[path[0]].addPath(nodes[path[1]])
    nodes[path[1]].addPath(nodes[path[0]])

  return nodes

## Part 1
def part1(L):
  nodes = prepNodes(L)
  return findPaths([nodes["start"]])

assert test1(part1) == 10
assert test2(part1) == 19
assert test3(part1) == 226

## Part 2
def part2(L):
  nodes = prepNodes(L)
  return findPaths2({
    "small": {},
    "nodes": [nodes["start"]],
  })

assert test1(part2) == 36
assert test2(part2) == 103
assert test3(part2) == 3509

with open("2021/input/12.txt", "r") as F:
  L = [x.rstrip().split("-") for x in F.readlines()]

  assert part1([Q[:] for Q in L]) == 5457

  #assert test2() == 2
  assert part2([Q[:] for Q in L]) == 128506