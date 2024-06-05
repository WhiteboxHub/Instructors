class Person {
    constructor(name,age,salary){
        this.name=name;
        this.age=age;
        this.salary=salary;

    }
    getName(){
        console.log(this.name);
    }
    getAge(){
        console.log(this.age)
    }
    getSalary(){
        console.log(this.salary)
    }
}
let pDetails = new Person("shivapatel",23,20000);
pDetails.getName();
pDetails.getAge()