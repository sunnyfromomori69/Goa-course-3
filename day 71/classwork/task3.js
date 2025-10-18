let numbers = [10, 20, 30, 40, 50];
// pop removes the last element
numbers.pop(); 
console.log(numbers);
// shift removes the first element
numbers.shift(); 
console.log(numbers); 
// unshift adds elements at the start
numbers.unshift(5); 
console.log(numbers); 
// slice slices or well copies  a part of the array 
let part = numbers.slice(1, 3); 
console.log(part); 
// splice removes or adds elements 
console.log(numbers); 
numbers.splice(2, 1, 35); 
// indexOf finds the first index of a value
let index = numbers.indexOf(20);
console.log(index); 
// lastIndexOf finds the last index of a value 
numbers.push(20);
let lastIndex = numbers.lastIndexOf(20);
console.log(lastIndex); 
// includes checks if a value exists in the array
let has30 = numbers.includes(30);
console.log(has30);
// find returns the first element that matches a condition
let found = numbers.find(num => num > 25);
console.log(found); 
// findIndex returns the index of the first element that matches a condition
let foundIndex = numbers.findIndex(num => num > 25);
console.log(foundIndex); 