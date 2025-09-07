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
        print("file1.txt  file2.txt")

    elif command == "cd": #cd - change directory
        if len(args) > 1:
            print("ERROR\nСлишком много аргументов для 'cd'")
        elif len(args) == 1:
            print(f"Переход в дриекторию {args[0]}")  
        else:
            print('Домашнаяя директория')
    else:
        print(f"ERROR\nНеизвестная команда: {command}")
            
