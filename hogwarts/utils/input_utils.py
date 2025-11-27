def ask_text(message):
    try :
        return str(input(message))
    except ValueError :
        print("Invalid input. Please enter text.")
        return str(ask_text(message))

def ask_number(message):
    try :
        return int(input(message))
    except ValueError :
        print("Invalid input. Please enter a number.")
        return ask_number(message)

def ask_choice(message, options):
    print(message)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = ask_number("Enter the number of your choice: ")
    if 1 <= choice <= len(options):
        return options[choice - 1]
    else:
        print("Invalid choice. Please try again.")
        return ask_choice(message, options)