function moveZeroes(nums) {
    let nonZeroIndex = 0;

    // Iterate through the array, and whenever a non-zero element is encountered, swap it with the element at nonZeroIndex
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            [nums[i], nums[nonZeroIndex]] = [nums[nonZeroIndex], nums[i]];
            nonZeroIndex++;
        }
    }

    return nums;
}

// Test cases
const example1 = [0, 1, 0, 3, 12];
moveZeroes(example1);
console.log(example1); 
// Output: [1, 3, 12, 0, 0]

const example2 = [0, 2, 0, 8, 0, 5];
moveZeroes(example2);
console.log(example2); 
// Output: [2, 8, 5, 0, 0, 0]

const example3 = [4, 0, 9, 1, 0, 3, 0];
moveZeroes(example3);
console.log(example3); 
// Output: [4, 9, 1, 3, 0, 0, 0]
