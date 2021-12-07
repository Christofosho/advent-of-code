# Advent of Code: Day 6
## There is probably a more math-centric solution
## to this problem..

## Constants
adult = 7
baby = 9
mama = 0

## Part 1
def worse(fish, days):
  for d in range(0, days):
    babies = []
    for i, f in enumerate(fish[:]):
      if f == 0:
          fish[i] = adult
          babies.append(baby)
      else:
        fish[i] -= 1

    fish.extend(babies)

  return len(fish)

## Part 2
def better(fish, days):
  d = [0] * 10
  for f in fish:
    d[f] += 1

  for _ in range(0, days):
    for age_of_fish, quantity in enumerate(d):
      if age_of_fish == 0:
        d[adult] += d[mama]
        d[baby] += d[mama]
        d[mama] -= d[mama]
      else:
        d[age_of_fish-1] += quantity
        d[age_of_fish] -= quantity

  return sum(d)

with open("2021/input/6.txt", "r") as F:
  L = [int(x) for x in F.readlines()[0].split(",")]

  assert better(L[:], 80) == 361169
  assert better(L[:], 256) == 1634946868992