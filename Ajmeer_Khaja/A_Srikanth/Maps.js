// let myMap = new Map();

// myMap.set('name', 'John');
// myMap.set(1, 'One');
// myMap.set(true, 'Boolean');

// console.log(myMap.get('name'));
// console.log(myMap.get(1));       
// console.log(myMap.get(true));    

// console.log(myMap.has('age'));   

// console.log(myMap.size);         

// myMap.delete(1);
// console.log(myMap.size);        

// for (let [key, value] of myMap) {
//   console.log(`${key}: ${value}`);
// }
// myMap.clear();
// console.log(myMap.size);       




// const fruits = new Map([
//     ["apples", 500],
//     ["bananas", 300],
//     ["oranges", 200]
//   ]);
//   console.log(fruits.get("apples")); 
//   console.log(fruits.size);
//   fruits.delete("apples");
//   console.log(fruits);
//   console.log(fruits.has("apples"));
// console.log(fruits);


// let map=new Map();
// map.set('srikanth','java');
// map.set('ram','sql');
// map.set('saindhav','python');
// map.set('srikanth','javascript');
// for(let [k,v]of map){
//     console.log(k,':',v);
// }


let myMap = new Map();

myMap.set('key1', 'value1');
myMap.set('key2', 'value2');
myMap.set('key1', 'new_value'); 

console.log(myMap.get('key1')); 
console.log(myMap.get('key2')); 
