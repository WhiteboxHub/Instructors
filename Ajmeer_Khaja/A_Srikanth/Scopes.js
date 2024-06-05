// local scope : 
// function localF(){
//     var local='i am local'
//     console.log(local);
// }
// localF();
// console.log(local); //error

// block scope : 
// function exampleFunction() {
//     if (true) {
//       let x = 10; 
//       console.log(x); 
//     }
//   }
//       console.log(x); 
//   exampleFunction();
  
// function scope : 
// function fnScope(){
//     if(true){
//         var funScVar='im function scoped';
//         console.log(funScVar);
//     }
// }
// fnScope();
// console.log(funScVar);

// Rest parameter : 
// function sum(a,b,...args){
//     let num=a+b;
//     for(let n of args){
//         num=num+n;
//     }
//     return num;
// }
// let result=sum(4,3,6,2,5);
// console.log(result);

// Spread operator : 
// function sum(a,b,c,d,e){
//     return(a+b+c+d+e);
// } 
// let nums=[4,3,6,2,5];
// let result=sum(nums);
// console.log(result);

// to over come this we use spread operator

// function sum(a,b,c,d,e){
//     return(a+b+c+d+e);
// } 
// let nums=[4,3,6,2,5];
// let result=sum(...nums);
// console.log(result);


// *Swp of 2 numbers :
// let a=5;
// let b=6;
// [a,b]=[b,a]
// console.log(a,b);


// Array detructuring :

// let nums=[5,7,2,4]
// console.log(nums);
// let [a,b,c,d]=nums;
// console.log(d);

// string : 
// let words='my name is srikanth';
// console.log(words);
// let word="my name is srikanth".split('');
// console.log(word);
// let [a,b,c,d,e]=word;
// console.log(a,b);







