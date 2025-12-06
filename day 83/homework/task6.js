let weatherIsGood = true; 
const checkWeather = new Promise((resolve, reject) => {
  setTimeout(() => {
    if (weatherIsGood) {
      resolve("ამინდი კარგია — გასეირნება შემიძლია 😊");
    } else {
      reject("ამინდი ცუდია — ვერ გავდივარ 🌧️");
    }
  }, 2000);
});
checkWeather
  .then(result => console.log(result))
  .catch(error => console.log(error));