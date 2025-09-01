balance=1000.0
pin_code =1234

print("***welcome to ATM Menu***")


user_pin=int(input("Enter your Four digit[0-9] pin code : "))


if pin_code==user_pin:
    while True:
        print('''
              -------------ATM Menu----------------
              1.Balance Enquiry
              2.Withdraw funds
              3.Deposite Funds
              4.Exit
              ''')
        choice=input("Enter your choice among above [1-4] : ")
        if choice == '1':
            print(f"Your Total balance is Rs.{balance}")
        
        elif choice == '2':
            withdraw_amt=float(input("Enter your withdraw amount Rs . "))
            if balance>=withdraw_amt:
                balance -=withdraw_amt
                print(f"{withdraw_amt} is debit from your account.Now Total balance is Rs.{balance}")
                break
            else:
                print("insufficient balance")
                break
        elif choice == '3':
            deposite_amt=float(input("Enter your deposite amount Rs. "))
            balance += deposite_amt 
            print(f"{deposite_amt} is credit in your account . Now Total Balance is Rs.{balance}")
            
        elif choice=='4':
            print("thanks for visit ")
            break
            

else:
    print("wrong pin code ,please try again")
