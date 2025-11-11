from functools import wraps

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Wrong name"
        except IndexError:
            return "Give me name"

    return inner

def parse_input(user_input):
    """
    Parse user input string into command and arguments.

    Args:
        user_input (str): Input string entered by the user. 
                          The first word is treated as a command, 
                          and the rest as arguments separated by spaces.

    Returns:
        tuple: A tuple containing:
            - cmd (str): The parsed command in lowercase.
            - *args (list[str]): The remaining parts of the input as arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contact list.

    Args:
        args (tuple[str, str]): A tuple containing two elements:
            - name (str): The contact name.
            - phone (str): The contact phone number.
        contacts (dict): A dictionary storing contact names as keys 
                         and phone numbers as values.

    Returns:
        str: Confirmation message "Contact added." after the contact 
             is successfully added.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Change the phone number of an existing contact.

    Args:
        args (tuple[str, str]): A tuple containing two elements:
            - name (str): The name of the contact to be updated.
            - phone (str): The new phone number for the contact.
        contacts (dict): A dictionary storing contact names as keys 
                         and phone numbers as values.

    Returns:
        str: Confirmation message "Contact changed." after the contact 
             is successfully updated.

    """
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@input_error
def phone_contact(args, contacts):
    """
    Retrieve and display the phone number of a specified contact.

    Args:
        args (list[str]): A list where the first element is:
            - name (str): The name of the contact whose phone number is requested.
        contacts (dict): A dictionary storing contact names as keys 
                         and phone numbers as values.

    Returns:
        str: A formatted string "Calling {name} {phone}." 
             showing the contact name and phone number.
             If the contact is not found, phone will be displayed as "None".
    """
    name = args[0]
    phone = contacts.get(name)
    return f"Calling {name} {phone}."

@input_error
def all_contacts(contacts):
    """
    Return a string representation of all contacts.

    Args:
        contacts (dict): A dictionary storing contact names as keys 
                         and phone numbers as values.

    Returns:
        str: String representation of the entire contacts dictionary.
    """
    return f"{contacts}"

def main():
    """
    Main function that runs the assistant bot for managing contacts.

    The bot supports basic text commands entered by the user to manage 
    a contact list stored in a dictionary. Supported commands:
        - 'hello'  : Greets the user.
        - 'add'    : Adds a new contact. Usage: add <name> <phone>
        - 'change' : Changes an existing contact’s phone number. Usage: change <name> <new_phone>
        - 'phone'  : Displays a contact’s phone number. Usage: phone <name>
        - 'all'    : Displays all contacts.
        - 'close' or 'exit' : Ends the program.
    """
    
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except:
            print("Please send your command")
            continue          

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
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()