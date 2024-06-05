function reverseStringWords(sentence)
{
    // split string to an array
   let splitString = sentence.split(' ');
   // map every word in the array
   let temp = splitString.map(word=>{
       // now split every string character
       let reverseIt = word.split('');
     //  console.log(reverseIt)
       // reverser string in order
       let reversedWordArray = reverseIt.reverse();
     //  console.log(reversedWordArray)
       // make it return to array of word
       return reversedWordArray.join('');
   });
   // join and fallback to original; string
   return temp.join(' ');
}
const str = 'Hello World';
const getResults = reverseStringWords(str);
console.log(getResults)
