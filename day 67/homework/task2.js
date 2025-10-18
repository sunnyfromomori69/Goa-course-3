function validateForm() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirm = document.getElementById("confirm").value;

    if (name === "" || email === "" || password === "" || confirm === "") {
      alert("Please fill in all fields!");
      return;
    }

    if (password.length < 8) {
      alert("Password must be at least 8 characters long!");
      return;
    }


    if (password !== confirm) {
      alert("Passwords do not match!");
      return;
    }


    if (!email.includes("@") || !email.includes(".")) {
      alert("Please enter a valid email address!");
      return;
    }

    alert("Registration successful!");
    document.getElementById("message").innerText = "Welcome, " + name + "!";
  }