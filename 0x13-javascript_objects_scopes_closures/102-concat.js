#!/usr/bin/node

const fs = require('fs');

// const fileB = require('fileB');
// const fileC = require('fileC');
function concatFiles (fileA, fileB, fileC) {
  const content1 = fs.readFileSync(fileA, 'utf-8');
  const content2 = fs.readFileSync(fileB, 'utf-8');
  const concatContent = content1 + content2;
  fs.writeFileSync(fileC, concatContent);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

concatFiles(fileA, fileB, fileC);
