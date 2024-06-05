function* asyncGenerator() {
    yield new Promise(resolve => setTimeout(() => resolve('First'), 1000));
    yield new Promise(resolve => setTimeout(() => resolve('Second'), 5000));
    yield new Promise(resolve => setTimeout(() => resolve('Third'), 1000));
  }
  
  async function iterateAsyncGenerator() {
    for await (const value of asyncGenerator()) {
      console.log(value);
    }
  }
  
  iterateAsyncGenerator();
  function* gen(){
   console.log("before")
   yield 
   console.log('a1')
   console.log('b2')
   yield 
   console.log('A2')
   console.log('B3')
   return
   yield
   console.log('A3')
   console.log('B4')
  }
  const i = gen();
   i.next();
   i.next();
   i.next();
   i.next();
   console.log(i.next());
