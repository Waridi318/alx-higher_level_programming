#!/usr/bin/node

const isnumber = parseInt(process.argv[2]);

if (isNaN(isnumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${process.argv[2]}`);
}
