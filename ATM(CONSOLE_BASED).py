bank_account = {
    12345:[9873.0,9989,"mahipal9988@gmail.com","6309472354"],
    23456:[6573.9,None,"akhil9872@gmail.com","8978387028"],
    78910:[3452.2,9390,"vamshi939@gmail.com","9390091863"],
    11121:[5363.2,7093,"naveen709@gmail.com","7093464735"],
    13141:[1000.2,None,"rohithreddy@gmail.com","9876543210"],
    }
print(bank_account)
while True:
    print("***********************************")
    print("WELCOME TO NIKK BANK ATM")
    print("choose your option")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statment")
    print("5. Exit")
    option = int(input("Enter your option:"))
    print("********************************")
    if option ==1:
        print("*****************************")
        account_no =int(input("Enter your account number:"))
        if account_no not in bank_account:
            print("Invalid Account Number")
        else:
            if bank_account[account_no][1] is None:
                print(f"Dear{account[account_no][3]}, Pin Not Generated")
            else:
                pin = int(input("Enter Your Pin"))
                if bank_account[account_no][1] == pin:
                    amt=int(input("Enter Amount:"))
                    if bank_account[account_no][0]>= amt:
                       bank_account[account_no][0]= bank_account[account_no][0]-amt
                       print("Amount Withdraw Sucessfull")
                    else:
                        print("Insufficient Balance")
                else:
                    print("Invalid Pin")
        print("********************************")
    elif option==2:
        print("********************************")
        account_no = int(input("Enter Your Account Number:"))
        if account_no not in bank_account:
            print("Invalid Account Number")
        else:
            amt-int(input("Enter Amount:"))
            bank_account[account_no][0] =amt
            print("Deposit Sucessfull")
        print("***********************")
    elif option==3:
        print("****************************")
        account_no = int(input("Enter Your Account Number"))
        if account_no not in bank_account:
            print("Invalid Bank Account")
        else:
            if bank_account[account_no][1] is not None:
                print("Pin Already Generated")
            else:
                pin = int(input("Enter New Pin:"))
                bank_account[account_no][1] == pin
                print("Pin Generated Sucessfully")
        print("****************************")
    elif option==4:
        print("*****************************")
        account_no = int(input("Enter Your Account Number:"))
        if account_no not in bank_account:
            print("Invalid Account Account")
        else:
            pin= int(input("Enter Your Pin:"))
            if bank_account[account_no][1] == pin:
                print(f"Name:{bank_account[account_no][-2]}")
                print(f"Email:{bank_account[account_no][-3]}")
                print(f"mobile no:{bank_account[account_no][-1]}")
                print(f"Balance:{bank_account[account_no][0]}")
            else:
                print("Invalid Pin")
        print("********************************")
    elif option ==5:
        print("********************************")
        print("Thank You")
        print("Visit Again")
        print("***************************************")
        break
                                                                                                
                                                                                                                 
                                                                                                          
                                                                
                                                                           
                                                       
                          
    
    
