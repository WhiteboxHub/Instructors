// try {
//     let result = 10 / 0; 
//     console.log(result);
//     console.log(reslt);
//   } catch (error) {
//     console.error('An error occurred:', error.name);
//   } finally {
//     console.log('Finally block executed');
//   }


// ********************************************************************
// try catch :
// try {
//   let result = add(10, 20);
//   console.log(result);
// } catch (e) {
//   console.log({ name: e.name, message: e.message });
// }
// console.log('Bye');


// ignoring the catch block

// const add = (x, y) => x + y;

// try {
//   let result = add(10, 20);
//   console.log(result);
// } catch (e) {
//   console.log({ name: e.name, message: e.message });
// }
// console.log('Bye');


// **********************************************************************************


// try catch finally : 

// let result = 0;
// try {
//   result = add(10, 20);
// } catch (e) {
//   console.log(e.message);
// } finally {
//   console.log({ result });
// }


// const add = (x, y) => x + y;

// let result = 0;

// try {
//   result = add(10, 20);
// } catch (e) {
//   console.log(e.message);
// } finally {
//   console.log({ result });
// }


// **********************************************************************************

// throw :

// function add(x, y) {
//     if (typeof x !== 'number') {
//       throw 'The first argument must be a number';
//     }
//     if (typeof y !== 'number') {
//       throw 'The second argument must be a number';
//     }
  
//     return x + y;
//   }
  
//   const result = add('a', 10);
//   console.log(result);
  

// function add(x, y) {
//     if (typeof x !== 'number') {
//       throw 'The first argument must be a number';
//     }
//     if (typeof y !== 'number') {
//       throw 'The second argument must be a number';
//     }
  
//     return x + y;
//   }
  
//   try {
//     const result = add('a', 10);
//     console.log(result);
//   } catch (e) {
//     console.log(e);
//   }
  
// ***************************************************************************

// Using JavaScript throw statement to throw an instance of the Error class :

// function add(x, y) {
//     if (typeof x !== 'number') {
//       throw new Error('The first argument must be a number');
//     }
//     if (typeof y !== 'number') {
//       throw new Error('The second argument must be a number');
//     }
  
//     return x + y;
//   }
  
//   try {
//     const result = add('a', 10);
//     console.log(result);
//   } catch (e) {
//     console.log(e.name, ':', e.message);
//   }
  