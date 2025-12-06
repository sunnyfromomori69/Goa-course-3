
studentsMap.set("Nika", 95);
studentsMap.set("Ani", 88);
studentsMap.set("Luka", 76);
studentsMap.set("Mariam", 90);
studentsMap.set("Gio", 82);
console.log(studentsMap.get("Ani"));     
console.log(studentsMap.has("Luka"));    
studentsMap.delete("Gio");
console.log("Map after delete:");
console.log(studentsMap);