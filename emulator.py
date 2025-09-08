import os
import socket

username = os.getlogin()

hostname = socket.gethostname()

while True:
    inp = input(f"{username}@{hostname}:~$ ")
    parts = inp.strip().split()

    if not parts:
        continue

    command = parts[0]
    args = parts[1:]

    if command == "exit":
        break

    elif command == "ls": #list - содержимое текущей директории
        if len(args) > 1:
            print("ERROR\nСлишком много аргументов для 'ls'")
        elif len(args) == 1:
            print(f"ls {args[0]}")  
        else:
            print('ls')

    elif command == "cd": #cd - change directory
        if len(args) > 1:
            print("ERROR\nСлишком много аргументов для 'cd'")
        elif len(args) == 1:
            print(f"cd {args[0]}")  
        else:
            print('cd')
    else:
        print(f"ERROR\nНеизвестная команда: {command}")
            
