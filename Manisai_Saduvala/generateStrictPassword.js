function generateRandomNumbersWithConstraints(n) {
    const result = [];
  
    while (result.length < n) {
      const randomNumber = Math.floor(100 + Math.random() * 900);
      const digits = randomNumber.toString().split('');
  
      // Check for three equal digits or two subsequent equal digits
      if (!(digits[0] === digits[1] && digits[1] === digits[2]) &&
          !(digits[0] === digits[1] && digits[1] === digits[2])) {
        result.push(randomNumber);
      }
    }
  
    return result;
  }
  
  // Example usage:
  const n = 3;
  const randomNumbers = generateRandomNumbersWithConstraints(n);
  console.log(`Generated ${n} random numbers with constraints:`, randomNumbers);
