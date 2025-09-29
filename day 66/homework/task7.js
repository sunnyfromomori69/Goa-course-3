function checkEntry() {
    let hasTicket = document.getElementById("ticket").checked;
    let hasFriend = document.getElementById("friend").checked;
      if (hasTicket || hasFriend) {
      document.getElementById("entryOut").textContent = "შეგიძლიათ შესვლა";
    } else {
      document.getElementById("entryOut").textContent = "შესვლა აკრძალულია";
    }
  }