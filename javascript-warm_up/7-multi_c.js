#!/usr/bin/node
const x = parseInt(process.argv[2]);
//constant num is a command line argument
if (isNan(x)){
    console.log("Missing number of occurrences");
}
else{
    for(let i =0; i < x; i++){
        //if number/argument is present print it this many times.
        console.log("C is fun");
    }
}