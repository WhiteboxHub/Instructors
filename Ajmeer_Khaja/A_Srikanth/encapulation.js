class BankAccount {
    constructor(balance) {
      this.balance = balance; 
    }
  
    getBalance() {
      return this.balance; 
    }
  
    deposit(amount) {
      this.balance += amount;
    }
  
    withdraw(amount) {
      if (amount <= this.balance) {
        this.balance -= amount;
        console.log('collect cash');
      } else {
        console.log("Insufficient funds");
      }
    }
  }
  
  const account = new BankAccount(1000);
  console.log(account);
  account.withdraw(500)