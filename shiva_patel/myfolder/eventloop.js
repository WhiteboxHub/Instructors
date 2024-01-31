console.log('Start');

function asyncFunction() {
  setTimeout(() => {
    console.log('Async function callback');
  }, 2000);
}

asyncFunction();

console.log('End');
