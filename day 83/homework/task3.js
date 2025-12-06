const productPrices = new Map([
    ["Bread", 2.5],
    ["Milk", 3],
    ["Eggs", 4.2],
    ["Juice", 5],
  ]);
  for (const [product, price] of productPrices) {
    console.log(product, price);
  }
  let oldPrice = productPrices.get("Milk");
  let newPrice = oldPrice * 1.20; 
  productPrices.set("Milk", newPrice);
  console.log("Updated prices:", productPrices);
  