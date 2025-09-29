function checkAnd() {
let n1 = Number(document.getElementById("num1").value);
  let n2 = Number(document.getElementById("num2").value);

  let result = (n1 > 10) && (n2 > 10);

  document.getElementById("andOut").textContent = "Result: " + result;
}