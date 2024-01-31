let set = new Set();

let j = { name: "Jo" };
let p = { name: "Pe" };
let m = { name: "Ma" };
let a ="shiva";
var b = "shiva";
var b = "patel";


set.add(j);
set.add(p);
set.add(m);
set.add(a);
set.add(b);
set.add(b);


console.log( set.size ); 

for (let user of set) {
  console.log(user); 
}


let set1 = new Set();
set1.add("hello");
console.log(set1)