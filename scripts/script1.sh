# Тестирование всех команд и логики VFS

# Проверка ls
ls
ls home

# Проверка cd
cd home
ls
cd user
ls
cd docs
ls report.doc

# Проверка навигации
cd ..
cd ..
cd /
ls

# Проверка uniq
uniq apple banana apple cherry banana
uniq 1 2 3 1 2 4

# Проверка tail
tail -3 A B C D E F G
tail -1 x y z

# Пример несуществующей команды и ошибок
unknown_command arg1
ls non_existent_file

# Команда exit для завершения работы скрипта
exit