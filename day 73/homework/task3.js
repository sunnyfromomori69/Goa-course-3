let time = 10;

let timer = setInterval(() => {
  console.log(time);
  time--;

  if (time < 0) {
    clearInterval(timer);
    console.log("Time up");
  }
}, 1000);