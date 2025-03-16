import os; from datetime import datetime as dt
executable_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(executable_dir)
current_date = dt.now()


def custom_time():
    form = int(input(f"""Format?:
        1. Current format (%B %d %Y  e.g:{current_date.strftime("%B %d %Y")})
        2. Custom format\n"""))
    if form == 1:
        time = input("Enter custom time: ")
        form  = "%B %d %Y"
    elif form == 2:
        form = input("Enter custom format: ")
        time = input("Enter custom time: ")
    else: 
        print("Wrong or invalid format type")
        custom_time()

    return dt.strptime(time,form)

def path_resolver(date):
    "Return new folder path with current date in its name"
    new_folder_name = date.strftime("%B_%d_%Y")
    new_folder_path = os.path.join(executable_dir,new_folder_name)
    return new_folder_path

def create_new_folder(path):
    try:
        os.mkdir(path)
        print(f"Directory created: {path}")
    except FileExistsError:
        print(f"Directory already exist: {path}")
    except PermissionError:
        print(f"Permission denied while creating the directory {path}.")
    except FileNotFoundError:
        print(f"Folder not found: {path}.\nEXITTING!")
        exit()
        

def symlink_boiii(path,date):
    subfolder_name = date.strftime("%B_%d_%Y")
    for folder_name in ["Homework","Classwork"]:
        src_path = os.path.join(executable_dir, os.pardir, folder_name, subfolder_name)
        destination_path = os.path.join(path,folder_name)
        
        try:
            create_new_folder(src_path)
        except FileExistsError:
            pass
        
        try:
            os.symlink(src_path,destination_path)
        except FileExistsError:
            print(f"Symlink already exist: {destination_path}")
        except PermissionError:
            print(f"Permission denied while creating the fsymlink {destination_path}.")


def main():
    mode = int(input(f"""Hello, {os.getlogin()}
    We 're currently in {executable_dir}
    What do you want to do?
    1. Create a new folder with current datetime ({current_date})
    2. Create a new folder with custom datetime (MMMM dd yyyy)
    3. Exit\n"""))
    if mode == 3:
        print("Exiting")
        exit()
    elif mode == 2:
        path = path_resolver(custom_time())
        create_new_folder(path)
    elif mode == 1:
        path = path_resolver(current_date)
        create_new_folder(path)
        symlink_boiii(path,current_date)
    else:
        print("Invalid, try again.")

if __name__ == "__main__":
    main()