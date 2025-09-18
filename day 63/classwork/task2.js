let heading = document.getElementById("hallo"); 
let input = document.getElementById("name!");  
let button = document.getElementById("submit"); 

button.addEventListener("click", function() {
  let userName = input.value;

  heading.textContent = "Hello " + userName;
});
