import os
from collections import deque

sample1 = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

sample2 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''

DEAD = -1
FF = 0
CNJ = 1

q = deque()
nodes = {}
counts = [0, 0]

class ff:
  kind = FF
  def __init__(self, name):
    self.name = name
    self.on = False
    self.out = []

  def add(self, out):
    self.out.append(out)

  def act(self, _in, pulse):
    if pulse == False:
      self.on = not self.on
      self.send()

  def send(self):
    for o in self.out:
      q.appendleft((o, self.name, self.on))
      counts[self.on] += 1

class cnj:
  kind = CNJ

  def __init__(self, name):
    self.name = name
    self.out = []
    self.inp = {}

  def add(self, out):
    self.out.append(out)

  def feed(self, _in):
    self.inp[_in] = False

  def act(self, _in, pulse):
    self.inp[_in] = pulse
    if len(self.inp) == sum(self.inp.values()):
      self.send(False)

    else:
      self.send(True)

  def send(self, pulse):
    for o in self.out:
      q.appendleft((o, self.name, pulse))
      counts[pulse] += 1

class dead:
  kind = DEAD

  def __init__(self, name):
    self.name = name

  def add(self, out):
    pass

  def act(self, _in, pulse):
    if pulse == False and self.name == "rx":
      print("rx")

  def send(self):
    pass

def part1(L, press = 1000):
  counts[0] = 0
  counts[1] = 0
  nodes.clear()
  instructions = L.split("\n")

  # Parse instructions, separating out the broadcaster.
  broadcaster = None
  for i in instructions:
    _in, _out = i.split(" -> ")
    if _in == "broadcaster":
      broadcaster = _out.split(", ")
      continue

    if _in[0] == "%":
      nodes[_in[1:]] = ff(_in[1:])
    elif _in[0] == "&":
      nodes[_in[1:]] = cnj(_in[1:])

  for i in instructions:
    _in, _out = i.split(" -> ")
    if _in == "broadcaster":
      continue

    _in = _in[1:]
    _out = _out.split(", ")

    for o in _out:
      if o not in nodes:
        nodes[o] = dead(o)

      nodes[_in].add(nodes[o])
      if nodes[o].kind == CNJ:
        nodes[o].feed(_in)

  for i in range(press):
    counts[False] += 1
    q.extendleft([(nodes[n], "broadcaster", False) for n in broadcaster[::-1]])

    counts[False] += len(broadcaster)
    while q:
      node, name, pulse = q.pop()
      node.act(name, pulse)

  print(counts[0] * counts[1])
  return counts[0] * counts[1]

def part2(L):
  pass

print("Test 1")
assert part1(sample1) == 32000000
print("Test 1 passed")

print("Test 2")
assert part1(sample2) == 11687500
print("Test 2 passed")

path = os.path.join(os.path.dirname(__file__), "../input/20.txt")
with open(path, "r") as f:
  L = f.read()

  print("Begin Part 1:")
  assert part1(L) == 896998430
  print("assert part1(L) == 896998430 passed")

  print("Begin Part 2:")
  assert part1(L, 10000000) == 0
  print("assert part2(L) == 0 passed")
