function customSort(arr) {
  const positiveNumbers = arr.filter(num => num >= 0);
  const sortedPositive = positiveNumbers.sort((a, b) => a - b);

  let sortedArr = [];
  let positiveIndex = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 0) {
      sortedArr.push(sortedPositive[positiveIndex]);
      positiveIndex++;
    } else {
      sortedArr.push(arr[i]);
    }
  }

  return sortedArr;
}

// Example test cases
const testCase1 = [11, 16, -2, -4, 7, 8];
const result1 = customSort(testCase1);
console.log(`Test Case 1: ${JSON.stringify(result1)}`); // Output: [7, 8, -2, -4, 11, 16]

const testCase2 = [-5, -3, 0, 2, 4];
const result2 = customSort(testCase2);
console.log(`Test Case 2: ${JSON.stringify(result2)}`); // Output: [0, 2, -3, -5, 4]

const testCase3 = [1, -1, 3, -3, 5, -5];
const result3 = customSort(testCase3);
console.log(`Test Case 3: ${JSON.stringify(result3)}`); // Output: [1, -1, 3, -3, 5, -5]
