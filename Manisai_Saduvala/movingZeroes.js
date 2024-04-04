function moveZeroesToEnd(nums) {
    let left = 0; // left pointer

    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            // Swap non-zero element with the element at left pointer
            [nums[left], nums[i]] = [nums[i], nums[left]];
            left++;
        }
    }

    return nums;
}

// Example usage:
const nums = [0, 1, 0, 3, 12];
console.log("Original array:", nums);
console.log("Array with zeroes moved to end:", moveZeroesToEnd(nums.slice())); // Using slice() to avoid modifying the original array
