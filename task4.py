from functools import wraps
from Classes.AddressBook import AddressBook
from Classes.Record import Record

def input_error(func):
    """
    Decorator for unified handling of user input errors.

    Catches common exceptions raised by command handler functions and
    returns readable messages instead of stack traces.

    Handled exceptions:
        - ValueError: wrong number or type of arguments.
        - KeyError: missing key/name in the address book.
        - IndexError: not enough arguments passed by the user.

    Parameters
    ----------
    func : Callable
        Function to wrap.

    Returns
    -------
    Callable
        Wrapped function that returns either the result of `func`
        or an error message string.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Wrong request."
        except KeyError:
            return "Wrong name."
        except IndexError:
            return "Give me name."
        except AttributeError:
            return f"Can not find your value in the book."
        except TypeError:
            return f"Error while chech dates."

    return inner

def parse_input(user_input):
    """
    Splits the user command string into command and arguments.

    Expected format: "<command> [arg1] [arg2] ...".
    Command is normalized to lowercase and stripped of extra spaces.

    Parameters
    ----------
    user_input : str
        The input string entered by the user.

    Returns
    -------
    tuple
        Tuple (command, *args), where `command` is the command name and
        `args` are additional arguments (may be empty).

    Examples
    --------
    >>> parse_input("add John 1234567890")
    ('add', 'John', '1234567890')
    >>> parse_input("all")
    ('all',)
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    """
    Adds a contact or adds a phone number to an existing contact.

    If the contact does not exist, a new Record is created and added to the
    AddressBook. If a phone is provided, it is appended to the record.

    Expected external interfaces
    ----------------------------
    AddressBook:
        - find(name) -> Record | None
        - add_record(record: Record)
    Record:
        - __init__(name: str)
        - add_phone(phone: str)

    Parameters
    ----------
    args : Sequence[str]
        Two arguments: name, phone.
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        "Contact added." or "Contact updated." depending on the result.

    Raises
    ------
    IndexError
        If not enough arguments are given.
    ValueError
        If the phone format is invalid.
    """
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book: AddressBook):
    """
    Changes the phone number for an existing contact.

    Calls `Record.edit_phone(old_phone, new_phone)` if the record is found.

    Expected external interfaces
    ----------------------------
    AddressBook:
        - find(name) -> Record | None
    Record:
        - edit_phone(old_number: str, new_number: str)

    Parameters
    ----------
    args : Sequence[str]
        Three arguments: name, old_phone, new_phone.
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        Success message or message that the contact was not found.

    Raises
    ------
    IndexError
        If not enough arguments are given.
    ValueError
        If new phone validation fails.
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact has been updated."
    

@input_error
def phone_contact(args, book: AddressBook):
    """
    Retrieves and displays all phone numbers of a contact.

    Numbers are joined with a comma separator.

    Expected external interfaces
    ----------------------------
    AddressBook:
        - find(name) -> Record | None
    Record:
        - phones: list[Phone], where Phone has a `.value` attribute (str)

    Parameters
    ----------
    args : Sequence[str]
        One argument: name.
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        "Numbers {name}: ..." or error message.

    Raises
    ------
    IndexError
        If name argument is missing.
    """
    name = args[0]
    record = book.find(name)
    callable_number = ", ".join([phone.value for phone in record.phones])
    return f"Nimbers {name}: {callable_number}."
    
    

@input_error
def all_contacts(book: AddressBook):
    """
    Returns all contacts from the address book as a formatted string.

    Delegates string representation to AddressBook.__str__.

    Parameters
    ----------
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        All contacts or "The book is empty." if there are none.
    """
    address_book = f"{book.__str__()}"
    return address_book if address_book != "" else "The book is empty."


@input_error
def add_birthday(args, book: AddressBook):
    """
    Adds a birthday date to an existing contact.

    Uses `record.add_birthday(birthday)` method.

    Expected external interfaces
    ----------------------------
    AddressBook:
        - find(name) -> Record | None
    Record:
        - add_birthday(birthday_str: str)

    Parameters
    ----------
    args : Sequence[str]
        Two arguments: name, birthday (string format).
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        Confirmation or error message from the record.
    """
    name, birthday = args
    record = book.find(name)
    record.add_birthday(birthday)
    return f"Added birthday {birthday} to {name}."

@input_error
def show_birthday(args, book: AddressBook):
    """
    Displays the birthday date of a contact.

    Expects the record to have a `birthday` field with a `.value` attribute.

    Expected external interfaces
    ----------------------------
    AddressBook:
        - find(name) -> Record | None
    Record:
        - birthday: object with `.value` attribute

    Parameters
    ----------
    args : Sequence[str]
        One argument: name.
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        "{name} birthday - {value}" or error message.
    """
    name = args[0]
    record = book.find(name)
    birthday = record.birthday.value
    return f"{name} birthday - {birthday}"

@input_error
def birthdays(book: AddressBook):
    """
    Returns a list of upcoming birthdays.

    Delegates computation to `AddressBook.get_upcoming_birthdays()`,
    which should return an iterable of dicts with 'name' and 'congratulation_date'.

    Expected external interfaces
    ----------------------------
    AddressBook:
        - get_upcoming_birthdays() -> Iterable[dict]
          each element: {'name': str, 'congratulation_date': 'YYYY-MM-DD'}

    Parameters
    ----------
    book : AddressBook
        The address book instance.

    Returns
    -------
    str
        Multi-line string like "Alice - 2025-11-17\nBob - 2025-11-18".
    """
    bd = book.get_upcoming_birthdays()
    return "\n".join([f"{d['name']} - {d['congratulation_date']}" for d in bd])


def main():
    """
    Entry point for the command-line contact assistant bot.

    Supported commands
    ------------------
    hello
        Greet the user.
    add <name> <phone>
        Add a new contact or phone number.
    change <name> <old_phone> <new_phone>
        Replace a phone number for an existing contact.
    phone <name>
        Show contact’s phone number(s).
    all
        Show all saved contacts.
    add-birthday <name> <YYYY-MM-DD>
        Add a birthday to a contact.
    show-birthday <name>
        Show the contact’s birthday.
    birthdays
        Show upcoming birthdays for congratulations.
    close | exit
        Exit the program.

    Example session
    ----------------
    Enter a command: add John 1234567890
    Contact added.
    Enter a command: phone John
    Nimbers John: 1234567890.
    Enter a command: add-birthday John 01.05.1990
    Added birthday 01.05.1990 to John.
    Enter a command: show-birthday John
    John birthday - 01.05.1990
    Enter a command: all
    <address book contents>
    Enter a command: exit
    Good bye!
    """
    
    book = AddressBook()
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
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(phone_contact(args, book))
        elif command == "all":
            print(all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()