fetch("https://jsonplaceholder.typicode.com/posts")
  .then(response => {
    return response.json();
  })
  .then(data => {
    const firstFive = data.slice(0, 5);
    firstFive.forEach(post => {
      console.log(post.title);
    });
  })
  .catch(err => console.log("Error:", err));