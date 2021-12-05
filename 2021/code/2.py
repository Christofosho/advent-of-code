
with open('input2.txt') as F:
  L = F.readlines()

  H = 0
  D = 0
  A = 0
  for line in L:
    dir, q = line.split(" ")

    if dir == "forward":
      H += int(q)
      D += A * int(q)

    elif dir == "down":
      A += int(q)

    elif dir == "up":
      A -= int(q)

  print(H*D)
