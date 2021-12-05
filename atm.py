class Atm(object):
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin

    def BalanceEnquiry(self):
        print("Your balance is 1000$")

    def CashWithdrawal(self, amount):
        newBalance = 1000 - amount
        print("You withdrew " + str(amount) + ", Remaining balance is " + str(newBalance))

def main():
    name = input("Hi, please tell me your name: ")
    print("Hello " + name)

    card = input("Please give your card number: ")
    pin = input("Please give your pin: ")

    newUser = Atm(card, pin)

    print("Choose what you want to do: ")
    print("1. Cash Withdrawal")
    print("2. Balance Enquiry")

    action = int(input("Please give the number next to the action you want to perform: "))

    if(action == 1):
        amount = int(input("Choose the amount you want to withdraw: "))
        newUser.CashWithdrawal(amount)
    elif(action == 2):
        newUser.BalanceEnquiry()
    else:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()