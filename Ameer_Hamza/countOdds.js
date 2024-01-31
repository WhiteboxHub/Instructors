function countOdds(low, high) {
  // Validating input
  if (!Number.isInteger(low) || !Number.isInteger(high) || low > high) {
    throw new Error(
      "Invalid input. Please provide valid integer values with low <= high."
    );
  }

  const oddNumbers = [];

  for (let num = low; num <= high; num++) {
    if (num % 2 === 1) {
      oddNumbers.push(num);
    }
  }
  return oddNumbers.length;
}

// Test cases:
try {
  console.log("Count of Odd Numbers:", countOdds(3, 7));
  console.log("Count of Odd Numbers:", countOdds(1, 7));
  console.log("Count of Odd Numbers:", countOdds(3, 6));
  console.log("Count of Odd Numbers:", countOdds(3, "7")); // error : Please provide valid integer values with low <= high
  console.log("Count of Odd Numbers:", countOdds(4, 2)); // error : Please provide valid integer values with low <= high
} catch (error) {
  console.error(error.message);
}
