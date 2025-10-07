import argparse
import os
import socket
import sys
from cli import Shell

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vfs", "-v", help="Путь к файлу VFS")
    parser.add_argument("--script", "-s", help="Путь к стартовому скрипту")
    args = parser.parse_args()

    shell = Shell(args.vfs)

    username = os.getlogin()
    hostname = socket.gethostname()

    # Если передан стартовый скрипт — выполнить его
    result = '~'
    if args.script:
        try:
            with open(args.script, "r") as script:
                for line in script:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    print(f"{username}@{hostname}:{result}$ {line}")
                    if line == "exit":
                        sys.exit(0)
                    result = shell.process_input(line)
        except FileNotFoundError:
            print(f"Ошибка: файл скрипта '{args.script}' не найден")

    # Основной интерактивный цикл
    while True:
        inp = input(f"{username}@{hostname}:{result}$ ")
        if inp.strip() == "exit":
            break
        result = shell.process_input(inp)


if __name__ == "__main__":
    main()