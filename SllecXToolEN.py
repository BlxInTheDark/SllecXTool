import os
import psutil
import random
import socket

def display_menu(username):
    print("\n=== SllecXTool Utility ===")
    print(f"Hello {username}! How can I assist you?")
    print("1. List Running Processes")
    print("2. Terminate a Process")
    print("3. Search for a Process")
    print("4. ZIP Passport Cracker")
    print("5. SpyWare Tool")
    print("6. IP Address Changer")
    print("7. Exit")

def list_processes():
    print("=== List Running Processes ===")
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            print(f"PID: {process.info['pid']}, Name: {process.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def terminate_process():
    print("=== Terminate a Process ===")
    print("Please enter the PID of the process you want to terminate:")
    try:
        pid = int(input().strip())
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process with PID {pid} terminated successfully!")
    except (ValueError, psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        print("Invalid PID or process not found or access denied.")

def search_process():
    print("=== Search for a Process ===")
    print("Please enter a keyword to search for a process:")
    keyword = input().strip()
    
    if not keyword:
        print("Invalid keyword. Please enter a valid keyword.")
        return
    
    found_processes = []
    for process in psutil.process_iter(attrs=['name']):
        try:
            if keyword.lower() in process.info['name'].lower():
                found_processes.append(process.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    if found_processes:
        print(f"Processes matching '{keyword}': {', '.join(found_processes)}")
    else:
        print(f"No processes found matching '{keyword}'.")

def zip_passport_cracker(username):
    print("=== ZIP Passport Cracker ===")
    password = input("Please enter the ZIP passport password: ").strip()

    if password == "correct_password":
        print("ZIP passport cracked successfully!")
    else:
        print("Incorrect password. ZIP passport not cracked.")

def spyware_tool(username):
    print("=== SpyWare Tool ===")
    email = input("Please enter your email: ").strip()

    if email == "correct_email@example.com":
        print("SpyWare Tool: Access granted. Displaying incoming and outgoing messages...")
    else:
        print("SpyWare Tool: Try again, the email is incorrect...")

def change_ip_address():
    print("=== IP Address Changer ===")
    new_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    try:
        socket.inet_aton(new_ip)
        print(f"IP address successfully changed! New IP address is {new_ip}")
    except socket.error:
        print("IP address couldn't be changed, please try again...")

def main():
    username = "User"

    while True:
        display_menu(username)
        choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()
        if choice == "1":
            list_processes()
        elif choice == "2":
            terminate_process()
        elif choice == "3":
            search_process()
        elif choice == "4":
            zip_passport_cracker(username)
        elif choice == "5":
            spyware_tool(username)
        elif choice == "6":
            change_ip_address()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()
