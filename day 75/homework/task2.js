
var name = "Nika";
var name = "Giorgi"; 
console.log("var:", name);


let age = 20;
age = 25; 
console.log("let:", age);


const country = "Georgia";

console.log("const:", country);



function testScope() {
  var x = 10;  
  let y = 20;  
  const z = 30;

  if (true) {
    var a = "var inside block";   
    let b = "let inside block";   
    const c = "const inside block"; 
    console.log(b); 
    console.log(c); 
  }

  console.log(a); 
}
testScope();


function outerFunction() {
  let outerVar = "Outer variable";

  function innerFunction() {
    let innerVar = "Inner variable";
  }
    
    console.log("Inner function sees:", outerVar);
    console.log("Inner variable:", innerVar);
  }

  innerFunction();


outerFunction();

