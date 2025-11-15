const input = document.getElementById("searchInput");
const btn = document.getElementById("searchBtn");
const list = document.getElementById("itemList");
const items = list.getElementsByTagName("li");
btn.addEventListener("click", function() {
    const searchText = input.value.toLowerCase(); 
    for (let i = 0; i < items.length; i++) {
        const itemText = items[i].textContent.toLowerCase();

        if (itemText.includes(searchText)) {
            items[i].style.display = "list-item"; 
        } else {
            items[i].style.display = "none"; 
        }
    }
});
