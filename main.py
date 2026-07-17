from happy import Bank

def input_pin(prompt="Enter 4-digit PIN: "):
    while True:
        pin = input(prompt)
        if pin.isdigit() and len(pin) == 4:
            return int(pin)
        print("❌ PIN must be exactly 4 digits.")

def input_account():
    acc_no = input("Enter Account Number: ").strip()
    if not acc_no:
        print("❌ Account number cannot be empty")
        return None
    return acc_no

def create_account():
    print("\n=== Create New Account ===")
    name = input("Name: ").strip()
    age = int(input("Age: "))
    email = input("Email: ").strip()
    pin = input_pin()

    user, msg = Bank.create_account(name, age, email, pin)
    print(msg)

    if user:
        print(f"✅ Your Account Number: {user['accountNo.']}")

def deposit_money():
    print("\n=== Deposit Money ===")
    acc_no = input_account()
    if not acc_no:
        return
    pin = input_pin()
    amount = int(input("Amount to deposit: "))

    success, msg = Bank.deposit(acc_no, pin, amount)
    print(msg)

def withdraw_money():
    print("\n=== Withdraw Money ===")
    acc_no = input_account()
    if not acc_no:
        return
    pin = input_pin()
    amount = int(input("Amount to withdraw: "))

    success, msg = Bank.withdraw(acc_no, pin, amount)
    print(msg)

def show_details():
    print("\n=== Account Details ===")
    acc_no = input_account()
    if not acc_no:
        return
    pin = input_pin()

    user = Bank.find_user(acc_no, pin)
    if user:
        print("\n--- Account Info ---")
        print(f"Name   : {user['name']}")
        print(f"Email  : {user['email']}")
        print(f"Balance: {user['balance']}")
    else:
        print("❌ Account not found")

def update_info():
    print("\n=== Update Account Info ===")
    acc_no = input_account()
    if not acc_no:
        return
    pin = input_pin("Enter current PIN: ")

    name = input("New Name (leave blank to skip): ").strip()
    email = input("New Email (leave blank to skip): ").strip()
    new_pin_input = input("New PIN (leave blank to skip): ").strip()

    new_pin = int(new_pin_input) if new_pin_input.isdigit() else None
    name = name if name else None
    email = email if email else None

    success, msg = Bank.update_user(acc_no, pin, name, email, new_pin)
    print(msg)

def delete_account():
    print("\n=== Delete Account ===")
    acc_no = input_account()
    if not acc_no:
        return
    pin = input_pin()

    confirm = input("⚠️ Are you sure? (yes/no): ").lower()
    if confirm != "yes":
        print("❌ Deletion cancelled")
        return

    success, msg = Bank.delete_user(acc_no, pin)
    print(msg)

def main():
    while True:
        print("""
🏦 SIMPLE BANK SYSTEM
---------------------
1. Create Account
2. Deposit
3. Withdraw
4. Show Details
5. Update Info
6. Delete Account
7. Exit
""")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            show_details()
        elif choice == "5":
            update_info()
        elif choice == "6":
            delete_account()
        elif choice == "7":
            print("👋 Thank you for using the Bank App!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
