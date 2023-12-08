import os
import math

sample = [
  "RL",
  "",
  "AAA = (BBB, CCC)",
  "BBB = (DDD, EEE)",
  "CCC = (ZZZ, GGG)",
  "DDD = (DDD, DDD)",
  "EEE = (EEE, EEE)",
  "GGG = (GGG, GGG)",
  "ZZZ = (ZZZ, ZZZ)"
]

sample2 = [
  "LLR",
  "",
  "AAA = (BBB, BBB)",
  "BBB = (AAA, ZZZ)",
  "ZZZ = (ZZZ, ZZZ)"
]

sample3 = [
  "LR",
  "",
  "11A = (11B, XXX)",
  "11B = (XXX, 11Z)",
  "11Z = (11B, XXX)",
  "22A = (22B, XXX)",
  "22B = (22C, 22C)",
  "22C = (22Z, 22Z)",
  "22Z = (22B, 22B)",
  "XXX = (XXX, XXX)"
]

class Node():
  val = None
  right = None
  left = None

  def __init__(self, val):
    self.val = val

  def __repr__(self):
    return self.val

  def addRight(self, right):
    self.right = right

  def addLeft(self, left):
    self.left = left

def part1(L):
  dirs = L[0]
  steps = [step.split(" = ") for step in L[2:]]
  steps = {
    step[0]: (Node(step[0]), step[1].replace("(", "").replace(")", "").split(", "))
    for step in steps
  }
  
  for step in steps.values():
    step[0].addRight(steps[step[1][1]][0])
    step[0].addLeft(steps[step[1][0]][0])

  for step in steps:
    steps[step] = steps[step][0]

  node = steps["AAA"]
  count = 0
  i = 0
  while node.val != "ZZZ":
    count += 1
    if dirs[i] == "R":
      node = node.right
    else:
      node = node.left
    i = 0 if i >= (len(dirs) - 1) else i + 1

  return count

def part2(L):
  dirs = L[0]
  steps = [step.split(" = ") for step in L[2:]]
  steps = {
    step[0]: (Node(step[0]), step[1].replace("(", "").replace(")", "").split(", "))
    for step in steps
  }
  
  for step in steps.values():
    step[0].addRight(steps[step[1][1]][0])
    step[0].addLeft(steps[step[1][0]][0])

  for step in steps:
    steps[step] = steps[step][0]

  nodes = [step for step in steps.values() if step.val[2] == "A"]
  i = 0

  LCM = []
  for node in nodes:
    quant = 0
    i = 0
    while node.val[2] != "Z":
      quant += 1
      node = node.right if dirs[i] == "R" else node.left
      i = 0 if i >= (len(dirs) - 1) else i + 1

    LCM.append(quant)

  return math.lcm(*LCM)

print("Test 1")
assert part1(sample) == 2
print("Test 1 passed")

print("Test 2")
assert part1(sample2) == 6
print("Test 2 passed")

print("Test 3")
assert part2(sample3) == 6
print("Test 3 passed")


path = os.path.join(os.path.dirname(__file__), "../input/8.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 19241
  print("assert part1(L) == 19241 passed")

  print("Begin Part 2:")
  assert part2(L) == 9606140307013
  print("assert part2(L) == 9606140307013 passed")