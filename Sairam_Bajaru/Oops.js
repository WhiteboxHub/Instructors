/*
let person = {
    name: 'John',
    age: 30,
    gender:'male',
    greet: function() {
      console.log('Hello mowa , ' + this.name + '!');
    }
  };
  
 console.log(person.greet()); // Outputs: Hello, John!
 
 function Person(name, age) {
    this.name = name;
    this.age = age;
    this.greet = function() {
      console.log('Hello, ' + this.name + '!');
    };
  }
  
  let person1 = new Person('John', 30);
  let person2 = new Person('Jane', 25);
  person1.greet(); // Outputs: Hello, John!
  //console.log(greet()); // Outputs: Hello, Jane!
  person2.greet();
  //console.log(greet());
  
 
  const Person = {
    name: 'sai',
    age: 22,
    greet: function () {
      console.log('Hello, ', this.name, this.age, '!');
    }
  };
  
  Person.greet();
  

 // Constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
  
    // Method defined inside the constructor
    this.greet = function() {
      console.log(`Hello, ${this.name}!`);
    };
  }
    // Creating an instance of Person
  const person = new Person('John', 30);
  
  // Calling the method
  person.greet(); // Outputs: Hello, John!
  // Inheriting from the Person class
class Student extends Person {
    // Constructor for Student
    constructor(name, age, grade) {
      // Call the constructor of the parent class
      super(name, age);
      this.grade = grade;
    }
  
    // Additional method for Student
    study() {
      console.log(`${this.name} is studying.`);
    }
  }
  
  // Creating an instance of the Student class
  const student = new Student('Alice', 20, 'A');
  
  // Using methods from both classes
  student.greet(); // Outputs: Hello, Alice!
  student.study(); // Outputs: Alice is studying.
  */
