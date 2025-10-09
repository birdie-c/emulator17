import os
import socket
import sys
from cli import Shell

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    shell_string = sys.argv

    cmd_name = shell_string[0]
    vfs_name = shell_string[1]
    script_args = shell_string[2:]

    #print("Имя скрипта:", cmd_name)
    #print("Имя VFS:", vfs_name)
    #print("Переданные аргументы:", *script_args)

    shell = Shell(vfs_name)

    username = os.getlogin()
    hostname = socket.gethostname()

    current_path = shell.current_dir.get_path()

    # Если передан стартовый скрипт — выполнить его
    if len(script_args) > 0:
        for script in script_args:
            try:
                with open(script, "r") as sc:
                    for line in sc:
                        line = line.strip()
                        # Пропуск пустых строк или комментариев
                        if not line or line.startswith("#"):
                            continue
                        print(f"{username}@{hostname}:{result}$ {line}")
                        if line == "exit":
                            sys.exit(0)
                        result = shell.process_input(line)
            except FileNotFoundError:
                print(f"Ошибка: файл скрипта '{script}' не найден")

    # Основной интерактивный цикл
    while True:
        inp = input(f"{username}@{hostname}:{result}$ ")
        if inp.strip() == "exit":
            sys.exit(1)
        current_path = shell.process_input(inp)
        except EOFError: # Обработка Ctrl+D
            print("\nexit")
            sys.exit(0)
        except KeyboardInterrupt: # Обработка Ctrl+C
            print("\nПрервано пользователем")
            continue


if __name__ == "__main__":
    main()