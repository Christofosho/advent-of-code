# Advent of Code: Day 8

## Helpers
def is147or8(output):
  return len(output) in (2, 3, 4, 7)

## Part 1
def part1(L):
  total = sum(
    len([
      o for o in output if is147or8(o)
    ])
    for output in L
  )
  return total

## Part 2
def part2(A, B):
  known = []
  for a in A:
    current = [None] * 10

    # Set our known values
    current[8] = a.pop(9)
    current[4] = a.pop(2)
    current[7] = a.pop(1)
    current[1] = a.pop(0)

    ## Educated guesses

    # 9 -> if 4 in 9
    current[9] = [x for x in a if set(current[4]) <= set(x)][0]
    a.pop(a.index(current[9]))

    # 0 -> if len == 6 and 7 in 0
    current[0] = [x for x in a if len(x) == 6 and set(current[7]) <= set(x)][0]
    a.pop(a.index(current[0]))

    # 6 -> len == 6
    current[6] = [x for x in a if len(x) == 6][0]
    a.pop(a.index(current[6]))

    # 3 -> 7 in 3
    current[3] = [x for x in a if set(current[7]) <= set(x)][0]
    a.pop(a.index(current[3]))

    # 5 -> in 9
    current[5] = [x for x in a if set(x) <= set(current[9])][0]
    a.pop(a.index(current[5]))

    # 2
    current[2] = a[0]

    known.append(current)

  sets = 0
  for i, b in enumerate(B):
    n = ""
    for output in b:
      n += str(known[i].index(output))

    sets += int(n)

  return sets

with open("2021/input/8.txt", "r") as F:
  L = [x.rstrip().split(' | ') for x in F.readlines()]
  A = [
    sorted([''.join(sorted(aa)) for aa in a[0].split()], key=len)
    for a in L
  ]

  B = [
    [''.join(sorted(bb)) for bb in b[1].split()]
    for b in L
  ]

  assert part1(B) == 416
  assert part2(A, B) == 1043697