#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const n = number + 1;
  theFunction(n);
};