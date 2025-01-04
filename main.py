import random

def user_menu():
    while True:
        print('''
        🌟 Welcome to the Password Generator 🌟
        
        1️⃣ Generate a password
        2️⃣ Exit
        ''')
        
        user_choice = input("👉 Choose an option: ")
        
        if user_choice == "1":
            pass_length = input("🔢 Please input the desired length: ")
            if not pass_length.isdigit() or int(pass_length) >= 30 or int(pass_length) <= 0:
                print("⚠️ The input is too long, too short, or not numerical!")
            else:
                passgen(int(pass_length))
                break
        elif user_choice == "2":
            print("👋 Goodbye!")
            exit()
        else:
            print("❌ Invalid option, please try again.")

def passgen(length):
    lower = "thebrownfoxjumpsoverthelazydog"
    upper = lower.upper()
    digits = "1234567890"
    specials = "!@#$%^&*()_+-="
    charset = lower + upper + digits + specials

    output = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(specials)
    ]

    while len(output) < length:
        output.append(random.choice(charset))

    random.shuffle(output)
    print("🔑 Generated Password:", ''.join(output))

    while True:
        user_after_gen_choice = input('''
        🤖 Thanks for using this free piece of software!
        
        1️⃣ Generate another password
        2️⃣ Go back to the menu
        3️⃣ Exit
        👉 Your choice: ''')

        if user_after_gen_choice == "1":
            passgen(length)
            break
        elif user_after_gen_choice == "2":
            return
        elif user_after_gen_choice == "3":
            print("👋 Goodbye!")
            exit()
        else:
            print("❌ Invalid choice, please try again.")

def main():
    user_menu()
    
if __name__ == "__main__":
    main()
