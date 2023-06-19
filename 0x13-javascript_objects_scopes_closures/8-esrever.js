#!/usr/bin/node

exports.esrever = function (list) {
  let j = list.length - 1;
  const newList = [];

  while (j >= 0) {
    newList.push(list[j]);
    j--;
  }

  return (newList);
};
