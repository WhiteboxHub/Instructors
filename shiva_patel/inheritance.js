class Parent {
    getMasg(){
        console.log("hello parentclass");
    }
}
class Child extends Parent{

}
let obj = new Child();
obj.getMasg();