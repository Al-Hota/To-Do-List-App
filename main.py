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
class Files:
    def __init__(self):
        self.selected_id = None
   
    def display_file(self):
        loop = True
        while loop:
            if not todofiles:
                choice = input("No File found, would you like to create a new file?(Y/N)")
                if choice.upper() == "Y":
                    self.first_id = "1"
                    todofiles[self.first_id] = {
                        "name": input("Input name:"),
                        "pin": input("Place a PIN(Leave blank for none): "),
                        "data": "",
                        "locked": False
                    }
                    save()
                    continue
                if choice.upper() == "N":
                    continue
            print("\n===NOTES===")
            for todofiles_id, data in todofiles.items():
                status = " [LOCKED] " if data['locked'] else ""
                print(f"{todofiles_id}. {data['name']}{status}")
            print("\nN. New File")
            print("\nQ. Quit")
            choice = input("Choose an option: ")
            if choice.upper() == "N":
                self.add_file()
            elif choice in todofiles:
                self.selected_id = choice
                self.open_file()
                        
            if choice.upper() == "Q":
                print("Goodbye!")
                loop = False
            

    def add_file(self):
        self.new_id = str(len(todofiles) + 1)
        todofiles[self.new_id] = {
            "name": input("Input name:"),
            "pin": input("Place a PIN(Leave blank for none): "),
            "data": "",
            "locked": False
        }
        save()
    def open_file(self):
        file = todofiles[self.selected_id]
        if file["locked"]:
            print("Locked")
            return
        self.retries = 3
        
        while self.retries > 0:
            password = input("Enter PIN: ")
            if password == file["pin"]:
                print(f"File: {file['data']}")
                while True:
                    print("1. Edit File")
                    print("2. Delete File")
                    print("3. Return to Menu")

                    choice = input("Choose an option: ")

                    if choice == "1":
                        self.edit_file()

                    elif choice == "2":
                        self.delete_file()
                        return

                    elif choice == "3":
                        return

            else:
                self.retries -= 1
                print(f"Incorrect PIN, you have {self.retries} left.")
            if self.retries == 0:
                file["locked"] = True
                print("Retries used up, File locked")
                return
    def edit_file(self):
            file = todofiles[self.selected_id]
            new_text = input("Type Here: ")
            file["data"] = new_text
            print(f"File: {file['data']}")
            save()
    def delete_file(self):
            del todofiles[self.selected_id]
            save()
            return

menu_instance = Files()
menu_instance.display_file()   
                






