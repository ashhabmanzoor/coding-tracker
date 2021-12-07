import main


def print_msg():
    # main.instantiate_db()
    print("""Hello, Have you coded today?
Please choose an option:
    1.ADD an entry
    2.UPDATE an entry
    3.DELETE an entry
    4.VIEW specific entry   
    5.VIEW ALL entries
    6.QUIT
    """)


def user_choice():
    user_input = input("Please input choice: ")
    if user_input == "1":
        day = input("Please provide day: ")
        date = input("Please provide date: ")
        time = input("Please provide time: ")
        main.add_entry(day, date, time)
        print_msg()
        user_choice()
    elif user_input == "2":
        print("Updating")
        date = input("Please provide date: ")
        time = input("Please provide updated time: ")
        main.update_entry(date, time)
        print("Coding Time has been updated")
        print_msg()
        user_choice()
    elif user_input == "3":
        print("Deleting...")
        date = input("Please provide date: ")
        main.delete_entry(date)
        print("Date has been deleted")
        print_msg()
        user_choice()
    elif user_input == "4":
        date = input("PLease provide specific date: ")
        main.view_entry(date)
        print_msg()
        user_choice()
    elif user_input == "5":
        main.view_all_entry()
        print("""What would you like to do?
PLease choose an option:
    1. Return to Main Menu
    2. Quit Application
        """)
        choice = input()
        if choice == "1":
            print_msg()
            user_choice()
        elif choice != "1":
            quit
    elif user_input == "6":
        quit
    else:
        print("Please Try Again!")
        user_choice()


print_msg()
user_choice()
