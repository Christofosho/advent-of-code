import os
import re
from collections import OrderedDict
from functools import cache

sample1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

@cache
def h(s):
  return s * 17 % 256

def part1(L):
  steps = L.split(",")

  total = 0
  for step in steps:
    val = 0
    for c in step:
      val = h(val + ord(c))
    total += val

  return total


def part2(L):
  steps = L.split(",")
  pattern = re.compile(r"([a-z]+)([-=]{1})([0-9]*)")
  boxes = {}
  for step in steps:
    m = pattern.match(step)
    label, op, focal_length = m.groups()

    box = 0
    for c in label:
      box = h(box + ord(c))

    if op == "-":
      if box in boxes:
        if label in boxes[box]:
          del boxes[box][label]

    elif op == "=":
      if box not in boxes:
        boxes[box] = OrderedDict()

      boxes[box][label] = int(focal_length)

  total = 0
  for box in boxes.keys():
    for i, lens in enumerate(boxes[box].items()):
      curr = box + 1
      curr *= (i + 1) * lens[1]
      total += curr

  return total

print("Test 1")
assert part1(sample1) == 1320
print("Test 1 passed")

print("Test 2")
assert part2(sample1) == 145
print("Test 2 passed")

# print("Test 3")
# assert part2(sample1.split("\n")) == 400
# print("Test 3 passed")

# print("Test 4")
# assert part2(sample2.split("\n")) == 6
# print("Test 4 passed")

path = os.path.join(os.path.dirname(__file__), "../input/15.txt")
with open(path, "r") as f:
  L = list(f)[0]

  print("Begin Part 1:")
  assert part1(L) == 516469
  print("assert part1(L) == 516469 passed")

  print("Begin Part 2:")
  assert part2(L) == 221627
  print("assert part2(L) == 221627 passed")
