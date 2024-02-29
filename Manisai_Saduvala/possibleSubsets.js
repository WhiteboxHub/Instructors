function generateSubsets(arr, index = 0, currentSubset = [], result = []) {
    if (index === arr.length) {
      result.push([...currentSubset]);
      return;
    }
  
    // Exclude the current element
    generateSubsets(arr, index + 1, currentSubset, result);
  
    // Include the current element
    currentSubset.push(arr[index]);
    generateSubsets(arr, index + 1, currentSubset, result);
    currentSubset.pop();
  }
  
  // Example usage:
  const inputArray = [1, 2, 3];
  const subsets = [];
  generateSubsets(inputArray, 0, [], subsets);
  
  console.log("All Subsets:", subsets);
  
