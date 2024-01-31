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




  function getUsers() {
    return new Promise((resolve) => {
        setTimeout(() => {
            const users = [
                { username: 'john', email: 'john@test.com' },
                { username: 'jane', email: 'jane@test.com' },
            ];
            resolve(users);
        }, 1000);
    });
}

// Usage
getUsers().then((users) => {
    console.log(users);
});
