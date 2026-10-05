from datetime import datetime 
dt = datetime.now()

class Journal:

    def __init__(self):
 
        with open("journal.txt", "a") as file:
            print()
  
    def add_entry(self):
        try:
            new_entry = input("Enter your journal entry:-")
            with open("journal.txt", "a") as file:
                file.write( new_entry + "\n " +str(dt)+ "\n")
                print("Entry added successfully !")
        except:
            print("Error: The journal file does not exit.pelase add a ne entry first.")
            
    def view_all_entry(self):
        print("Your Journal Entries:")
        print("---------------------------------")
        try:
            with open("journal.txt", "r") as file:
                data = file.read()
                print(f"[{data}]")
        except:
            print("No journal entries found. Start by adding a new entry !")

    def seach_entry(self):
        try:
            with open("journal.txt", "r") as file:
                find = input("Enter a Keyword or data to search:- ")
                print("Matching Entries :")
                print("---------------------------------")

                for i in file:
                    if find in i:
                        print(f"{i}[{dt}]")
                        break
                else :
                    print("Not Found")
        except:
            print("No entries were found for the Keyword:", find)

    def delete_entry(self):
        try:
            num = input("Are you sure you want to delet all entries? (yes/no):- ").strip().lower()
            if num == "yes":
                with open("journal.txt", "w") as file:
                    file.write("")
                    print("All journal entries have been deleted.")
            elif num == "no":
                print("No journal entries to delete.")

            else:
                print("please Select (yes-no)")
        except:
            print("No journal entries to delete.")

 
obj = Journal()

while True:
    print()
    print("Welcome to Personal Journal Manager!")
    print()
    print("Please select an option:")
    print("1. Add a new Entry ")
    print("2. View All Entries ")
    print("3. Search for an Entry ")
    print("4. Delete All Entries ")
    print("5. Exit")

    try:
        choice = int(input("User Input :-"))
    except :
        print("Enter Only (1to5).")

    if choice == 1:
        obj.add_entry()

    elif choice == 2:
        obj.view_all_entry()

    elif choice == 3:
        obj.seach_entry() 

    elif choice == 4:
        obj.delete_entry() 

    elif choice == 5:
        print("Thank you for using personal Journal Manager. GoodBye!")
        break      

    else:
        print("Invalid option. please select a valid option from the menu.")