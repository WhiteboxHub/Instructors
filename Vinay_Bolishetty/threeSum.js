function threeSum(nums) {
    const result = [];

    // Sorting the array
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 2; i++) {
        // Check if it's the first element or a new element to avoid duplicates
        if (i === 0 || (i > 0 && nums[i] !== nums[i - 1])) {
            let left = i + 1;
            let right = nums.length - 1;

            while (left < right) {
                const sum = nums[i] + nums[left] + nums[right];

                // If the sum is zero, add the triplet to the result array
                if (sum === 0) {
                    result.push([nums[i], nums[left], nums[right]]);

                    // Skip duplicates in the left and right pointers
                    while (left < right && nums[left] === nums[left + 1]) {
                        left++;
                    }

                    while (left < right && nums[right] === nums[right - 1]) {
                        right--;
                    }

                    // Move pointers to the next unique pair
                    left++;
                    right--;
                } else if (sum < 0) {
                    // If sum is less than zero, move the left pointer to increase the sum
                    left++;
                } else {
                    // If sum is greater than zero, move the right pointer to decrease the sum
                    right--;
                }
            }
        }
    }

    return result;
}

// Example usage:
const nums = [-1, 0, 1, 2, -1, -4];
const result = threeSum(nums);

console.log(result);
