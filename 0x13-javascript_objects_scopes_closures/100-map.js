#!/usr/bin/node

const list = require('./100-data.js').list;

let i = -1;
const newList = list.map(function (num) {
  i++;
  return num * i;
});
console.log(list);
console.log(newList);
