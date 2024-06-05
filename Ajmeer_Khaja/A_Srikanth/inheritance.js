

class Animal{
    data(name,breed,colour){
      this.name='dog';
      this.breed='lab';
      this.colour='brown';
      console.log(name,breed,colour);
    }
  }
  class Dog extends Animal{
  
  }
  const property=new Dog()
  // property('Dog','lab','brown')
  property.data('Dog','lab','brown');