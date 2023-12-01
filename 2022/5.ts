import fs from 'fs';
import { log, test } from './helpers';

const parseCrates = (input: string): [string[], string[][]] => {
  const lines = input.split(/\r?\n/);
  const crates: string[] = [];
  let moves: string[][] = [];

  let parseMove = false;
  for (const line of lines) {

    // Row count line
    if (/^\d+$/.test(line.replaceAll(' ', ''))) {
      continue;
    }

    // Empty spacer line
    if (/^$/g.test(line)) {
      parseMove = true;
      continue;
    }

    if (parseMove) {
      const tempMoves = line.split(" ");
      moves.push([tempMoves[1], tempMoves[3], tempMoves[5]]);
    }
    else {
      crates.push(
        line.replaceAll(/\s{4}/g, '0')
          .replaceAll(/\[([A-Z]*)\] ?/g, '$1'));
    }
  }

  // Create stacks
  const crateStacks: string[][] = [];
  for (let i = 0; i < crates[0].length; i++) {
    crateStacks.push([]);
    for (let crate of crates) {
      if (crate === '0') continue;
      crateStacks[i].push(crate);
    }
  }

  log(crateStacks);
  log(moves);

  const columns: string[][] = [];
  for (const line of crates) {
    for (let i = 0; i < line.length; i += 4) {
      columns.push()
    }
  }

  return [crates, moves];
}

const shuffleCrates = (input: string): string[][] => {
  return[[""]]
}

const getTopCrates = (input: string): string => {
  const crates = parseCrates(input);

  return "";
}

const testData = `    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`;

test('test1', getTopCrates, testData, 'CMZ');

fs.readFile('2022/5.txt', 'utf8', (error, data) => {
  test('puzzle', getTopCrates, data, 'CMZ');
});

const countAnyOverlap = (input: string): number => {
  return 0;
}

test('test2', countAnyOverlap, testData, 4);

fs.readFile('2022/5.txt', 'utf8', (error, data) => {
  test('puzzle', countAnyOverlap, data, 911);
});