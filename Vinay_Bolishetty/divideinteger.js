function bitwiseDivide(dividend, divisor) {
    // Get the absolute values of dividend and divisor
    const absDividend = Math.abs(dividend);
    const absDivisor = Math.abs(divisor);

    if (absDivisor === 0) {
        throw new Error("Division by zero");
    }

    let quotient = 0;
    let remainder = 0;

    // Perform division using bitwise shifting and subtraction
    for (let i = 31; i >= 0; i--) {
        remainder = (remainder << 1) | ((absDividend >> i) & 1);

        if (remainder >= absDivisor) {
            remainder -= absDivisor;
            quotient |= (1 << i);
        }
    }

    // Determine the sign of the quotient
    if ((dividend < 0) !== (divisor < 0)) {
        quotient = -quotient;
    }

    return [quotient, remainder];
}

// Example usage
const [quotient, remainder] = bitwiseDivide(-50, 7);
console.log("Quotient:", quotient);
console.log("Remainder:", remainder);
