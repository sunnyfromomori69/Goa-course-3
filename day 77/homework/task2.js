const form = document.getElementById("taskForm");
const input = document.getElementById("taskInput");
const list = document.getElementById("taskList");

form.addEventListener("submit", function(e) {
    e.preventDefault(); 
    const taskText = input.value.trim();
    if (taskText === "") return;

    const li = document.createElement("li");
    li.textContent = taskText;

    const btn = document.createElement("button");
    btn.textContent = "შესრულებულია";
    btn.style.marginLeft = "10px";
    li.appendChild(btn);
    list.appendChild(li);
    input.value = "";
    btn.addEventListener("lick", function() {
        const parentLi = btn.parentElement;   
        parentLi.style.textDecoration = "line-through"; 
    });
});