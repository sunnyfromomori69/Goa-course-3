
const numSet = new Set([1, 2, 2, 3, 4, 4, 5, 6]);
let acc = 0;
for (const num of numSet) {
  acc += num;
}
console.log("Sum of unique numbers:", acc);