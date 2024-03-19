def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Передано неверное кол-во аргументов"
    if name in contacts:
        return "Контакт уже существует"
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Передано неверное кол-во аргументов"
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "К сожалению контакт с таким именем не найдет"

def show_phone(args, contacts):
    try:
        name, = args
    except ValueError:
        return "Передано неверное кол-во аргументов"
    if name in contacts:
        return contacts[name]
    else:
        return "К сожалению контакт с таким именем не найдет"

def show_all(contact, contacts):
    return f"Имя: {contact} номер телефона {contacts[contact]}\n"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(*[show_all(contact, contacts) for contact in contacts])
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

