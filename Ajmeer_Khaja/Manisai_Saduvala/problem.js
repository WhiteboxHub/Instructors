function arrangeElements(arr) {
    const counts = { 'a': 0, 'b': 0, 'c': 0 };

    // Count occurrences of 'a', 'b', and 'c'
    for (const element of arr) {
        counts[element]++;
    }

    // Reconstruct the array based on counts
    const result = Array(counts['a']).fill('a').concat(Array(counts['b']).fill('b'), Array(counts['c']).fill('c'));

    return result;
}

// Test cases
const testCase1 = ['a', 'b', 'c', 'a', 'c', 'a', 'b', 'c'];
const testCase2 = ['c', 'b', 'a', 'c', 'a', 'b', 'c', 'a'];

console.log("Input:", testCase1);
console.log("Output:", arrangeElements(testCase1));
