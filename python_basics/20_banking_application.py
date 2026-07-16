print("==================================")
print("Hello welcome to python bank")
print("==================================")
balance = 0.0

def check_balance():
    print("*** checking balance ***")
    print(f"your current balance is {balance} rupees")


def deposit_money():
    print("*** depositing money ***")
    money = int(input("Enter your money to be deposited:"))
    if money >= 0:
        global balance
        balance = balance + money
        print(f"your current money is {balance} rupees")
    else:
        print("invalid money")

def withdraw_money():
    print("*** withdrawing money ***")
    money = int(input("Enter your money to be withdrawn:"))
    global balance

    if money > balance:
        print("!!! insufficient balance !!!")

    elif money >= 0:
        balance = balance - money
        print(f"your current money is {balance} rupees")
    else:
        print("invalid money")



while True:
    print("1. show balance")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. exit")
    choice = input("Enter your choice:")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit_money()
    elif choice == '3':
        withdraw_money()
    elif choice == '4':
        break
    else:
        print("Invalid choice")

print("==================================")
print("Thank you for banking with us !!!")
print("==================================")