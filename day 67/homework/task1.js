function checkData() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (name === "" || email === "" || password === "") {
      alert("Please enter all information!");
    } else {
      alert("Data submitted successfully!");
    }
  }