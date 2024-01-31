class Parent {
    getMasg(){
        console.log("hello parentclass");
    }
}
class Child extends Parent{
    getMasg(){
        console.log("hello childclass");
    }
}
let obj = new Child();
obj.getMasg();