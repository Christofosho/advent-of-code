import fs from 'fs';
import { log, test } from './helpers';

const countElves = (input: string): number[] => {
  const inputList = input.split(/\r?\n/);
  const elves: number[] = [0];
  inputList.forEach(v => {
    if (v === "") {
      elves.push(0);
    }
    elves[elves.length - 1] += Number(v);
  });
  return elves;
}

const findHighestQuantity = (input: string): number => {
  const elves = countElves(input);
  return Math.max(...elves);
}

const sumThreeHighest = (input: string): number => {
  const elves = countElves(input);
  elves.sort((a: number, b: number): number => b - a);
  return elves[0] + elves[1] + elves[2];
}


const testData: string = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`;

test('test1', findHighestQuantity, testData, 24000);

fs.readFile('2022/1.txt', 'utf8', (error, data) => {
  test('puzzle1', findHighestQuantity, data, 66306);
});

test('test2', sumThreeHighest, testData, 45000);

fs.readFile('2022/1.txt', 'utf8', (error, data) => {
  test('puzzle2', sumThreeHighest, data, 195292);
});