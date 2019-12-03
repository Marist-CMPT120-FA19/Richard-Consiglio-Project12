#Richie Consiglio

class Account:

    def __init__(self , id , pin , savings , checking):
        self.ID = id
        self.PIN = pin
        self.savings = int(savings)
        self.checking = int(checking)
        
    def ID(self):
        return self.ID
        
    def PIN(self):
        return self.PIN
        
    def Savings(self):
        return self.savings
        
    def Checking(self):
        return self.checking
        
    def withdraw(self , account , amm):
        if account == "savings":
            self.savings = self.savings - int(amm)
        elif account == "checking":
            self.checking = self.checking - int(amm)

    def transfer(self , toAcc , amm):
        if toAcc == "savings":
            self.savings = self.savings + int(amm)
            self.checking = self.checking - int(amm)
        elif toAcc == "checking":
            self.savings = self.savings - int(amm)
            self.checking = self.checking + int(amm)
            
    def toString(self):
        return str(str(self.ID) + "\t" + str(self.PIN) + "\t" + str(self.savings) + "\t" + str(self.checking))
        
def checkCredentials(id , pin):
    accountsFile = open("accts.txt" , "r")
    for i in accountsFile:
        a = createAccount(i.split("\t"))
        if id == a.ID():
            if pin == a.PIN():
                accountsFile.close()
                return True        
                
def createAccount(info):
    return Account(info[0] , info[1] , info[2] , info[3])
    
def accountMenu(acc):    
    
    b = True
    while b:
        print("Your current balance is " , acc.Savings() , " in Savings Account $\n and $" , acc.Checking(), "in Checking account")
        print("\nSelect an option: \n1) Withdraw \n2) Transfer funds \n3) Quit")
        action = int(input("Answer with 1, 2, or 3: "))
        if action == 1:
            ammount = int(input("Enter how much you would like to withdraw: "))
            account = input("pick an account: ")
            if account.lower() == "savings":
                if ammount <= acc.Savings():
                    acc.withdraw(account.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("Your bank account balance is too low.")
            elif account.lower() == "checking":
                if ammount <= acc.Checking():
                    acc.withdraw(account.lower() , ammount)
                    print("Success!\n")
                else:
                    print("Your bank account balance is too low.")
        elif action == 2:
            ammount = int(input("Enter amount to transfer: "))
            account = input("Select an account: ")
            if account.lower() == "savings":
                if ammount <= acc.Savings():
                    acc.transfer(account.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("Your bank account balance is too low.")
            elif account.lower() == "checking":
                if ammount <= acc.Checking():
                    acc.transfer(acc.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("Your bank account balance is too low.")
                    print("Please try again \n")
        elif action == 3:
            b = False
        else:
            print("Incorrect info, please try again \n")
            
    accountsFile = open("accts.txt" , "r")
    counter = -1
    newFile = []
    for i in accountsFile:
        counter += 1
        newFile = newFile + [i]
        if i.split("\t")[0] == acc.ID():
            newFile[counter] = acc.toString()
        else:
            newFile[counter] = i
    accountsFile.close()
    accountsFile = open("accts.txt" , "w")
    for i in range(counter+1):
        accountsFile.write(newFile[i])
        if i == 0:
            accountsFile.write("\n")
    accountsFile.close()
            
def main():
    
    b = True
    while b:
        id = input("Enter account number: ")
        pin = input("Enter PIN number: ")
        
        if checkCredentials(id , pin):
            b = False
            accountsFile = open("accts.txt" , "r")
            for i in accountsFile:
                a = createAccount(i.split("\t"))
                if id == a.ID():
                    if id == a.PIN():
                        accountMenu(a)
        else:
            print("Wrong Sign in info, please try again!\n")
    
if __name__ == '__main__':
    main()
