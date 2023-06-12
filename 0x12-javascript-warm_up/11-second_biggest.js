#!/usr/bin/node

const array = process.argv.slice(2).map(Number);

const n = array.length;
let i;
let j;
if (n <= 1) {
  console.log('0');
} else {
  for (i = 0; i < n - 1; i++) {
    for (j = 0; j < (n - 1 - i); j++) {
      if (array[j] > array[j + 1]) {
        const n = array[j];
        array[j] = array[j + 1];
        array[j + 1] = n;
      }
    }
  }
  function checkLastDigit (array) {
    while (i >= 1 && array[i] === array[i - 1]) {
      i--;
    }
    return array[i - 1];
  }
  console.log(checkLastDigit(array));
}
