import fs from 'fs';
import { log, test } from './helpers';

const getSacks = (L: string): string[] => {
  return L.split(/\r?\n/);
}

const parseSacks = (L: string): string[][] => {
  const toSplit: string[] = getSacks(L);
  return toSplit.map(v => [v.substring(0, Math.floor(v.length / 2)), v.substring(Math.floor(v.length / 2))])
}

const getPriority = (c: string): number => c.charCodeAt(0) > 96 ? c.charCodeAt(0) - 96 : c.charCodeAt(0) - 38;

const getPrioritySum = (L: string) => {
  const sacks = parseSacks(L);
  let total = 0;
  sacks.forEach(sack => {
    const sackExists: {[key: string]: boolean} = {};
    const left: string = sack[0];
    const right: string = sack[1];
    left.split('').forEach(c => { sackExists[c] = true });
    let chosen: string = '';
    for (chosen of right) {
      if (sackExists[chosen]) {
        break;
      }
    }
    total += getPriority(chosen);
  });
  return total;
}

const testData = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`;

test('test1', getPrioritySum, testData, 157);

fs.readFile('2022/3.txt', 'utf8', (error, data) => {
  test('puzzle', getPrioritySum, data, 7863);
});

const getBadges = (L: string) => {
  const sacks = getSacks(L);
  let total = 0;
  for (let i = 0; i < sacks.length; i += 3) {
    const sackExists: {[key: string]: boolean} = {};
    const twoSacks:  {[key: string]: boolean} = {};

    // Loop through first sack and add.
    for (const item of sacks[i]) {
      sackExists[item] = true;
    }

    // Loop through second sack
    for (const item of sacks[i + 1]) {
      if (sackExists[item]) {
        twoSacks[item] = true;
      }
    }

    // Loop through third sack
    let chosen: string = '';
    for (chosen of sacks[i + 2]) {
      if (twoSacks[chosen]) {
        break;
      }
    }
    total += getPriority(chosen);
  }
  return total;
}

test('test2', getBadges, testData, 70);

fs.readFile('2022/3.txt', 'utf8', (error, data) => {
  test('puzzle2', getBadges, data, 2488);
});