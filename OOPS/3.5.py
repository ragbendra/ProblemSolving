def main():
    atm = ATM(1000,1234)
    
    while True:
        print("Welcome to the ATM mahcine.")
        pin = int(input("Please enter your pin: "))
        
        if pin != atm.pin:
            print("Incorrect PIN. Please try again.")
            continue
        
        print("\nMenu")
        print("!. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")
        
        option = int(input("\nEnter your choice: "))
        
        if option == 1:
            print("Current balance:",atm.check_balance())
            
        elif option == 2:
            amount = float(input("Enter the amount to deposit: "))
            print(atm.withdraw(amount))
            
        elif option == 3:
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))
        
        elif option == 4:
            new_pin = int(input("Enter your new PIN: "))
            print(atm.change_pin(new_pin))
            
        elif option == 5:
            print("thank you for using the ATM machine.")
            break 
        
        else:
            print("Invalid Option. Please try again. ")

if __name__ == "__main__":
    main()            