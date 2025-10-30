const input = document.getElementById("noteInput");
    const addBtn = document.getElementById("addBtn");
    const notesList = document.getElementById("notesList");

    addBtn.addEventListener("click", () => {
      const noteText = input.value.trim();
      if (noteText === "") return;

      const li = document.createElement("li");
      li.textContent = noteText;

      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "Delete";
      deleteBtn.addEventListener("click", () => {
        li.remove();
      });

      li.appendChild(deleteBtn);
      notesList.appendChild(li);

      input.value = "";
    });