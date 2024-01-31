/*function add(a,b){
    return a+b;
}
console.log(add(10,20));*/
//Arrow function syntax
const add =(a,b) => {
    return a+b;
};
console.log(add(20,10));
// implicite return
const subtract = (a, b) => a - b; 
// can  leave off () with a single  param
const double = a => a*2;
console.log(double(10));
console.log(subtract(10,5));

// returning an object 
const createObj = ()=>({
    name : 'shiva',
    age : 20,
});
console.log(createObj());
  const num =[1,2,3,3,4,45,54345];
  num.forEach( function (i){
    console.log(i)
  })
// Arrow function in a callback
num.forEach (i => console.log(i));
const user = 'siva';
console.log(user);