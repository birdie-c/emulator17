import os
import socket
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--vfs', '-v', help = 'Путь к файлу VFS')
parser.add_argument('--script', '-s', help = 'Путь к стартовому файлу')
args = parser.parse_args()
print(args.vfs)

def processInput(inp): # обработка команд
    parts = inp.strip().split()

    if not parts:
        return

    command = parts[0]
    args = parts[1:]
    
    if command == "ls": # list - содержимое текущей директории
        if len(args) > 1:
            return "ERROR\nСлишком много аргументов для 'ls'"
        elif len(args) == 1:
            return f"ls {args[0]}" 
        else:
            return 'ls'

    elif command == "cd": # cd - change directory
        if len(args) > 1:
            return "ERROR\nСлишком много аргументов для 'cd'"
        elif len(args) == 1:
            return f"cd {args[0]}"
        else:
            return 'cd'
    else:
        print(f"ERROR\nНеизвестная команда: {command}")

username = os.getlogin()
hostname = socket.gethostname()

if args.script:
    try:
        with open(args.script, 'r') as script_file:

            commandExit = False;
            for line in script_file:
                line = line.strip()
                if not line or line.startswith('#'): # пропускаем пустые строки и комментарии
                    continue

                print(f"{username}@{hostname}:~$ {line}")
                
                if line.split()[0] == "exit":
                    sys.exit()
                
                result = processInput(line) # обрабатываем все остальные команды
                if result:
                    print(result)
    except FileNotFoundError:
        print(f"Ошибка: скрипт '{args.script}' не найден")


while True:
    inp = input(f"{username}@{hostname}:~$ ")
        
    if inp.strip() == "exit":
        break
    result = processInput(inp)
    if result:
        print(result)
