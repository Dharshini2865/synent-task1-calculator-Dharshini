# Task 1: Simple Calculator
# Synent Technologies Python Internship
# This calculator uses colorama for coloured terminal output

from colorama import init, Fore, Style
init(autoreset=True)  # Resets colour after each print


def show_banner():
    """Prints a nice header when the program starts"""
    print(Fore.CYAN + "=" * 45)
    print(Fore.CYAN + "     SIMPLE CALCULATOR - Synent Internship")
    print(Fore.CYAN + "=" * 45)
    print(Style.RESET_ALL)


def get_number(prompt):
    """Asks the user for a number, handles invalid input"""
    while True:
        try:
            return float(input(Fore.YELLOW + prompt))
        except ValueError:
            print(Fore.RED + "  Invalid input! Please enter a number.")


def show_menu():
    """Shows the operation menu"""
    print(Fore.WHITE + "\nSelect an operation:")
    print(Fore.GREEN  + "  1. Addition       (+)")
    print(Fore.GREEN  + "  2. Subtraction    (-)")
    print(Fore.GREEN  + "  3. Multiplication (*)")
    print(Fore.GREEN  + "  4. Division       (/)")
    print(Fore.RED    + "  5. Exit")
    print()


def calculate(num1, num2, choice):
    """Performs the calculation and returns the result"""
    if choice == "1":
        return num1 + num2, "+"
    elif choice == "2":
        return num1 - num2, "-"
    elif choice == "3":
        return num1 * num2, "*"
    elif choice == "4":
        if num2 == 0:
            return None, "/"  # Cannot divide by zero
        return num1 / num2, "/"


def main():
    """Main program loop"""
    show_banner()

    while True:
        show_menu()

        # Get the user's operation choice
        choice = input(Fore.YELLOW + "Enter choice (1-5): ").strip()

        if choice == "5":
            print(Fore.CYAN + "\nThank you for using the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print(Fore.RED + "Invalid choice! Please enter 1-5.")
            continue

        # Get the two numbers from the user
        num1 = get_number("Enter first number:  ")
        num2 = get_number("Enter second number: ")

        # Perform the calculation
        result, operator = calculate(num1, num2, choice)

        # Show the result
        if result is None:
            print(Fore.RED + "\n  Error: Cannot divide by zero!")
        else:
            # Format nicely: remove .0 from whole numbers
            n1 = int(num1) if num1 == int(num1) else round(num1, 4)
            n2 = int(num2) if num2 == int(num2) else round(num2, 4)
            r  = int(result) if result == int(result) else round(result, 4)

            print(Fore.GREEN + f"\n  {n1} {operator} {n2} = ", end="")
            print(Fore.WHITE + Style.BRIGHT + f"{r}")

        print(Fore.CYAN + "-" * 45)


# This is the entry point — Python runs main() when you run the file
if __name__ == "__main__":
    main()