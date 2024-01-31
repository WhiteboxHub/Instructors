function arraysIntersection(nums1, nums2) {
  // Handle edge cases
  if (!Array.isArray(nums1) || !Array.isArray(nums2)) {
    throw new Error("Invalid inputs. Please provide valid arrays.");
  }

  const result = [];

  for (let num1 of nums1) {
    const indexInNums2 = nums2.indexOf(num1);

    if (indexInNums2 !== -1) {
      result.push(num1);
      // Remove the found element in nums2 to handle duplicates
      nums2.splice(indexInNums2, 1);
    }
  }

  return result;
}

console.log(arraysIntersection([], [])); // output - []
console.log(arraysIntersection([1, 2, 3, 4], [])); // output - []
console.log(arraysIntersection([], [3, 4, 5, 6])); // output - []
console.log(arraysIntersection([1, 2, 3, 4], [3, 4, 5, 6])); // output - [3,4]
console.log(arraysIntersection([1, 2, 3, 4], "3, 4")); // output - Error("Invalid inputs. Please provide valid arrays.");
console.log(arraysIntersection(4, [3, 4, 5, 6])); // output - Error("Invalid inputs. Please provide valid arrays.");
