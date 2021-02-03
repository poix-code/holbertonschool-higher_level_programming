#!/usr/bin/node
exports.callMeMoby = function (x, xtimes) {
  for (let i = 0; i < x; i++) {
    xtimes();
  }
};