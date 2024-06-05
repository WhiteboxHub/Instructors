function minOperationsToEmptyArray(arr) {
    let operations = 0;
  
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] === arr[i - 1]) {
        // Remove consecutive elements with the same value
        arr.splice(i - 1, 2);
        operations++;
        i -= 2; // Move the index back to check previous elements
      }
    }
  
    return operations;
  }
  
//   Test cases
  const array1 = [1, 2, 3,4,5];
  const array2 = [1, 2, 3, 4, 5];
  const array3 = [10, 10, 20, 30, 30, 30, 40];
  
  console.log(`Minimum operations for array1: ${minOperationsToEmptyArray(array1)}`);
  console.log(`Minimum operations for array2: ${minOperationsToEmptyArray(array2)}`);
  console.log(`Minimum operations for array3: ${minOperationsToEmptyArray(array3)}`);
  
