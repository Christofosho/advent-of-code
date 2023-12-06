# Advent of Code: Day 14

## Tests
def test1():
  L = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
  ]
  template = list(L[0])
  assert solve(template, [rule.split(" -> ") for rule in L[2:]], 10) == 1588

def test2():
  L = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
  ]
  template = list(L[0])
  assert solve(template, [rule.split(" -> ") for rule in L[2:]], 40) == 2188189693529

## helper
def solve(template, rules, steps):
  pairs = {}
  counts = {}

  ruleToOutput = {}
  for rule in rules:
    pair = rule[0]
    letter = rule[1]
    counts[letter] = 0

    # ex: [CN, [CC, CN]]
    ruleToOutput[pair] = [pair[0] + letter, letter + pair[1]]

  # Initial counts
  for c in template:
    counts[c] = counts.get(c, 0) + 1

  # Initial rule counts
  for rule in zip(template, template[1:]):
    pairs[rule[0] + rule[1]] = pairs.get(rule[0] + rule[1], 0) + 1

  for i in range(steps):
    toRemove = {}
    nextPairs = {}
    for match, output in ruleToOutput.items():
      pair = pairs.get(match, 0)

      # We have the pair in our sequence, so "insert between"
      if pair > 0:
        nextPairs[output[0]] = nextPairs.get(output[0], 0) + pair
        nextPairs[output[1]] = nextPairs.get(output[1], 0) + pair

        # Remove our old pair, because we have put one between it
        toRemove[match] = pair

        # Count out how many of the letter we have added
        counts[output[0][1]] += pair
    
    for rule, count in toRemove.items():
      pairs[rule] = pairs.get(rule, 0) - count

    for rule, count in nextPairs.items():
      pairs[rule] = pairs.get(rule, 0) + count

  return max(counts.values()) - min(counts.values())

#test1()
#test2()

with open("2021/input/14.txt", "r") as F:
  L = [line.rstrip() for line in F.readlines()]
  template = list(L[0])
  assert solve(template[:], [rule.split(" -> ") for rule in L[2:]], 10) == 2068
  assert solve(template[:], [rule.split(" -> ") for rule in L[2:]], 40) == 2158894777814