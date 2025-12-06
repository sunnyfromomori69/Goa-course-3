const users = new Map([
    [1, "Nika"],
    [2, "Ana"],
    [3, "Giorgi"],
    [4, "Mariam"]
  ]);
  console.log("User IDs:");
  for (const id of users.keys()) {
    console.log(id);
  }
  for (const name of users.values()) {
    console.log(name);
  }
  console.log("User Entries (id => name):");
  for (const [id, name] of users.entries()) {
    console.log(id, "=>", name);
  }