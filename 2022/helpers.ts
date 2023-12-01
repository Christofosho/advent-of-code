export const log = (...message: unknown[]): void => {
  console.log(...message);
};

export const assert = (check: boolean): void => {
  console.assert(check);
}

export const test = (name: string, func: Function, input: string, expected: string|number): void => {
  log(`Begin ${name}...`);
  const response = func(input);
  log(`Expected: ${expected} -- Response: ${response}`);

  assert(expected === response);
  log(`End ${name}.`);
}