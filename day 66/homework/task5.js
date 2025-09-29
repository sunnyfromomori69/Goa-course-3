function checkOrNum() {
    let a = Number(document.getElementById("valA").value);
    let b = Number(document.getElementById("valB").value);
      let result = (a < 5) || (b < 5);
      document.getElementById("orNumOut").textContent = "Result: " + result;
  }