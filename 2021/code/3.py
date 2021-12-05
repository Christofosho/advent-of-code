def part1():
  with open("input3.txt", 'r') as F:
    L = [x.strip() for x in F.readlines()]
    bits = len(L[0])

    quantity = len(L) // 2
    counts = [0] * bits

    for item in L:
      for index, char in enumerate(item):
        counts[index] += int(char)

    gamma = ""
    for count in counts:
      gamma += "1" if count > quantity else "0"

    return int(gamma, 2) * (int(gamma, 2) ^ 0xFFF)

def part2():
  with open("input3.txt", "r") as F:
    # Strip the lines and count them
    L = [x.strip() for x in F.readlines()]
    bits = len(L[0])

    gamma = ""
    epsilon = ""
    A = list(L)
    B = list(L)
    for i in range(bits):

      # Grab the halfway point and initialize a list of 0s
      # for counting the 1s
      quantityA = len(A) / 2
      quantityB = len(B) / 2
      countA = 00000000000000
      countB = 00000000000000

      # Gotta improve this.. count the 1s
      for item in A:
        countA += int(item[i])

      for item in B:
        countB += int(item[i])

      # Form the string
      gamma = "1" if countA >= quantityA else "0"
      epsilon = "1" if countB < quantityB else "0"

      if len(A) > 1:
        A = [item for item in A if item[i] == gamma]
      if len(B) > 1:
        B = [item for item in B if item[i] == epsilon]

    return int(A[0], 2) * int(B[0], 2)

assert part1() == 2250414

assert part2() == 6085575