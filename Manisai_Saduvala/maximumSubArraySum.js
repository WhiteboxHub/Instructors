// Program to find the maximum sub array sum in an array
// Test cases
// Given an array of length n, where n=6, caluclate max sub array sum
// for example consider an array [2, -1, -6] the maxsub array sum will be 2

  function maximumSubArraySum(arr)
  {
    // let max and current sum be the intial element of array
    let maximumSum = arr[0];
    let currentSum = arr[0];
    // iterating  over the array from the second element
    for (let i =1; i<= arr.length-1; i++)
    {
        // checking the max array sum and assigning to current sum
        currentSum = Math.max(arr[i], currentSum + arr[i]);
        // finding the max sum from current sum and the current ellement
        maximumSum = Math.max (maximumSum, currentSum);
    }
    return maximumSum;

  }
  console.log(maximumSubArraySum([-9, 3 ,-3 ,-7 ,-1 ,5]));

  //Excepted output - 5

// Big O notation- O(n)-> linear 
