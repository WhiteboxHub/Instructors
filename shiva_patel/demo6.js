// function Person(name, age) {
//     this.name = name;
//     this.age = age;
  
//     this.sayHello = function() {
//       console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
//     };
//   }
  
  
//   const person1 = new Person('Alice', 25);
//   const person2 = new Person('Bob', 30);
  
 
//   console.log(person1.name); 
//   console.log(person2.age);  
//   person1.sayHello();       
//   person2.sayHello();    
  function exampleFunction(firstArg, ...restArgs) {
    console.log("First argument:", firstArg);
  
    if (restArgs.length > 0) {
      console.log("Second argument:", restArgs[1]);
    } else {
      console.log("No second argument provided.");
    }
  }
  
  // Usage
  exampleFunction("A");
  