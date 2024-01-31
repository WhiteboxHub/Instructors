// function divide(a,b){
//     if(b===0){
//         throw new Error("we can't divide by zero")
//     }
//     else{
//         return a/b;
//     }
// }
// try {
//     const result = divide(10, 40);
//     console.log("Result:", result);
//   } catch (error) {
//     console.error("Error:", error.message);
//   }
function productExceptSelf(nums) {
    try {
      if (!Array.isArray(nums) || nums.length < 2) {
        throw new Error("Input must be an array with at least two elements.");
      }
  
      const n = nums.length;
  
      // Initialize the result array with all elements set to 1
      const result = new Array(n).fill(1);
  
      // Calculate products to the left of each element
      let leftProduct = 1;
      for (let i = 0; i < n; i++) {
        result[i] *= leftProduct;

        console.log(result[i]+"$$$$$$$");
        leftProduct *= nums[i];
        console.log(leftProduct+"***********");
      }
  
      // Calculate products to the right of each element and multiply with the result
      let rightProduct = 1;
      for (let i = n - 1; i >= 0; i--) {
        result[i] *= rightProduct;
        rightProduct *= nums[i];
      }
  
      return result;
    } catch (error) {
      console.error("Error:", error.message);
      return null; // or throw the error again based on your needs
    }
  }
  
  // Example usage
  const nums = [1, 2, 3, 4, 10];
  const output = productExceptSelf(nums);
  if (output !== null) {
    console.log(output); // Output: [240, 120, 80, 60, 24]
  }
  