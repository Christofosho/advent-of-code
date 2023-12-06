import os
import math

sample = [
"seeds: 79 14 55 13",
"",
"seed-to-soil map:",
"50 98 2",
"52 50 48",
"",
"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",
"",
"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",
"",
"water-to-light map:",
"88 18 7",
"18 25 70",
"",
"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",
"",
"humidity-to-location map:",
"60 56 37",
"56 93 4"
]

def numeric(x):
  return x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def do(input, seeds):
  visited = [False] * len(seeds)

  for line in input[1:]:
    if len(line) == 0:
      continue

    elif not(numeric(line[0])):
      visited = [False] * len(seeds)

    else:
      dest, source, count = [int(n) for n in line.split(" ")]
      source2 = source + count
      for i, seed in enumerate(seeds):
        if seed >= source and seed < source2 and not visited[i]:
          seeds[i] -= (source - dest)
          visited[i] = True

  return min(seeds)

def part1(input):
  # First line is always seeds
  firstLine = input[0]
  valueString = firstLine.split(": ")[1]
  seeds = [int(s) for s in valueString.split(" ")]
  return do(input, seeds)

# def checkSeed(seed, input):
#   visited = False
#   for line in input[1:]:
#     if len(line) == 0:
#       continue

#     elif not(numeric(line[0])):
#       visited = False

#     else:
#       dest, source, count = [int(n) for n in line.split(" ")]
#       source2 = source + count
#       if seed >= source and seed < source2 and not visited:
#         seed -= (source - dest)
#         visited = True

#   return seed

# def partition(seed1, seed2):
#   seeds = [seed1, seed2]
#   visited = False
#   for line in input[1:]:
#     if len(line) == 0:
#       continue

#     elif not(numeric(line[0])):
#       continue

#     else:
#       dest, source, count = [int(n) for n in line.split(" ")]
#       source2 = source + count

#       if seed1 < source:
#         seeds.append(source)
#       elif seed1 < source2:
        

#       if seed2 >= source2:
#         seeds.append(source2)

# def part2(input):
#   # First line is seed, count, seed, count
#   firstLine = input[0]
#   valueString = firstLine.split(": ")[1]
#   seedAndCounts = [int(s) for s in valueString.split(" ")]
#   seed = math.inf
#   for i in range(0, len(seedAndCounts), 2):
#     seeds = partition(seedAndCounts[i], seedAndCounts[i] + seedAndCounts[i + 1])
#     for s in seeds:
#       seed = min(seed, checkSeed(s, input))
#   print(seed)
#   return seed

def part2(input):
  firstLine = input[0]
  valueString = firstLine.split(": ")[1]
  counts = [int(s) for s in valueString.split(" ")]
  seeds = [
    (counts[i], counts[i] + counts[i + 1])
    for i in range(0, len(counts), 2)
  ]

  chunks = []
  for line in input[1:]:
    if len(line) == 0:
      continue

    elif not numeric(line[0]):
      chunks.append([])

    else:
      chunks[-1].append([int(n) for n in line.split(" ")])

  for chunk in chunks:
    nextSeeds = []
    while seeds:
      start, end = seeds.pop()
      for dest, source, count in chunk:
        overlap1 = max(start, source)
        overlap2 = min(end, source + count)

        # Chunk is > 0 in size.
        if overlap1 < overlap2:
          nextSeeds.append((overlap1 - source + dest, overlap2 - source + dest))

          # Append to the original seeds to check and transform these chunks
          if overlap1 > start:
            seeds.append((start, overlap1))

          if end > overlap2:
            seeds.append((overlap2, end))

          # Transform matched, no need to continue on this seed.
          break

      # None of the transforms in the chunk matched our
      # current seeds, so add them back as they were.
      else:
        nextSeeds.append((start, end))

    seeds = nextSeeds

  return min(seeds)[0]

print("Test 1")
assert part1(sample) == 35
print("Test 1 passed")

print("Test 2")
assert part2(sample) == 46
print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/5.txt")
with open(path, "r") as f:
  L = [line.strip() for line in f.readlines()]

  print("Begin Part 1:")
  assert part1(L) == 331445006
  print("assert part1(L) == 331445006 passed")

  print("Begin Part 2:")
  assert part2(L) == 6472060
  print("assert part2(L) == 6472060 passed")