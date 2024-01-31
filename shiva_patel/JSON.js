// Creating  an Object
const person = { "name": "John Doe", "age": 30, "city": "New York" };
console.log("Original Object:", person);

// Convert object to JSON string
const jsonPerson = JSON.stringify(person);
console.log("\nJSON String:", jsonPerson);

// Parse JSON String to Object
const parsedPerson = JSON.parse(jsonPerson);
console.log("\nParsed Object:", parsedPerson);

// Creating Array
const fruits = ["apple", "banana", "orange"];
console.log("\nOriginal Array:", fruits);

// Convert array to JSON string
const jsonFruits = JSON.stringify(fruits);
console.log("\nJSON String:", jsonFruits);

// Parse JSON String to Array
const parsedFruits = JSON.parse(jsonFruits);
console.log("\nParsed Array:", parsedFruits);
