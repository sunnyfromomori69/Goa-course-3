function checkAge() {
    let age = Number(document.getElementById("ageInput").value);
      if (age >= 13 && age <= 17) {
      document.getElementById("ageOut").textContent = "Teenager";
    } else {
      document.getElementById("ageOut").textContent = "Not Teenager";
    }
  }