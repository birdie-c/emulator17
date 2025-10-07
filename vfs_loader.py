import os
import xml.etree.ElementTree as ET
from vfs import VFSNode

def load_vfs(xml_path):
    if not os.path.exists(xml_path):
        raise FileNotFoundError(f"Файл VFS '{xml_path}' не найден")

    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as e:
        raise ValueError(f"Ошибка при парсинге XML: {e}")

    root_el = tree.getroot()
    if root_el.tag.lower() != "vfs":
        raise ValueError("Корневой элемент XML должен быть <vfs>")

    root_node = VFSNode(name = "")
    for el in root_el:
        parse_element(el, root_node)

    return root_node

def parse_element(el, parent_node):
    if el.tag == "dir":
        name = el.get("name", "")
        node = VFSNode(name, "dir")
        parent_node.add_child(node)
        for child in el:
            parse_element(child, node)
    elif el.tag == "file":
        name = el.get("name", "")
        node = VFSNode(name, "file")
        parent_node.add_child(node)
    else:
        raise ValueError(f"Неизвестный элемент: {el.tag}")