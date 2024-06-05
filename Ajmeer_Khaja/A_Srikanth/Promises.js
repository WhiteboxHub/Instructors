// function fetchData() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             const success = true; 

//             if (success) {
//                 resolve("Data successfully fetched");
//             } else {
//                 reject("Error fetching data");
//             }
//         }, 1000);
//     });
// }

// fetchData()
//     .then((result) => {
//         console.log("Success:", result);
//     })
//     .catch((error) => {
//         console.error("Error:", error);
//     });



// function fetchData() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             const success = true; 
//             if (success) {
//                 const data = { message: "Data successfully fetched" };
//                 resolve(data); 
//             } else {
//                 const error = new Error("Failed to fetch data");
//                 reject(error);
//             }
//         }, 2000); 
//     });
// }

// console.log("Start");

// fetchData()
//     .then((result) => {
//         console.log("Success:", result.message);
//     })
//     .catch((error) => {
//         console.error("Error:", error.message);
//     })
//     .finally(() => {
//         console.log("End");
//     });


// function getUsers() {
//     return [
//       { username: 'sri', email: 'sri@gmail.com' },
//       { username: 'rajan', email: 'rajan@gmail.com' },
//     ];
//   }
  
//   function findUser(username) {
//     const users = getUsers(); 
//     const user = users.find((user) => user.username === username);
//     return user;
//   }
  
//   console.log(findUser('rajan'));
  



// function getUsers() {
//     let users = [];
  
//     // delay 1 second (1000ms)
//     setTimeout(() => {
//       users = [
//         { username: 'john', email: 'john@test.com' },
//         { username: 'jane', email: 'jane@test.com' },
//       ];
//     }, 1000);
  
//     return users;
//   }




//   function getUsers() {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             const users = [
//                 { username: 'john', email: 'john@test.com' },
//                 { username: 'jane', email: 'jane@test.com' },
//             ];
//             resolve(users);
//         }, 1000);
//     });
// }

// // Usage
// getUsers().then((users) => {
//     console.log(users);
// });


//CLASS

// class Student{
//     setDetails(sid,name,grade){
//         this.sid=sid;
//         this.name=name;
//         this.grade=grade;
//     }
//     display(){
//         console.log(this.sid,this.name,this.grade);
//     }
// }
// let stu=new Student();
// stu.setDetails(101,'raj','a')
// stu.display()


// let user = {    
//     name: "John", 
//     age: 30        
//   };
//   console.log(user.name);
//   console.log(user.age);

// Creating a simple object
// let person = {
//     name: 'Riyansh',
//     age: 25,
//     isStudent: true,
//     introduce: function() {
//       console.log(`Hi, I'm ${this.name}, and I'm ${this.age} years old.`);
//     }
//   };
//   console.log(person.name);  
//   console.log(person.isStudent); 
//   person.introduce(); 
  




// Creating a Promise
// const myPromise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//       const success = true;
  
//       if (success) {
//         resolve("Operation completed successfully!");
//       } else {
//         reject("Operation failed!");
//       }
//     }, 2000); // Simulating a delay of 2 seconds
//   });
  
//   myPromise
//     .then((result) => {
//       console.log("Success:", result);
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     })
//     .finally(() => {
//       console.log("Finally block - This will be executed regardless of success or failure.");
//     });
  




const fetchData = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const success = true;
  
        if (success) {
          const data = { id: 1, name: "John Doe", age: 25 };
          resolve(data);
        } else {
          reject("Failed to fetch data from the API");
        }
      }, 2000); 
    });
  };
  
  fetchData()
    .then((result) => {
      console.log("Data fetched successfully:", result);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    })
    .finally(() => {
      console.log("Fetching data operation completed.");
    });
  