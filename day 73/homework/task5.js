let time = 0;

let interval = setInterval(() => {
  time++;
  console.log("Current minutes: " + time);
  if (time === 34) {
    console.log("Time up");
  }
}, 60000);