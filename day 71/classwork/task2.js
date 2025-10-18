function NumberInfo(number, even) {
    this.number = number;
    this.even = even;
  }
  let numbers = [];
  for (let i = 1; i <= 10; i++) {
    let isEven = i % 2 === 0;
    let obj = new NumberInfo(i, isEven);
    numbers.push(obj);
  }
  console.log(numbers);