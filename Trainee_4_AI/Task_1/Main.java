class BankAccount {
    private final String account_holder_name;
    private final int account_number;
    private int balance;

    public BankAccount(String account_holder_name, int account_number) {
        this.account_holder_name = account_holder_name;
        this.account_number = account_number;
        this.balance = 0;
    }

    public void deposit(int amount){
        balance += amount;
        System.out.println("You have deposited: " + amount + "€");
    }

    public void withdraw(int amount) {
        if (amount > balance) {
            System.out.println("Sorry, you only have " + balance + "€ in your account you cannot withdraw " + amount + "€");
        }
        else {
            balance -= amount ;
            System.out.println("You have withdrawed: " + amount + "€ from your account");
        }
    }

    public void get_account_info () {
        System.out.println("The holder of the account: " + account_holder_name);
        System.out.println("The number of the account: " + account_number);
        System.out.println("Current balance: " + balance + "€");
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount("Taha Othman",500500);
        System.out.println("Hello, Welcome to AgrinBank");
        System.out.println("--------------------------------------------------");
        account.get_account_info();
        System.out.println("--------------------------------------------------");
        account.deposit(500);
        System.out.println("--------------------------------------------------");
        account.withdraw(200);
        account.withdraw(500);

    }
}