import shutil
import os
import socket
import datetime

delete_directory = "desired/directory"
delete_date = datetime.datetime(2024, 3 ,18, 14, 22)

def purge_directory(directory):
    files_to_delete = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            last_modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if last_modified_date > delete_date:
                files_to_delete.append(file_path)
    
    if files_to_delete:
        print(f"The following files were last modified before {delete_date} and are pending permanent deletion: ")
        for file_path in files_to_delete:
            print(file_path)
        confirmation = input("Do you wish to delete these files? (Y/N) ").strip().upper()
        if confirmation == 'Y':
            for file_path in files_to_delete:
                os.remove(file_path)
                print(f"{file_path} deleted")
        elif confirmation == 'N':
            print("Deletion cancelled.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"No files found that were modified before {delete_date}")

def disk_space():
    total, used, free = shutil.disk_usage("/")
    total = f"{total / (1024 ** 3):.2f}"
    used = f"{used / (1024 ** 3):.2f}"
    free = f"{free / (1024 ** 3):.2f}"
    print(f"Total system storage: {total}GB, Storage used: {used}GB, Free storage: {free}GB")

def verify_name():
    hostname = socket.gethostname()
    print(f"System Name: {hostname}")

def verify_datetime():
    dateandtime = datetime.datetime.now()
    print(f"System date and time: {dateandtime}")

def verify_app():
    program = shutil.which("teams")
    if program == None:
        print("Program not found")
    else:
        print(f"Teams installed at: {program}")

disk_space()
verify_name()
verify_datetime()
verify_app()
purge_directory(delete_directory)
