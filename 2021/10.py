# Advent of Code: Day 10

## Tests
def test():
  pass

def test2():
  pass

## Part 1
def part1(L):
  points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
  }
  matches = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
  }
  score = 0
  for row in L:
    current = ""
    for symbol in row:
      opposite = matches.get(symbol, False)
      if opposite and len(current) > 0:
        if current[-1] != opposite:
          score += points[symbol]
          break
        else:
          current = current[:len(current)-1]
      else:
        current += symbol
  return score
        


## Part 2
def part2(L):
  points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
  }
  matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
  }
  scores = []
  for i, row in enumerate(L):
    current = ""
    completion = ""
    scores.append(0)
    for symbol in row[::-1]:
      opposite = matches.get(symbol, False)
      if opposite:
        if len(current) > 0:
          current = current[:len(current)-1]
        else:
          scores[i] = scores[i] * 5 + points[opposite]
          completion += opposite
      else:
        current += symbol
  scores.sort()
  return scores[len(scores)//2 - 1]

with open("2021/input/10.txt", "r") as F:
  L = [list(x.rstrip()) for x in F.readlines()]

  #assert test() == 2
  assert part1(L) == 323691

  #assert test2() == 2
  assert part2(L) == 2858785164