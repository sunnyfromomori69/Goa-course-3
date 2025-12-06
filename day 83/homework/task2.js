
const mySet = new Set([1, 2, 2, 3, 3, 4]);
console.log(mySet); 
mySet.add(5);
mySet.delete(2);
console.log("Final size:", mySet.size);
console.log("Final set:", mySet);
