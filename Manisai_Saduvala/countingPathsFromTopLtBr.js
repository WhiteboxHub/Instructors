function factorial(n) {
    // finding the factorial of n
    if (n <= 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function countPathsLinear(m, n) {
    //mathematical formula for counting paths from top left to right bottom(m+n-2/m-1)
    const totalSteps = m + n - 2;
    const downSteps = m - 1;
    const paths = factorial(totalSteps) / (factorial(downSteps) * factorial(totalSteps - downSteps));
    return paths;
}

// Example usage:
const m = 3; // Number of rows
const n = 3; // Number of columns
console.log("Total paths:", countPathsLinear(m, n));
