#!/usr/bin/node
const args = process.argv.length;
const num = [];
switch (args) {
  case 2:
  case 3:
    console.log(0);
    break;

  default:
    for (let i = 2; i < args; i++) {
      num.push(process.argv[i]);
    }
    num.sort((a, b) => b - a);
    console.log(num[1]);
    break;
}
