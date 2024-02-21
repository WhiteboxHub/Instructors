// Function to showcase amplitude in a textual format
function showcaseAmplitude(amplitude) {
    const numberOfPoints = 50;  // You can adjust this value to change the number of points

    for (let i = 0; i < numberOfPoints; i++) {
        const value = Math.sin((i / numberOfPoints) * (2 * Math.PI)) * amplitude;
        const bar = '*'.repeat(Math.abs(value) * 10);
        
        console.log(bar);
    }
}

// Example usage
const myAmplitude = 3;  // You can change this value to adjust the amplitude
showcaseAmplitude(myAmplitude);
