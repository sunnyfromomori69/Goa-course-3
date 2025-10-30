const button = document.getElementById("generateBtn");

button.addEventListener("click", () => {
  const randomNumber = Math.floor(Math.random() * 1001);
  const p = document.createElement("p");
  p.textContent = randomNumber;
  document.body.appendChild(p);
});
