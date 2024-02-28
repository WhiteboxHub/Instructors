
// function to swap the characters in an array
function swap(array, index1, index2) {
    let temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
}
// Generate permutations using array of characters
function generatePermutations(characters, start, end) {
    if (start === end) {
        console.log(characters.join(''));
    } else {
        for (let i = start; i <= end; i++) {
          // call the swap function recursively
            swap(characters, start, i);
          // Call generatePermutations recursievly
            generatePermutations(characters, start + 1, end);
          // Backtrack the character positions
            swap(characters, start, i); // backtrack
        }
    }
}

let inputString = ['A', 'B', 'C'];
let lengthOfString = inputString.length;
generatePermutations(inputString, 0, lengthOfString - 1);
