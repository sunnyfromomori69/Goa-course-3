function checkNot() {
    let val = document.getElementById("notVal").checked;
      let result = !val;
      document.getElementById("notOut").textContent = "Result: " + result;
  }