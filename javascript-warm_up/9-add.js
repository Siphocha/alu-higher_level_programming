#!/usr/bin/node
//variable acting as function to add two integers

const add = (x, n) => {
    
    if (isNaN(x) || isNaN(n)){
      console.log('NaN');
    } else {
      console.log(x+n);
    }
};

add(parseInt(process.argv[2]), parseInt(process.argv[3]));

