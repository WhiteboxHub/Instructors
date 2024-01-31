// Find the first non repeating characters of a given string
// Given a string of length n so, have to find the first non-repeating element of a string
// consider a String for example input ="Welcome", here the first non-repeating char will be W
// i/p = 'Welcome'
// o/p = 'W'
function firstNonRepeatingCharacter(str) {
    const characterCount = {};
    // counting the occurances of characters in a string 
    for (let x of str) {
      characterCount[x] = (characterCount[x] || 0) + 1;
    }
    // finding  the first non-repeating character
    for (let x of str) {
      if (characterCount[x] === 1) {
        return x;
      }
    }
    // If no return null
    return null;
  }
  const input= "innovapath";
  const output = firstNonRepeatingCharacter(input); 
  console.log(`The first non-repeating chafracter in string is : ${output}`);// i
  // Big O-notation => O(n)- linear
