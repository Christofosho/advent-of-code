import os
from collections import deque

sample1 = [
"px{a<2006:qkq,m>2090:A,rfg}",
"pv{a>1716:R,A}",
"lnx{m>1548:A,A}",
"rfg{s<537:gd,x>2440:R,A}",
"qs{s>3448:A,lnx}",
"qkq{x<1416:A,crn}",
"crn{x>2662:A,R}",
"in{s<1351:px,qqz}",
"qqz{s>2770:qs,m<1801:hdj,R}",
"gd{a>3333:R,R}",
"hdj{m>838:A,pv}",
"",
"{x=787,m=2655,a=1222,s=2876}",
"{x=1679,m=44,a=2067,s=496}",
"{x=2036,m=264,a=79,s=2244}",
"{x=2461,m=1339,a=466,s=291}",
"{x=2127,m=1623,a=2188,s=1013}",
]

workflows = {}
def workflowParser(line):
  name, rules = line.split("{")
  rules = rules.rstrip("}").split(",")
  final = rules.pop()
  parsedRules = []
  for rule in rules:
    parsedRules.append(tuple(rule.split(":")))

  parsedRules.append((None, final))

  workflows[name] = tuple(parsedRules)

def parse(L):
  # Groom the input
  parseWorkflow = True
  ratings = []
  for line in L:
    line = line.strip("\n")
    if line == "":
      parseWorkflow = False
      continue

    if parseWorkflow:
      workflowParser(line)

    else:
      line = line.lstrip("{")
      line = line.rstrip("}")
      ratings.append({})
      for rating in line.split(","):
        k, v = rating.split("=")
        ratings[-1][k] = v

  return ratings

def walktheGauntlet(rating, workflows):
    workflow = workflows["in"]

    working = True
    while working:

      nextWorkflow = None
      for rule in workflow:
        if rule[0] is None:
          if rule[1] == "A":
            nextWorkflow = "A"
            break

          if rule[1] == "R":
            nextWorkflow = "R"
            return 0

          nextWorkflow = rule[1]
          break

        else:
          category = rating[rule[0][0]]

          if rule[0][1] == ">" and int(category) > int(rule[0][2:]):
            nextWorkflow = rule[1]
            break

          elif rule[0][1] == "<" and int(category) < int(rule[0][2:]):
            nextWorkflow = rule[1]
            break

      if not nextWorkflow or nextWorkflow == "R":
        return 0

      if nextWorkflow == "A":
        return sum(map(int, rating.values()))

      workflow = workflows[nextWorkflow]


def part1(ratings):
  # Walk the gauntlet
  total = 0
  while ratings:
    rating = ratings.pop()
    total += walktheGauntlet(rating, workflows)

  return total

def pick(name, ratings):
  if name == "R":
    return 0

  elif name == "A":
    total = 1
    for low, high in ratings.values():
      total *= high - low + 1
    return total

  rules = workflows[name]

  total = 0
  for rule, step in rules:
    if rule == None:
      total += pick(step, ratings)
      break

    low, high = ratings[rule[0]]
    compare = int(rule[2:])
    if rule[1] == "<":
      valid = (low, compare - 1)
      invalid = (compare, high)
    else:
      valid = (compare + 1, high)
      invalid = (low, compare)

    # Check for valid valid  >o<
    if valid[0] <= valid[1]:
      modify = dict(ratings)
      modify[rule[0]] = valid
      total += pick(step, modify)

    if invalid[0] <= invalid[1]:
      ratings = dict(ratings)
      ratings[rule[0]] = invalid
    else:
      break

  return total

def part2(L):
  for line in L:
    line = line.strip("\n")
    if line == "":
      break

    workflowParser(line)

  total = pick("in", { category: (1, 4000) for category in "xmas" })
  return total

print("Test 1")
assert part1(parse(sample1)) == 19114
print("Test 1 passed")

print("Test 2")
assert part2(sample1[:11]) == 167409079868000
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/19.txt")
with open(path, "r") as f:
  L = list(f)

  print("Begin Part 1:")
  assert part1(parse(L)) == 362930
  print("assert part1(L) == 362930 passed")

  print("Begin Part 2:")
  assert part2(L) == 116365820987729
  print("assert part2(L) == 116365820987729 passed")
