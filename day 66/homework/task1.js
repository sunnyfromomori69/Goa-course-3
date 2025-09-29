function checkOr() {
    let v1 = document.getElementById("val1").checked;
    let v2 = document.getElementById("val2").checked;
      let result = v1 || v2;
      document.getElementById("orOut").textContent = "Result: " + result;
  }