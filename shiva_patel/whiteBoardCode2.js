//findpairssumisequaltothetarget
function findPairsWithSum(arr, targetSum) {
    const pairs = [];
    const visitedNumbers = new Set();
  
    for (let num of arr) {
      const complement = targetSum - num;
  
      if (visitedNumbers.has(complement)) {
        pairs.push([num, complement]);
      }
  
      visitedNumbers.add(num);
    }
  
    return pairs;
  }
  
  const numbersArray = [1, 2, 3, 4, 5, 6];
  const targetSum = 7;
  
  const resultPairs = findPairsWithSum(numbersArray, targetSum);
  console.log(resultPairs);