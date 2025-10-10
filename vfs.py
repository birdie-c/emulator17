class VFSNode:
    def __init__(self, name, content, node_type="dir",):
        self.name = name
        self.type = node_type  # "dir" или "file"
        self.children = {} #словарь для дочерних элементов (ключ — имя дочернего узла)
        self.parent = None
        self.content = content

    def add_child(self, node):
        if self.type != "dir":
            raise ValueError("Нельзя добавить дочерний элемент к файлу")
        node.parent = self
        self.children[node.name] = node

    def get_path(self):
        node = self
        parts = []
        while node and node.name != "":
            parts.append(node.name)
            node = node.parent
        return "/" + "/".join(reversed(parts))

    def get_content(self):
        if self.type != "file":
            raise ValueError(f"Узел '{self.name}' не является файлом")
        return self.content