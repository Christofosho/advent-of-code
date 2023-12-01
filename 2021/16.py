# Advent of Code: Day 16

## Tests
def test1():
  assert part1("8A004A801A8002F478") == 16

def test2():
  assert part1("620080001611562C8802118E34") == 12

def test3():
  assert part1("C0015000016115A2E0802F182340") == 23

def test4():
  assert part1("A0016C880162017C3686B18A3D4780") == 31

def decode_packet(packet):
  version_total = 0

  pointer = 0

  version_total += int(packet[pointer:pointer+3], 2)
  type_id = packet[pointer+3:pointer+6]
  pointer += 6

  # Literal packet
  if type_id == "100": # 4
      group = ""
      while True:
        pointer += 5 # Always update pointer even if breaking
        group += packet[pointer-4:pointer]
        if packet[pointer-5] == "0":
          break

  # Operator packet
  elif type_id in ("000", "011", "110"):

    # Decode each subpacket
    while pointer < len(packet):
      length_type = 18 if packet[pointer] == "1" else 22
      subpacket_length = packet[pointer+1:pointer+length_type]
      pointer += length_type
      version_total += decode_packet(packet[pointer:pointer+subpacket_length])

  print(version_total)
  return version_total

## Part 1
def part1(hex_packet):
  packet = ''.join([
    format(int(hex_char, 16), "04b")
    for hex_char in hex_packet
  ])
  decode_packet(packet)


test1()
test2()

def part2(cave):
  pass

#test2()

with open("2021/input/16.txt", "r") as F:
  L = F.readlines().rstrip()
  assert part1(L[:]) == 0
  #assert part2(L[:]) == 0