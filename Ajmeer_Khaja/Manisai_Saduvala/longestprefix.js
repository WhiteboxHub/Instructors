// Finding the longest prefix in an given array
// let n be the lengthof an array
//Have to check and iterate over the array to find the matching prefix over evry element
// return the longest prefix which matches to evefry element in array
// else return empty array

function getLongestPrefix(arr)
{
  // first element to check
    let first = arr[0].split('');
 // last element to validate
    let last = arr[arr.length-1].split('');
// an empty array to push and return 
    let results = [];
// iterating over the array of elements
    for (let i = 0; i< arr.length; i++)
    {
      // Base condition for checking whether the element has even one character same
        if(first[i]!==last[i])
        break;
      //if the characters are matching push to results array
        results.push(first[i])
    }
  // return results within string
    return results.join('');

}
// sorting array 
const arr = ['Bad','Barber','Bank'].sort();
console.log(getLongestPrefix(arr))
