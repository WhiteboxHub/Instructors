function moveZeroes(arr) {
  //taking a variable and assigning it to a value 0 which is used to store non zero element
  let nonZeroIndex = 0;

  //looping through an array
  for (let i = 0; i < arr.length; i++) {
    //Storing non zero element in a temp variable
      let temp = arr[nonZeroIndex];
      //checking if current ele is not zero
    if (arr[i] != 0) {
      arr[nonZeroIndex] = arr[i];
      arr[i] = temp;
      nonZeroIndex++;
    }
  }
  return arr;
}
console.log(moveZeroes([1,2,3]));

// // Positive Test Case
// let nums = [1, 0, 0, 2, 3];
// moveZeros(nums);
// console.log(nums); // Output: [1, 2, 3, 0, 0]

// Negative Test Case: Empty Array
// let numsEmpty = [];
// moveZeros(numsEmpty);
// console.log(numsEmpty); // Output: []

// Negative Test Case: Null
// let numsNull = null;
// moveZeros(numsNull);
// console.log(numsNull); // Output: null
