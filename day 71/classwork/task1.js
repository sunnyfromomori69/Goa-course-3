let age = 17;          
let name = "Sunny";    
let coding = true;   
let nothing = false;    


// primative and complex values are values that are stored in the memory stack, and they are also have a fixed size.

// stack is a memory storing type that is fast but doesnt have enough storage
// while heap is slower but can store more data? and memory.

let a = 5;
let b = a; // stack 

let obj1 = { name: "Sunny" };
let obj2 = obj1; // heap
obj2.name = "Mika";

let arr = [];
function addData() {   // memory leak is a thing that accours when the code runs infinitely or however you spell it and well drains your memory

}

addData()