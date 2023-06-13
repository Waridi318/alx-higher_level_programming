#!/usr/bin/node

exports.esrever = function (list) {
  let j = 0;
  while (j < list.length - 1) {
    j++;
  }
  const newList = [];
  while (j > -1) {
    newList.push(list[j]);
    j--;
  }
  list = newList;
  return (list);
};
