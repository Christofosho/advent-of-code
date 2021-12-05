count = 0
with open("input.txt", "r") as f:
  F = f.readlines()
  X = [int(y) for y in F]

  V = X[0] + X[1] + X[2]
  for a, b, c in zip(X[1:], X[2:], X[3:]):
    L = a + b + c
    if L > V:
      count += 1
    V = L

print(count)