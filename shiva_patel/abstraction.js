class ATM{
    constructor(withdraw){
        this.balance =10000;
   
        this.withdraw=withdraw;
    
    }
    getAmount(){
        this.minimum=500;
        // we are hideing this to restricted from miss use
        if ( (this.balance-this.withdraw)>=this.minimum)
        {
            console.log("withdraw successful")
        }
        else
        console.log("withdraw failled")
    }
}
let x = new ATM(0);

x.getAmount();