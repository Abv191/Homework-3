def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter a valid name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter a name."
    return inner


def parse_command(command):
    try:
        _, name, phone = command.split(' ')
        return name, phone
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid name and phone number separated by a space.")
    except IndexError:
        raise IndexError("Invalid input. Please enter a name.")


@input_error
def add_contact(command):
    name, phone = parse_command(command)
    contacts[name] = phone
    return "Contact added."


@input_error
def change_phone(command):
    name, phone = parse_command(command)
    contacts[name] = phone
    return "Phone number updated."


@input_error
def get_phone(command):
    name, _ = parse_command(command)
    return contacts[name]


def show_all():
    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    else:
        return "No contacts."


def main():
    print("How can I help you?")
    while True:
        command = input("> ").lower()

        if command == "hello":
            print("How can I help you?")

        elif command.startswith("add"):
            response = add_contact(command)
            print(response)

        elif command.startswith("change"):
            response = change_phone(command)
            print(response)

        elif command.startswith("phone"):
            response = get_phone(command)
            print(response)

        elif command == "show all":
            response = show_all()
            print(response)

        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    contacts = {}
    main()
