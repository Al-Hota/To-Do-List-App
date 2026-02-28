todofiles = {
    1: {
        "File": "File1",
        "data": "text",
        "PIN": "4334",
        "Locked": False
    },

    2:  {
        "File": "File2",
        "data": "text",
        "PIN": "2313",
        "Locked": False
    },

    3: {
        "File": "File3",
        "data": "text",
        "PIN": "4234",
        "Locked": False
    }
}



def menu(todofiles_id):
    choices = todofiles[todofiles_id]

    if choices == ["Locked"]:
        print("Locked.")
        return
    retries = 3
 
    while retries > 0:
        password = input("Enter your PIN: ")

        if password == choices["PIN"]:
            print(f"File1: {choices['data']}")
            while True:
                print("1. Edit File")
                print("2. Delete File")
                print("3. Return to Menu")

                choice = int(input("Choose an option(1-2): "))

                if choice == 1:
                    new_text = input("Type Here: ")
                    choices["data"] = new_text
                    print(f"File1: {choices['data']}")

                if choice == 2:
                    pass
                    

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
    print("==NOTES==")
    for todofiles_id, data in todofiles.items():
        print(f"{todofiles_id}. {data['File']}")
    
    try:
        choice = int(input("Please choose an option(1-4): "))
    except ValueError:
        print("Invalid Input")
        continue
    if choice == 4:
        print("Goodbye!")
        loop = False
    elif choice in todofiles:
        menu(choice)
    else:
        print("Invalid Input")
       






