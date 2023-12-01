import fs from 'fs';
import { log, test } from './helpers';

const parsePairs = (input: string): string[] => {
  return input.split(/\r?\n/);
}

const parsePairRanges = (input: string): number[][][] => {
  const pairs = parsePairs(input);
  return pairs
    .map(pair => pair
      .split(',')
      .map(range => range
        .split('-')
        .map(i => Number(i))));
}

const countFullOverlap = (input: string): number => {
  const pairRanges = parsePairRanges(input);
  let totalFullOverlaps = 0;
  pairRanges.forEach(pair => {
    if ((pair[0][0] >= pair[1][0] && pair[0][1] <= pair[1][1])
      || (pair[1][0] >= pair[0][0] && pair[1][1] <= pair[0][1])) {
      totalFullOverlaps++;
    }
  });

  return totalFullOverlaps;
};

const testData = `2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`;

test('test1', countFullOverlap, testData, 2);

fs.readFile('2022/4.txt', 'utf8', (error, data) => {
  test('puzzle', countFullOverlap, data, 588);
});

const countAnyOverlap = (input: string): number => {
  const pairRanges = parsePairRanges(input);
  let totalOverlaps = 0;
  pairRanges.forEach(pair => {
    if ((pair[0][1] >= pair[1][0] && pair[0][1] <= pair[1][1])
      || pair[1][1] >= pair[0][0] && pair[1][1] <= pair[0][1]) {
        totalOverlaps++;
      }
  });
  return totalOverlaps;
}

test('test2', countAnyOverlap, testData, 4);

fs.readFile('2022/4.txt', 'utf8', (error, data) => {
  test('puzzle', countAnyOverlap, data, 911);
});