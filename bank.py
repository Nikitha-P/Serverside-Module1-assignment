class Bank():
    def __init__(self,owner, balance):
        self.owner=owner
        self.balance=balance

    def withdrawl(self,amount):
        if amount>self.balance:
            print("No sufficient amount")
        elif amount<0:
            print("Insufficient funds")
        else:
            self.balance=self.balance-amount
            return self.owner+" account's balance after withdrawing "+str(amount)+" rupees is " +str(self.balance)

    def deposit(self,amount):
        if amount>self.balance:
            print("No sufficient amount")
        elif amount<0:
            print("Insufficient funds")
        else:
            self.balance=self.balance+amount
            return self.owner+" account's balance after depositing "+str(amount)+" "+"rupees is " +str(self.balance)
        

def main():
    owner=input()
    balance=int(input())
    obj=Bank(owner,balance)
    
    n=int(input())
    for i in range(n):
        s=input().split(" ")
        if s[0]=="withdrawl":
            print(obj.withdrawl(float(s[1])))
        elif s[0]=="deposit":
            print(obj.deposit(float(s[1])))

if __name__=="__main__":
    main()


