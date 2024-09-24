#!/usr/bin/node
function Concat () {
  if ((process.argv).length === 2) {
    console.log('undefined is undefined');
  } else if ((process.argv).lenght === 3) {
    console.log(process.argv[2], 'is undefined');
  } else {
    console.log(process.argv[2], 'is', process.argv[3]);
  }
}
Concat();
