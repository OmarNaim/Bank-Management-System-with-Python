class Bank:
    bank_amount = 10000000
    bank_loan_amount = 0 


class User(Bank):
    
    user_ids = []
    can_take_loan = True

    def __init__(self,name,email,address,acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.balance = 0
        self.acc_num = self.generate_account_number()
        self.transaction_history = []
        self.loan_number = 2
        self.loan_amount = 0
        User.user_ids.append(self)



    def generate_account_number(self):
        return self.name+self.email

    def deposit(self,amount):
        if(amount > 0):
            self.balance+=amount
            Bank.bank_amount+=amount
            self.record_transaction("Deposit",amount)
        else:
            print("Invalid amount for Deposit.")
        

    def withdraw(self,amount):
        if(amount > self.balance):
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            Bank.bank_amount-=amount
            self.record_transaction("Withdraw",amount)

    def check_balance(self):
        print(f"Balance is: {self.balance}")

    def record_transaction(self, transaction_type, amount):
        print("Transaction added.")
        transaction_info = f"{transaction_type} : {amount}"
        self.transaction_history.append(transaction_info)


    def transiction_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self,amount):
        if User.can_take_loan == True:    
            if self.loan_number>0:
                self.loan_number -= 1
                self.loan_amount += amount
                self.balance+=amount
                Bank.bank_loan_amount+=amount
                self.record_transaction("Loan",amount)
                print(f"You have take loan : {amount}")
                print(f"Remaining Loan : {self.loan_number}")
            else:
                print("You have already taken the maximum number of loans.")
        
        

    def see_loan_amount(self):
        print(f"Loan amount: {self.loan_amount}")

    def transfer_amount(self, recipient_id, amount):
        for user in User.user_ids:
            if user.acc_num == recipient_id:
                if self.balance >= amount:
                    user.balance += amount
                    self.balance -= amount
                    self.record_transaction(f"Transfer to {recipient_id}", amount)
                    user.record_transaction(f"Transfer from {self.acc_num}", amount)
                    print(f"Transfer successful. Remaining balance: {self.balance}")
                else:
                    print("Not enough balance for the transfer.")
                return
        print("Recipient account not found.")
           
        
    def loan_condition():
        if User.can_take_loan == True:
            return True
        else:
            return False


class Admin(User,Bank):

    def __init__(self,name):
        self.name = name
    
    def delete_user_account(self,id):
        for user in User.user_ids:
            if user.acc_num == id:
                User.user_ids.remove(id)
        print("Account does not exist.")

    
    def see_user_account(self):
        for user in User.user_ids:
            print(user.acc_num)


    def bank_balance(self):
        print(f"Total bank balance is: {Bank.bank_amount}")


    def total_loan_amount(self):
        print(f"Total loan amount is: {Bank.bank_loan_amount}")


    def loan_feature(self,str):
        if str.lower() == "on":
            User.can_take_loan = True
        elif str.lower() == "off":
            User.can_take_loan = False
        else:
            print("Invalid command")

    




while(True):
    print("Are you: ")
    i = int(input("1.User 2.Admin 3.Exit "))

    if(i==3):
        break
    
    while(i==1): #user
        print("1.Creat account.")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Check Balance")
        print("5.Transaction history")
        print("6.Take Loan")
        print("7.Transfer amount")
        print("8.Exit")
        n = int(input())

        if(n == 1):
            print("Give name,email,address,account type(Saving / Current) (Use comma)")
            name,email,address,account_type = input().split(',')
            obj = User(name,email,address,account_type)
        elif(n==2):
            depo = int(input("Enter deposit ammount: "))
            obj.deposit(depo)
        elif(n==3):
            withd = int(input("Enter withdraw ammount: "))
            obj.withdraw(withd)
        elif(n==4):
            obj.check_balance()
        elif(n==5):
            obj.transiction_history()
        elif(n==6):
            if obj.loan_condition == True:
                loan_amount = int(input("enter loan amount: "))
                obj.take_loan(loan_amount)
            else:
                print("Bank wont allow to take loan")
            
        elif(n==7):
            id = input("Enter the id for transfer: ")
            money = int(input("Enter amount: "))
            obj.transfer_amount(id,money)
        elif(n==8):
            break


    while(i==2): #admin
        print("1.Creat account.")
        print("2.Delete any user account")
        print("3.See all user accounts")
        print("4.Check the total available balance of the bank.")
        print("5.Check the total loan amount. ")
        print("6.On or Off the loan feature of the bank")
        print("7.Exit")
        n = int(input())

        if(n == 1):
            print("Give name")
            name = input()
            adn = Admin(name)
        elif(n==2):
            id = int(input("Enter id you want to delete: "))
            adn.delete_user_account(id)
        elif(n==3):
            print("See all user accounts list:")
            adn.see_user_account()
        elif(n==4):
            adn.bank_balance()
        elif(n==5):
            adn.total_loan_amount()
        elif(n==6):
            loan_mode = input("Turn on or off the loan feature of the bank? (print : on/off) - ")
            adn.loan_feature(loan_mode)
        elif(n==7):
            break


        