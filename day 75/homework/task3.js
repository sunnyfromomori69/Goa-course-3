function containerFunction(event) {
    event.preventDefault(); 
  
    const name = document.getElementById("fullName").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
  
    const tr = document.createElement("tr");
  
    const tdName = document.createElement("td");
    tdName.textContent = name;
    const tdEmail = document.createElement("td");
    tdEmail.textContent = email;
  
    const tdPhone = document.createElement("td");
    tdPhone.textContent = phone;
   
    tr.appendChild(tdName);
    tr.appendChild(tdEmail);
    tr.appendChild(tdPhone);
  
    presentationalFunction(tr);
  
    document.getElementById("userForm").reset();
  }
  function presentationalFunction(row) {
    const tableBody = document.querySelector("#userTable tbody");
    tableBody.appendChild(row);
  }
  document.getElementById("userForm").addEventListener("submit", containerFunction);