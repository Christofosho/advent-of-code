import fs from 'fs';
import { log, test } from './helpers';

const worth: Record<string, number> = {
  "X": 1,
  "Y": 2,
  "Z": 3,
} as const;

const win: Record<string, string> = {
  A: "Y",
  B: "Z",
  C: "X",
} as const;

const draw: Record<string, string> = {
  A: "X",
  B: "Y",
  C: "Z",
} as const;

const lose: Record<string, string> = {
  A: "Z",
  B: "X",
  C: "Y",
} as const;

const parseRounds = (input: string): string[][] => {
  return input.split(/\r?\n/).map(i => i.split(' '));
}

const getTotalScore1 = (input: string): number => {
  const rounds = parseRounds(input);
  let total = 0;
  rounds.forEach(round => {
    const opponent = round[0];
    const us = round[1];

    // Calculate choice score
    total += worth[us];

    // Calculate round score
    if (win[opponent] === us) {
      total += 6;
    }
    else if (draw[opponent] === us) {
      total += 3;
    }
  });

  return total;
};

const testData = `A Y
B X
C Z`;

test('test1', getTotalScore1, testData, 15);

fs.readFile('2022/2.txt', 'utf8', (error, data) => {
  test('puzzle', getTotalScore1, data, 12679);
});

const getTotalScore2 = (input: string): number => {
  const rounds = parseRounds(input);
  let total = 0;
  rounds.forEach(round => {
    const opponent = round[0];
    const wanted = round[1];

    // Calculate round score
    if (wanted === "X") {
      // Lose
      total += worth[lose[opponent]];
    }
    else if (wanted === "Y") {
      // Draw
      total += 3;
      total += worth[draw[opponent]];
    }
    else {
      total += 6;
      total += worth[win[opponent]];
    }
  });

  return total;
};

test('test2', getTotalScore2, testData, 12);

fs.readFile('2022/2.txt', 'utf8', (error, data) => {
  test('puzzle2', getTotalScore2, data, 14470);
});