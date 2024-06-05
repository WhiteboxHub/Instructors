class shop {
    constructor (a,b,c){
        this.mobile=a;
        this.price = b;
        this.ram=c;

    }
    newRam (nr){
        this.ram=nr;
    }
}
let m1 = new shop('1pluse','20000','6gb');
console.log(m1);
let m2 = new shop('iPhone','100000','8gb');
console.log(m2);
m2.newRam('10gb');
console.log(m2)

