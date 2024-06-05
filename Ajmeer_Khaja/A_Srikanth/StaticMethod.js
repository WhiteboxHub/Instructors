class person {
    constructor(name,birthYear,gender){
        this.name=name;
        this.birthYear=birthYear;
        this.gender=gender;
    }
    calcAge(){
        console.log(new Date().getFullYear()-this.birthYear);
    }
    static greet(){
        console.log('hey there how r u');
    }
}
let john=new person('john',1990,'male');
console.log(john);
person.greet();