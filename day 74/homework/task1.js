const addItemForm = document.getElementById('addItemForm');
const cartTableBody = document.querySelector('#cartTable tbody');
const totalPriceEl = document.getElementById('totalPrice');
let cart = [];
function updateCart() {
  cartTableBody.innerHTML = ''; 
  let total = 0;
  cart.forEach((item, index) => {
    const row = document.createElement('tr');
    const totalItem = item.price * item.quantity;
    total += totalItem;
    row.innerHTML = `
      <td>${item.name}</td>
      <td>$${item.price.toFixed(2)}</td>
      <td><input type="number" min="1" value="${item.quantity}" data-index="${index}" class="quantity-input"></td>
      <td>$${totalItem.toFixed(2)}</td>
      <td><button class="remove-btn" data-index="${index}">Remove</button></td>
    `;
    cartTableBody.appendChild(row);
  });
  if(total > 100) {
    total = total * 0.9; 
  }
  totalPriceEl.textContent = `Total: $${total.toFixed(2)}`;
  document.querySelectorAll('.remove-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const index = e.target.getAttribute('data-index');
      cart.splice(index, 1);
      updateCart();
    });
  });
  document.querySelectorAll('.quantity-input').forEach(input => {
    input.addEventListener('change', (e) => {
      const index = e.target.getAttribute('data-index');
      const value = parseInt(e.target.value);
      if(value > 0) {
        cart[index].quantity = value;
        updateCart();
      }
    });
  });
}
addItemForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('itemName').value.trim();
  const price = parseFloat(document.getElementById('itemPrice').value);
  const quantity = parseInt(document.getElementById('itemQuantity').value);

  if(name && price > 0 && quantity > 0) {
    cart.push({ name, price, quantity });
    updateCart();
    addItemForm.reset();
  }
});