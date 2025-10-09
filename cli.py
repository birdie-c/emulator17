import sys
from vfs_loader import load_vfs

class Shell:
    def __init__(self, vfs_path=None):
        self.vfs_root = None
        self.current_dir = None

        if vfs_path:
            try:
                self.vfs_root = load_vfs(vfs_path)
                self.current_dir = self.vfs_root
                print(f"VFS успешно загружена из {vfs_path}")
            except (FileNotFoundError, ValueError) as e:
                # Ошибка загрузки VFS (Этап 3, требование 3)
                print(f"ERROR\n{e}")
                sys.exit(1)

    def process_input(self, inp):
        parts = inp.strip().split()

        if not parts:
            # Если ввод пустой, просто возвращаем текущий путь
            return self.current_dir.get_path()
        command, *args = parts

        # Проверка, что VFS загружена перед выполнением большинства команд
        if command not in ["exit", "clear"] and not self.current_dir:
            print("ERROR\nVFS не загружена")
            return "/"

        if command == "ls":
            return self.cmd_ls(args)
        elif command == "cd":
            return self.cmd_cd(args)
        elif command == "clear":
            return self.cmd_clear()
        elif command == "uniq":
            return self.cmd_uniq(args)
        elif command == "tail":
            return self.cmd_tail(args)
        elif command == "exit":
            sys.exit(0)
        else:
            # Обработка ошибки неизвестной команды (Этап 1, требование 8)
            print(f"ERROR\nНеизвестная команда: {command}")
            return self.current_dir.get_path()

    def cmd_ls(self, args):
        if len(args) > 1:
            print("ERROR\nСлишком много аргументов для 'ls'")
            return self.current_dir.get_path()

        node = self.current_dir

        if args:
            name = args[0]
            if name in node.children:
                node = node.children[name]
            else:
                print(f"ERROR\nПуть '{name}' не найден")
                return self.current_dir.get_path()
        if node.type == "file":
            # Если это файл, выводим только его имя
            return node.name

        print(*sorted(node.children.keys()))
        return self.current_dir.get_path()

    def cmd_cd(self, args):
        if len(args) > 1:
            print("ERROR\nСлишком много аргументов для 'cd'")
            return self.current_dir.get_path()

        # Без аргументов или "cd /" → перейти в корень
        if not args or args[0] == "/":
            self.current_dir = self.vfs_root
            return self.current_dir.get_path()  # всегда "/"

        name = args[0]

        # "cd .." → переход к родителю
        if name == "..":
            if self.current_dir.parent:
                self.current_dir = self.current_dir.parent
            return self.current_dir.get_path()

        # Проверка существования подкаталога
        if name not in self.current_dir.children:
            print(f"ERROR\nПуть '{name}' не найден")
            return self.current_dir.get_path()

        node = self.current_dir.children[name]

        if node.type != "dir":
            print(f"ERROR\n'{name}' не является директорией")
            return self.current_dir.get_path()

        self.current_dir = node
        return self.current_dir.get_path()

    def cmd_clear(self):
        print("\n" * 50)
        return self.current_dir.get_path()

    def cmd_uniq(self, args):
        print(*sorted(list(set(args))))
        return self.current_dir.get_path()

    def cmd_tail(self, args):
        try:
            num = - int(args.pop(0))
            print(*args[num:])
            return self.current_dir.get_path()
        except:
            print("incorrect args")
            return self.current_dir.get_path()