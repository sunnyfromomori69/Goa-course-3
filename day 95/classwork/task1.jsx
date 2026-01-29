import { useEffect, useState } from "react";
function DataFetcher() {
  const [dataType, setDataType] = useState("users");
  const [data, setData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `https://jsonplaceholder.typicode.com/${dataType}`
        );
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, [dataType]); 
  return (
    <div>
      <button onClick={() => setDataType("users")}>Users</button>
      <button onClick={() => setDataType("posts")}>Posts</button>
      <button onClick={() => setDataType("comments")}>Comments</button>
      <h2>Current data type: {dataType}</h2>
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            {dataType === "users" && item.name}
            {dataType === "posts" && item.title}
            {dataType === "comments" && item.email}
          </li>
        ))}
      </ul>
    </div>
  );
}
export default DataFetcher;