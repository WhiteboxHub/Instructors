// for in
// let aline={
//     name : 'sai',
//     tech : 'js',
//     laptop : {
//         cpu : 'i7',
//         ram : 4,
//         brand : 'asus'
//     }
// }
// for(let key in aline)
// {

//     // if(aline[key] == "laptop"){
//     //     break;
//     console.log(key,aline[key]);
//     }

// // }

// // for(let key1 in aline.laptop){
// //     console.log(key1,aline.laptop[key1]);
// // }

// let number ={
//     even : 2,
//     odd : 3,
//     whole :{
//         num : 0,
//         num1 : 'infinity'
//     }
// }
// for(let key in number){
//     console.log(key,number[key]);
// }

// for(let key1 in number.whole){
//     console.log(key1,number.whole[key1]);
// }

// var i=[7,8,9,2,4,5,6,7,7,12,22,8,97]
// console.log(i.sort((a,b) => a-b));


// forof

// let nums=[];
// nums [0]=5;
// nums [99]=9;
// // for(let n of nums){
// //     console.log(n);
// // }
// for(let key in nums){
//     console.log(nums[key]);
// }

// x=12;
// console.log('x= '+x);
// var x;

// for(var x=1;x<5;x++){
//     console.log(x);
// }

// const fruits = ["Banana", "Orange", "Apple", "Kiwi"];
// let x=fruits.sort();
// console.log(x);

// const person = {
//     firstName: "John",
//     lastName : "Doe",
//     id       : 5566,
//     fullName : function() {
//     //   return this.firstName + " " + this.lastName;
//     } 
//   }
//   console.log(person.firstName);
//   console.log(person.lastName);
//   console.log(person.id);
//   console.log(person.fullName());


// function localFunction() {
//     var localVariable = "I am local";
//     console.log(localVariable); // Accessing local variable
// }

// localFunction();
// console.log(localVariable);


// if (true) {
//     let blockVariable = "I am in a block";
//     console.log(blockVariable); // Accessing block-scoped variable
// }
// console.log(blockVariable);

// function functionScopeExample() {
//     if (true) {
//         var functionScopedVariable = "I am function-scoped";
//         console.log(functionScopedVariable); // Accessing function-scoped variable
//     }
// }

// functionScopeExample();
// console.log(functionScopedVariable)


// let double = n => n * 2;
// console.log(double(3));


// var callback=function(){
//     console.log('this is callback');

// }
// callback();

// function fetchData(callback) {
//     setTimeout(function () {
//         const data = { message: "Data fetched successfully" };
//         callback(data);
//     }, 1000);
// }

// function handleData(data) {
//     console.log(data.message);
// }

// fetchData(handleData);
// function multiplier(factor) {
//     console.log(factor + "/////////////////");
//     return function (x) {
//         console.log( "==============================");
//         return  x * factor;
//     };
// }

// const double = multiplier(2);
// const triple = multiplier(3);

// console.log(double(5)); // Outputs 10
//  console.log(triple(6)); // Outputs 15
 


// function sum(a, b) {
//     return a + b;
//   }
//   function sum(a){
//     return a;
//   }
//   function sum(a,b,c,d){
//     return a+b+c+d;
//   }
// console.log( sum(3,4,5,76,7) );

// function sumAll(...args) { // args is the name for the array
//     let sum = 0;
  
//     for (let arg of args) sum += arg;
  
//     return sum;
//   }
  
//   console.log( sumAll(1) ); // 1
//   console.log( sumAll(1, 2) ); // 3
//   console.log( sumAll(1, 2, 3) ); // 6

// function showName(firstName, lastName, ...titles) {
//     console.log( firstName + ' ' + lastName ); // Julius Caesar
  
//     // the rest go into titles array
//     // i.e. titles = ["Consul", "Imperator"]
//     console.log( titles[0] ); // Consul
//     console.log( titles[1] ); // Imperator
//     console.log( titles.length ); // 2
//   }
  
//   showName("Julius", "Caesar", "Consul", "Imperator");


// general EX : 
// function sum(a,b){
// return a+b;
// }
// let result=sum(4,3,6,2);
// console.log(result);


// Arguments EX: 
// function sum(){
//     return arguments[0]+arguments[1]+arguments[2] ;

// }
// let result=sum(4,3,6,2);
// console.log(result);

// Rest parameters EX : 
// function sum(a,b,...args){
//     let num=a+b;
//     for(let n of args){
//         num=num+n;

//     }
//     return num;

// }
// let result=sum(4,3,6,2,5,4);
// console.log(result);

// Spread operator : 
// function sum(a,b,c,d,e){
//     return a+b+c+d+e;

// }
// let nums=[4,3,6,2,5];
// let result=sum(...nums);
// console.log(result);

// let num=[3,4,5,6,9];
// // console.log(num);
// let[a,b,c,d,e]=num;
// console.log(e);
// Destructuring


// let words="My name is srikanth A".split(' ');
// let[a,b,,...d] =words;

// console.log(d); //[ 'srikanth', 'A' ]



// let words="My name is srikanth A".split(' ');
// let[a,b,...d] =words;

// console.log(d); //[ 'is', 'srikanth', 'A' ]


// const arr=[2,23,45,76,876,89]
// function x(arr.reduce){
    
// }
// console.log(arr.reduce);


// this 

// let laptop1 ={
//     cpu : 'i7',
//     ram : 16,
//     brand : 'hp',
//     getinfig : function (){
//         console.log(this.ram);
//         console.log(this.brand);

//     }
// }
// let laptop2 = {
//     cpu : 'i5',
//     ram : 5,
//     brand : 'dell',
//     getinfig : function (){
//         console.log(this.ram);
//     }
// }
// laptop1.getinfig();


// function add(a,b){
//     return a+b;

// }
// console.log(add(4,56));


// const originalArray = [1, 2, 3];
// const newArray = [...originalArray, 4];
// console.log(originalArray);
// console.log(newArray);


// Higher-Order Function Example



// function multiplyBy(factor) {
//     return function (number) {
//       return number * factor;
//     };
//   }
  
//   const double = multiplyBy(2);
//   console.log(double(5)); // Output: 10
  
// let fruits = ['apple', 'banana', 'orange', 'grape'];

// // Remove 1 element starting from index 2
// let removedElement = fruits.splice(2, 1);

// console.log(fruits);          // Outputs: ['apple', 'banana', 'grape']
// console.log(removedElement);  // Outputs: ['orange']

// var i=  'hello i can"'t" hello'
// console.log(i);


// var i = 'hello i can"\'t" hello';
// console.log(i);





// function outerFunction() {
//     let outerVariable = "I am from outer function";
  
//     function innerFunction() {
//       console.log(outerVariable);
//     }
  
//     return innerFunction;
//   }
  
//   // Creating a closure by assigning innerFunction to a variable
//   let closure = outerFunction();
  
//   // Executing the closure
//   closure(); // Outputs: I am from outer function
  


// function createCounter() {
//     let count = 0;
  
//     return function() {

    
//         if (count == -4){
//             return 4;
//         }
        
//      return count--
     
//     };
//   }
  
//   let counter = createCounter();
//   console.log(counter()); 
//   console.log(counter());
//   console.log(counter()); 
//   console.log(counter()); 
//   console.log(counter()); 
  



// function sum(a,b,...args){
//     let num=a+b;
//     for(let a of args){
//         num=num+a;
//     }

//     return num;
// }
// let result=sum(4,3,6,2,5);
// console.log(result);


// const cars = [2,3,4,5,7,8,6,6,4,7,0];
// let text = " ";
// for (let x of cars) {
//   text += x;
// }
// console.log(text);


// function* simple(){
//     console.log('before 1');
//     yield 1;
//     console.log('after 1');
//     console.log('before 2');
//     yield 2;
//     console.log('after 2');
//     console.log('before 3');
//     yield 3;
//     console.log('after 3');
    

// }
// const generatorobj=simple();
// console.log(generatorobj.next());
// console.log(generatorobj.next());
// console.log(generatorobj.next());
// console.log(generatorobj.next());

// function* myGenerator() {
//     yield 1;
//     yield 2;
//     yield 3;
//     yield 4;
//     yield 5;
//   }
  
//   // Using the generator to iterate over values
//   const iterator = myGenerator();
  
//   let result = iterator.next();
//   while (!result.done) {
//     console.log(result.value);
//     result = iterator.next();
//   }
  


// function fact(num){
//   let f=1;
//   for(let i=1;i<=num;i++){
//     f=f*i;

//   }
//   console.log(f);
// }
// fact(5);


//class : 

// class Student{
//   details(sid,name,age){
//     this.sid=sid;
//     this.name=name;
//     this.age=age;
//   }
//   // display(){
//   //   console.log(this.sid,this.name,this.age);
//   // }
// }
// let stu=new Student();
// stu.details(143,'sai',22);
// console.log(stu);
// // stu.display();



// inheritance : 
// function check(a, b) {
//     if (a > b) {
//         console.log(add(a, b));
//     } else if (a < b) {
//         console.log(sub(a, b));
//     } else if (a == b) 
//         console.log(mul(a, b));
    
// }
//     function add(x, y) {
//         return x + y;
//     }

//     function sub(i, j) {
//         return i - j;
//     }

//     function mul(c, d) {
//         return c * d;
//     }


// check(4, 6);





