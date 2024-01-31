function* Genrat(){
    yield new Promise(resolve => setTimeout(() => resolve('first'),1000));
    yield new Promise(resolve => setTimeout(() => resolve('second'),5000));
    yield new Promise(resolve => setTimeout(() => resolve('third'),1000));
}
async function iterateAsync(){
    for await(const value of Genrat()){
        console.log(value);
    }
}
iterateAsync();




// function* numberGenerator() {
//     let i = 0;
//     while (true) {
//       yield i++;
//     }
//   }
  
//   const iterator = numberGenerator();
  
//   for (let j = 0; j < 5; j++) {
//     console.log(iterator.next().value);
//   }
  