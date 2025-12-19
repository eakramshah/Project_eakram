from menu import logo, espresso, cappuchino, latte
total_bill = 0  #Declared global variable so that we can call it inside order function
def coffee_menu():
    print(logo, "\n")

    choice = input(
        "Hi! How's your day?\nMay I take your order? Type Y or N: "
    ).lower()

    if choice != 'y':
        print("No order. Thank you, have a nice day!")
        return

    order()


def order():
    global total_bill #Global Funtion Called here
    while True:
        choice_coffee = input(
            f"\nWe have:\n"
            f"Espresso (E / 1)\n{espresso}\n"
            f"Latte (L / 2)\n{latte}\n"
            f"Cappuccino (C / 3)\n{cappuchino}\n"
            "Your choice: "
        ).lower()

        if choice_coffee in ('e', '1'):
            print(f"\nHere is your coffee ☕\n{espresso}\nThat will be $2")
            total_bill+=2

        elif choice_coffee in ('l', '2'):
            print(f"\nHere is your coffee ☕\n{latte}\nThat will be $3")
            total_bill+=3
        elif choice_coffee in ('c', '3'):
            print(f"\nHere is your coffee ☕\n{cappuchino}\nThat will be $4")
            total_bill+=4
        else:
            print("Invalid choice. Try again.")
            continue

        more = input("Do you want to order more? (Y/N): ").lower()
        if more != 'y':
            
            print("\n🧾 FINAL BILL")
            print(f"Total amount : ${total_bill}")
            money=int (input("Please enter currency nomination !\n"))
            if money >total_bill:
                print(f"here is you change ! {money-total_bill}$")
            else:
                print("Sorry thats not enough !")
                break    
            print("Thank you! ☕ Have a great day!")
            break

coffee_menu()
