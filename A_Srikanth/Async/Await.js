// async function fun(){
//     return 'Hello';
// }fun()

// async function fun() {
//     return 'Hello';
// }

// async function executeAsyncFunction() {
//     const result = await fun();
//     console.log(result);
// }

// executeAsyncFunction();


// function fun(){
//     return Promise.resolve('hello')
// }
// async function fun1() {
//         const result = await fun();
//         console.log(result);
//     }
    
//     fun1();



// async function example() {
//     try {
//         const result1 = await asynchronousOperation1();
//         const result2 = await asynchronousOperation2(result1);
//         console.log(result2);
//     } catch (error) {
//         console.error('Error:', error);
//     }
// }

// example();




function asynchronousOperation1() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('Result from asynchronousOperation1');
        }, 1000);
    });
}

function asynchronousOperation2(result) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(`Result from asynchronousOperation2 with input: ${result}`);
        }, 500);
    });
}

async function example() {
    try {
        const result1 = await asynchronousOperation1();
        const result2 = await asynchronousOperation2(result1);
        console.log(result2);
    } catch (error) {
        console.error('Error:', error);
    }
}

example();
