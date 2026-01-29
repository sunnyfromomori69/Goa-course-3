import React from "react";

function Product({ product }) {
  return (
    <div style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
      <h2>{product.title}</h2>
      <img src={product.image} alt={product.title} width="100" />
      <p>{product.description}</p>
      <p>
        <strong>Price:</strong> ${product.price}
      </p>
    </div>
  );
}

export default Product;