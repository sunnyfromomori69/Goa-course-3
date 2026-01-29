import React, { useEffect, useState } from "react";
import Product from "./components/Product";
function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true); 
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch("https://fakestoreapi.com/products");
        const data = await response.json();
        setProducts(data);
        setLoading(false); 
      } catch (error) {
        console.error("Error fetching products:", error);
        setLoading(false); 
      }
    };
    fetchProducts();
  }, []);
  if (loading) {
    return <div>...Loading</div>;
  }
  return (
    <div>
      <h1>Products</h1>

      {products.map((product) => (
        <Product key={product.id} product={product} />
      ))}
    </div>
  );
}
export default App;
