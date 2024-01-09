class User:
    def __init__(self,name,age:int,gender):
        self.name= name
        self.gender= gender
        self.age= age

    def show_user_details(self):
        print("Personal details\n")
        print(f"name, {self.name}")
        print(f"gender, {self.gender}")
        print(f"age, {self.age}")

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0  

    def deposits(self,amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Amount balance has been updated to, {self.balance}")

    def withraw(self,amount):
        if self.amount > self.balance:
            print(f"Insufficient fund, Balance available = {self.balance}")
        else:
            self.balance -= self.amount
            print(f"Your account balance has beem updated to {self.balance}")

    def view_balance(self):
        super().show_user_details()
        print(f"Your account balance has been updated to {self.balance}")

def main():
    user=User("Samuel", 24, "Male")

    user.show_user_details()

    bank=Bank("Samuel", 24, "Male")
    bank.deposits(1888)
    bank.withraw(30)
    bank.view_balance()


if __name__ =="__main__" :
    main()