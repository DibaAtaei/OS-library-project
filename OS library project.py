import os
from colorama import Fore ,init
init()

DEMO_PATH =os.path.join(os.path.dirname(__file__),"demo")

user={
    "diba":{
        "password":"1234",
        "email":"diba123@gmail.com",
    "access":"premium"
    },
    "sara":{
        "password":"4567",
        "email":"sara4@gmail.com",
        "access":"free"
    },
    "taha":{
        "password":"1122",
    "email":"tahaa@gmail.com",
    "access":"premium"
    },
    "ali":{
        "password":"2222",
    "email":"ali2@gmail.com",
        "access":"free"
    },
    "admin":{
        "password":"admin123",
    "access":"admin",
        "email":"adminpro@gmail.com"
    }
}

def can_access_tree(access):
    return access == "premium" or access == "admin"

def is_admin(access):
    return access == "admin"

def create_new_folder():
  folder_name=input("enter the new folder name:")
  new_path=os.path.join(DEMO_PATH,folder_name)
  if os.path.isdir(new_path):
      print("folder already exists")
  else:
      os.mkdir(new_path)
      print("folder created successfully " ,new_path)

def check_file_exists():
    folder_name=input("enter the folder name:")
    file_name=input("enter the file name:")
    folder_path=os.path.join(DEMO_PATH,folder_name)
    file_path=os.path.join(folder_path , file_name)

    if not os.path.isdir(folder_path):
        print("folder does not exist")
    elif os.path.isfile(file_path):
        print("file found:", file_path)
    else:
        print("this file is not in the folder")

def list_files_in_folder():
    folder_name=input("enter the folder name that you want to see the files of:")
    folder_path=os.path.join(DEMO_PATH,folder_name)
    if not os.path.isdir(folder_path):
        print("folder does not exist")
        return

    files = os.listdir(folder_path)
    files.sort()
    print("files inside", folder_name ,":")
    for f in files:
        print("-" , f)

def show_tree(path , prefix=""):
    items=sorted(os.listdir(path))
    count=len(items)
    for index , item in enumerate(items):
        items_path=os.path.join(path , item)
        is_last = (index == count - 1)
        if is_last:
            connector = "└── "
        else:
            connector = "├── "
            print(prefix + item + connector)
            if os.path.isdir(items_path):
                if is_last:
                    next_prefix = prefix + "    "
                else:
                    next_prefix = prefix + "│   "
                show_tree(items_path, next_prefix)

def register_new_user():
    print("register new user")
    new_username = input("enter new username: ")

    if new_username in user:
        print("username already exists")
        return


    new_password=input("enter new password: ")
    new_email=input("enter new email: ")
    new_access=input("enter new access:(premium / free) : ")

    if new_access not in ("free", "premium"):
        print("Access level must be 'free' or 'premium'.")
        return
    user[new_username] = {"password": new_password, "access": new_access, "email": new_email}
    print("User registered successfully:", new_username)

def show_menu(access):
    print("\n------ MENU ------")
    print("1. Create new folder")
    print("2. Check if a file exists")
    print("3. List files in a folder (sorted)")
    if can_access_tree(access):
        print("4. Show full folder tree")
    if is_admin(access):
        print("5. Register new user")
    print("0. Exit")


def main():
    username = input("username: ")
    password = input("password: ")
    if username not in user:
        print("username does not exist!")
        return
    if user[username]["password"] != password:
        print("wrong password!")
        return
    access = user[username]["access"]
    
    access = user[username]["access"]

    print(Fore.GREEN + "wellcome"+ username)


    if is_admin(access):
        print(Fore.MAGENTA + "Access level: Admin")
    elif can_access_tree(access):
        print(Fore.BLUE + "Access level: Premium")
        print("You have access to all movies.")
    else:
        print(Fore.RED + "Access level: Free")
        print("Buy a subscription to unlock more movies.")

    while True:
        show_menu(access)
        choice = input("Pick an option: ")

        if choice == "1":
            create_new_folder()
        elif choice == "2":
            check_file_exists()
        elif choice == "3":
            list_files_in_folder()
        elif choice == "4" and can_access_tree(access):
            print("Demo folder structure:")
            show_tree(DEMO_PATH)
        elif choice == "4" and not can_access_tree(access):
            print("You have Free access and cannot use the tree feature.")
        elif choice == "5" and is_admin(access):
            register_new_user()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
if __name__ == "__main__":
        main()




























