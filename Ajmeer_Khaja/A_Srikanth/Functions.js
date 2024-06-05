// function myFun() {
//     console.log('hiii');
// }
// myFun();

// var func=new Function('console.log("hello func")')
// func()

// var fun3=function(){
//     console.log('this is function fun3');
//     return 781356;
// }
// console.log(fun3());

// var fun4=()=> {
//     console.log('this is arrow function');
// }
// fun4();

// (function(){
//     console.log('Anonymous function');
// })
// ();

// var a=100,b=2000,c=300,d=20
// function add(x,y) {
//     return x+y;
// }
// console.log(add(a,b));
// console.log(add(c,d));
// console.log(add(b,d));
// console.log(add(a,d));

// var callback=function () {
//     console.log('this is call back function');
// }
// function higher(fun) {
//     fun();
//     console.log('this is higher order function');
// }
// higher(callback)


// Basic example for callback and higher order function

// var x=function () {
//     return 'function1'
// }
// console.log(x());
// var y=x;
// console.log(y());


// (
//     function () {
//         console.log('anonymous');
//     }
// )();


// var person={
// fullname :function(){
//     console.log(this.fname+" "+this.lname);
// }
// }
// var person1={
//     fname : 'sai',
//     lname : 'Ram',
    
// }


// var person2={
//     fname : 'Ram',
//     lname : 'Babu'
// }
// person.fullname.call((person2));
// person.fullname.call((person1));




// var person = {
//     fullName: function() {
//     console.log(this.firstName+ " "+ this.lastName);
//     }
//   }
//   var person1 = {
//     firstName:"John",
//     lastName: "Doe"
//   }
//   var person2 = {
//     firstName:"Mary",
//     lastName: "Doe"
//   }
   
//   person.fullName.call(person2,'hiii');



// var obj1={
//     fname : 'Riyansh',
//     lname : 'DEV',
//     fullname : function () {
//         // return `${this.fname} ${this.lname}`
//         console.log(this.fname,this.lname);
//     }
// }
// console.log(obj1.fullname.call());


// bind() :
// var person={
//     fName : 'Jhon',
//     lName : 'Wick'
// }
// function fullName(msg){
//     return (`${msg} ${this.fName} ${this.lName}`);
// }
// var newFunc=fullName.bind(person,'Hello');
// console.log(newFunc());


// call() :
// var person={
//     fName : 'Jhon',
//     lName : 'Wick'
// }
// function fullName(msg){
//     return (`${msg} ${this.fName} ${this.lName}`);
// }
// var newFunc=fullName.call(person,'Hello');
// console.log(newFunc);


// var x=10;
// console.log(x);
// function fun1(){
//     var y=20;
//     console.log(x,y);
// }
// fun1();
// // console.log(x,y);


// let x=10;
// console.log(x);
// function fun1(){
//     let y=20;
//     console.log(x,y);
// }
// fun1();
// // console.log(x,y);


// const x=10;
// console.log(x);
// function fun1(){
//     const y=20;
//     console.log(x,y);
// }
// fun1();
// // console.log(x,y);

// forin
// const person = {fname:"John ", lname:"Doe ", age:25};

// let text = "";
// for (let x in person) {
//   text += person[x];
// }
// console.log(text);

// var a=10;
// console.log(a);
// var fun1=function(){
//     var b=20;
//     console.log(a,b);
//     var fun2=function() {
//         var c=30;
//         console.log(a,b,c);
//     }
//     fun2();
// }
// fun1();

// console.log(getName)
// var x=7;
// function getName(){
//     console.log("namasthay javaScript");

// }

// console.log(x);
// var x=20;
// console.log(x);

// function maxOfAll() {
//     var max=0;
//     for(var i=0;i<arguments.length;i++){
//         if(arguments[i]>max){
//             max=arguments[i];
//         }
//     }
//     return max;
// }
// var x=maxOfAll(1,4,3,2,5,7,9,56,45,78,65,87,97,3,5);
// console.log(x);

