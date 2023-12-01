import os

def numeric(x):
  return x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

d = {
  "0": 0,
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def str_to_num(x):
  return d[x]

def part1(L):
  nums = []
  for word in L:
    s = 0
    e = len(word) - 1
    while s <= e:
      if numeric(word[s]) and numeric(word[e]):
        nums.append(str(word[s]) + str(word[e]))
        break
      else:
        if not numeric(word[s]):
          s += 1
        if not numeric(word[e]):
          e -= 1

  return sum(map(int, nums))

def findNumber(word):
  found = []
  found2 = []
  for key in d.keys():
    try:
      i = word.index(key)
      if i > -1:
        found.append((d[key], i))

      j = word.rfind(key)
      if j > -1:
        found2.append((d[key], j))
    except:
      pass

  s = min(found, key=lambda x: x[1])[0]
  e = max(found2, key=lambda x: x[1])[0]

  return int(str(s) + str(e))

def part2(L):
  nums = []
  for word in L:
    nums.append(findNumber(word))
  return sum(nums)

print("Test 1")
assert part1(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 142
print("Test 1 passed")

print("Test 2")
assert part2(["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]) == 281
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/1.txt")
with open(path, "r") as f:
  F = f.readlines()
  L = [y.strip() for y in F]

  print("Part 1")
  assert part1(L) == 55002
  print("Part 1 passed")

  print("Part 2")
  assert part2(L) == 55093