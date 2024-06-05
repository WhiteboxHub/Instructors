function longestCommonPrefix(strings) {
    // Check if the input is an array and it contains only strings
    if (!Array.isArray(strings) || strings.length < 2 || strings.some(str => typeof str !== 'string')) {
      throw new Error('Input must be an array containing only strings and length should be greater than 2.');
    }
  
    // Sort the array of strings to ensure that the shortest string comes first
    strings.sort();
  
    const firstStr = strings[0];
  
    let commonPrefix = "";
  
    // Iterate through the characters from index 0 to the last index of the first string
    for (let i = 0; i < firstStr.length; i++) {
      // Check if the character at the current position is the same in all strings
      if (strings.every(str => str.charAt(i) === firstStr.charAt(i))) {
        commonPrefix += firstStr.charAt(i);
      } else {
        // If a mismatch is found, break the loop
        break;
      }
    }
  
    return commonPrefix;
}

// Example usage:
const stringsArray = ['s'];
const result = longestCommonPrefix(stringsArray);
console.log(result); // Output: Error: Input must be an array containing only strings and length should be greater than 1.
