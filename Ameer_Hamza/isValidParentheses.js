function isValidParentheses(s) {
  // Handle edge cases
  if (s === null || typeof s !== "string") {
    throw new Error("Invalid input. Please provide a valid string.");
  }

  const stack = [];
  const pairs = { "(": ")", "{": "}", "[": "]" };

  for (let char of s) {
    if (char in pairs) {
      stack.push(char);
    } else if (stack.length === 0 || pairs[stack.pop()] !== char) {
      return false;
    }
  }

  // Check if the stack is empty, indicating all parentheses are matched
  return stack.length === 0;
}
console.log(`Test Case 1: Is "${"({[]})"}" valid?${isValidParentheses("({[]})")}`); // true
console.log(`Test Case 1: Is "${"({[]})"}" valid?${isValidParentheses("({})")}`); // true
console.log(`Test Case 1: Is "${"({[]})"}" valid?${isValidParentheses("")}`); // true
console.log(`Test Case 1: Is "${"({[a]})"}" valid?${isValidParentheses("({[a]})")}`); // false
console.log(`Test Case 1: Is "${"({]})"}" valid?${isValidParentheses("({]})")}`); // false
console.log(`Test Case 1: Is "${"({[]})"}" valid?${isValidParentheses("({[])")}`); // true
