function reverseEvenIndices(inputString) {
    if (typeof inputString !== 'string') {
        console.log('Input must be a string.');
        return;
    }

    const length = inputString.length;
    let result = '';

    for (let i = 0; i < length; i++) {
        if (i % 2 === 0) {
            result += inputString[i];
        } else {
            result += inputString[length - 1 - i];
        }
    }

    return result;
}

// Example: Reverse even indices in the string "abcdefgh"
const inputString = "abcdefgh";
const reversedString = reverseEvenIndices(inputString);
console.log(reversedString); // Output: "hgfedcba"
