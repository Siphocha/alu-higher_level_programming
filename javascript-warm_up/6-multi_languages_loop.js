#!/usr/bin/node
//Defines 3 strings in array that will be iteravely displayed by for loop.
const sentences = ["C is fun", "Python is cool", "JavaScript is amazing"];

//loops through array to print each one, one line down from previous
for(let x = 0; x < sentences.length; x++){
    console.log(sentences[x]);
}