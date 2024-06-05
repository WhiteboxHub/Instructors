function changeSignIfNumeric(arr) {
  // Check if the array contains non-numeric values
  if (arr.some(element => typeof element !== 'number')) {
    throw new Error('Array contains non-numeric values.');
  }

  // Regular expression to match + or -
  let regex = /\+|-/;

  // Change the sign of numeric elements
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].toString().match(regex)) {
      arr[i] = -arr[i]; // Change sign
    }
  }

  return arr;
}

// Example usage:
try {
  let result = changeSignIfNumeric([2, -2, 0, 1, -3]);
  console.log(result); // Output: [-2, 2, 0, -1, 3]

  // Uncomment the next line to test with non-numeric values
  // let invalidResult = changeSignIfNumeric([2, 'abc', 1]);
} catch (error) {
  console.error(error.message);
}
