import json
try:
    with open("data.json", "r") as f:
        todofiles = json.load(f)
except FileNotFoundError:
    todofiles = {}
except json.JSONDecodeError:
    todofiles = {}
def save():
    with open("data.json", "w") as f:
        json.dump(todofiles, f, indent=4)




def menu(todofiles_id):
    choices = todofiles[todofiles_id]
    if not todofiles:
        create = input("No File found, would you like to create a new file?(Y/N)")
        if create.upper() == "Y":
            first_id = "1"
            todofiles[first_id] = {
                "name": "untilted",
                "pin": "",
                "data": "",
                "locked": False
            }
            save()
    
        elif create.upper() == "N":
            print("Goodbye!")
            exit()
        else:
            print("Invalid Input")
            return

    if choices["locked"]:
        print("Locked.")
        return
    retries = 3
 
    while retries > 0:
        password = input("Enter your PIN: ")

        if password == choices["pin"]:
            print(f"File: {choices['data']}")
            while True:
                print("\n1. Edit File")
                print("2. Delete File")
                print("3. Return to Menu")
                try:
                    choice = int(input("Choose an option(1-2): "))
                except ValueError:
                    print("Please Enter a Number: ")
                    continue

                if choice == 1:
                    new_text = input("Type Here: ")
                    choices["data"] = new_text
                    print(f"File: {choices['data']}")
                    save()
        
                 

                if choice == 2:
                    del todofiles[todofiles_id]
                    save()
                    return


                if choice == 3:
                    return
        else:
            retries -= 1 
            print(f"Incorrect PIN, you have {retries} left.")
    if retries == 0:
        choices["Locked"] = True
        print("Retries used up, file locked.")
        return


loop = True
while loop:
    print("\n==NOTES==")

    if not todofiles:
        print("No File Found")
    else:
        for todofiles_id, data in todofiles.items():
            status = " [LOCKED] " if data['locked'] else ""
            print(f"{todofiles_id}. {data['name']}{status}")
        
    print("\nN. NEW FILE")
    print("\nQ. QUIT")

    choice = input("Choose a file or an option: ")

    if choice.upper() == "N":
        new_id = str(len(todofiles) + 1)
        todofiles[new_id] = {
            "name": input("Input Name: "),
            "pin": input("Set a Pin(Blank for none): "),
            "data": '',
            "locked": False
        }
        save()
    elif choice in todofiles:
        menu(choice)
    elif choice.upper() == "Q":
        print("Goodbye!")
        loop = False
    else:
        print("Invalid Input")




