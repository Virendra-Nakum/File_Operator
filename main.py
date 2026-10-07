from datetime import datetime
dt= datetime.now()

class Journal:
    def __init__(self):
        try:
            with open("journal.txt","x") as file:
                print(file)
        except:
                print("Please Delete file'journal.txt' first\n")
        
    def add_entry(self):
        try:
            with open("journal.txt","a") as file:
                add=input("Enter your journal entry :")
                file=file.write(f" [{dt}] \n {add}\n")
                print("Entry added sucessfully!")
        except:
            print("There is An Error in Add function!!")

    def view_all_entries(self):
        try:
            with open("journal.txt","r") as file:
                read=file.read()
            
            print("Your Journal Entries:")
            print("-------------------------------")
            print(read)

        except:
            print(" Error:No journal entries found. Start by  adding a new entry!")

    def search_entry(self):
        try:
            with open("journal.txt","r") as file :
                
                entry=input("Enter a  keyword or date to search :- ")
                a=file.readlines()
            for x in a:
                if entry.lower() in x.lower():
                    print(f"[{dt}] \n {x}")
                    break

            else:
                print(f"No entries were found for the keyword : {entry}. ")

        except:
            print("Something Went Wrong in Search Function !!")

    def delete_entries(self):
        try:
            choice =input("Are you sure you want to delete all entries? (yes/no):")
            
            if choice == "yes":
                with open("journal.txt", "w") as file:
                    file.write("")

                print("All journal entries have been deleted.")
           
            elif choice == "no":
                print("Data is not deleted")

        except :
            print("No Journal Entries to Delete.")

obj= Journal()

print("Welcome to Personal Journal Manager Project !")

while True:
    print("\nPlease Select an Option :")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search For an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice=int(input("User Input :-"))

    if choice==1:
        obj.add_entry()

    elif choice==2:
        obj.view_all_entries()

    elif choice==3:
        obj.search_entry()

    elif choice==4:
        obj.delete_entries()

    elif choice==5:
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break
    
    else:
        print("Invalid option Please a  valid option from the menu")
         
         
         

                


        
