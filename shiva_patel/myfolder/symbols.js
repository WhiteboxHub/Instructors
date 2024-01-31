const firstName = Symbol('first name');
const lastName = Symbol('last name');
const person = {
  [firstName]: 'shiva',
  [lastName]: 'patel',
  age: 24,
};

console.log(person[firstName]); 
console.log(person[lastName]); 


for (const key in person) {
  console.log(person[key]); 
}


//person[Symbol.toStringTag] = 'Person';//The Symbol.toStringTag is used to customize the default toString representation of the person object.
//This allows for a more meaningful representation when logging the object.


console.log(person.toString());
