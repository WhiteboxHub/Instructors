
function longestCommonPrefix(strs) {
    // Sort the array
    strs.sort();

    // Get the first and last strings
    const first = strs[0].split('');
    const last = strs[strs.length - 1].split('');

    // creating an empty array to store the result
    const result = [];

    // Start comparing
    for (let i = 0; i < first.length; i++) {
        if (first[i] !== last[i]) {
            break;
        }
        result.push(first[i]);
    }
    return result.join('');
}

// Example usage:
const inputArray = ["flower", "flow", "flight"];
console.log(longestCommonPrefix(inputArray));  // Output: "fl"

// UNIT TEST CASES :

//---------------------------- case1 ----------------------------
// const inputArray = ["a", "a", "a"];
// console.log(longestCommonPrefix(inputArray));  // Output: "a"


//---------------------------- case2 ----------------------------
// const inputArray = ["aa", "aab", "aabc"];
// console.log(longestCommonPrefix(inputArray));  // Output: "aa"


//---------------------------- case3 ----------------------------
// const inputArray = ["a", "b", "c"];
// console.log(longestCommonPrefix(inputArray));  // Output: ""
