// Classes

// class Student {
//     setDetails(sid,Name,Grade){
        
//         this.sid=sid;
        
//         this.Name=Name;
      
//         this.Grade=Grade;

//     }
//     display(){
//         console.log(this.sid,this.Name,this.Grade);
   
//     }
// }
// let Stu=new Student();
// Stu.setDetails(143,"DEV","A+");
// Stu.display();


// Object

// const student ={
//     fName :'Riyansh',
//     lName : 'Dev',
//     age : 20,
//     gender : 'male',
//     isEnrolled : true,
// courses : ['UI','QA'],
// instructor : {
//     name : ['saketh','shiva','srikanth'],
//     courses : ['UI','QA'],
// },
// getDetails : function(){
//     return `Student full name : ${this.fName} ${this.lName}
//     age : ${this.age}
//     is enrolled in course : ${this.courses[1]}
//     `
// }
// }
// student.age=30;
// student.country='india';
// // delete student.fName;
// console.log(student.getDetails());


// Primitive type

// var x=10;
// var y=x;
// console.log(x,y);
// var x=20;
// console.log(x,y);


// non_pimitive type

// var obj1={name : 'DEV'}
// var obj2=obj1;
// console.log(obj1,obj2);
// var obj1={name : 'Sri'}
// console.log(obj1,obj2);


// inheritance 

// class Animal{
//     constructor(name,breed,colour){
//         this.name='Dog';
//         this.breed='Lab';
//         this.colour='Brown';
//         this.cost=5000;
//     }
// }
// class Dog extends Animal{   
   

// }
// const Dog1=new Dog() 
// console.log(Dog1.name,Dog1.breed,Dog1.colour); //dog lab brown
// console.log(Dog1);//Dog { name: 'dog', breed: 'lab', colour: 'brown' }
// console.log(Dog1);


// Getter :

// const student={
//     firstName : 'Raju',
//     lastName : 'kumar',
//     get getName(){
//         return ` ${this.firstName} ${this.lastName}`
//     }
// }
// console.log(student.firstName);
// console.log(student.getName);
// console.log(student.getName());


// Setter

// const student={
// firstName : 'Rajan',
// set changeName(newName){
//     this.firstName=newName;
// }
// }
// console.log(student.firstName);
// student.changeName='SriRajan';
// console.log(student.firstName);

// const student = {
//     firstName: 'Monica',
    
//     //accessor property(setter)
//     set changeName(newName) {
//         this.firstName = newName;
//     }
// };

// console.log(student.firstName); // Monica

// // change(set) object property using a setter
// student.changeName = 'Sarah';

// console.log(student.firstName); // Sarah




// class Animal{
//     constructor(name){
//         this.name=name
//     }
//     eats(){
//         console.log(this.name+' eats food');
//     }
// }
// class alligator extends Animal{
//     eats(){
//         // super.eats();
//         console.log(this.name+' eats fishes');
//     }
// }
// let murphy=new alligator('Murphy');
// murphy.eats();


// Static method


// 1. instance method

// class Person{
//     constructor(name,gender,birthYear){
//         this.name=name;
//         this.gender=gender;
//         this.birthYear=birthYear;
//     }
//     calcAge(){
//         console.log(new Date().getFullYear()-this.birthYear);
//     }
// }
// let DEV=new Person('DEV','male',2023);
// console.log(DEV);


// 2. Static method

// class Person{
//     constructor(name,gender,birthYear){
//         this.name=name;
//         this.gender=gender;
//         this.birthYear=birthYear;
//     }

//     calcAge(){ //instance method
//         console.log(new Date().getFullYear()-this.birthYear);
//     }
    
//     static greet(){  //Static method
//         console.log('Hey there ! how r u');
//     }
// }

// // to call instance method
// let DEV=new Person('DEV','male',2023);
// console.log(DEV);

// // to call static method
// Person.greet();


// static method for function constructor 
// let person=function(name,gender,birthYear){
//     this.name=name;
//     this.gender=gender;
//     this.birthYear=birthYear;
// }

// // to know age
// person.prototype.calcAge=function(){
//     let age=new Date().getFullYear()-this.birthYear;
//     console.log(age);
// }
// person.greet=function(){
//     console.log('Have a nice day');
// }

// // to call instance method
// let raju=new person('Raju','male',1998);
// console.log(raju);

// // to know age
// raju.calcAge();

// // to call static method
// person.greet();


// var i='hi';
// var k='Hi';
// console.log(i===k);
// program to find the ASCII value of a character

// take input from the user
// const v = '0';

// // convert into ASCII value

// const result =v.charCodeAt()
// console.log(`The ASCII value is: ${result}`);


// Encapsulation : 
// class BankAccount {
//     constructor(balance) {
//       this.balance = balance; 
//     }
  
//     getBalance() {
//       return this.balance; 
//     }
  
//     deposit(amount) {
//       this.balance += amount;
//     }

//     withdraw(amount) {
//       if (amount <= this.balance) {
//         this.balance -= amount;
//         console.log("collect cash");
//       } else {
//         console.log("Insufficient funds");
//       }
// }
   
//   }
  
//   let account = new BankAccount(1000);
//   account.withdraw(500);
  


// Polymorphism: 
class Bird {
    fly() {
      console.log("The bird is flying");
    }
  }
  
  class Fish {
    swim() {
      console.log("The fish is swimming");
    }
  }
  
  function move(animal) {
    if (animal.fly) {
      animal.fly();
    } else if (animal.swim) {
      animal.swim();
    }
  }
  
  const sparrow = new Bird();
  const salmon = new Fish();
  
  move(sparrow); 
  move(salmon); 
  
  

