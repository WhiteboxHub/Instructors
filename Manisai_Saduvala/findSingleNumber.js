//Given a non-empty array of integers nums, every element appears twice except for one
//Find that single one you must implement a solution whith a linear runtime complexity and use only constant extra space

function findSingleNumber(nums)
{
  // intializing results to 0

let results = 0;
// iterating through the loop

for (let i = 0; i< arr.length; i++)
{
  // comparing the bitwise numbers using XOR
  results ^ = arr[i];
}
  //Returning the resultant number
return results;

}

// Test cases
// Example 1 
// input num = [2,3,2,4,3,1];
// output = 1
// Example 2 
// input num = []
// return empty array
// Example 3 
// input nums = [2,3,4]
// output 0
