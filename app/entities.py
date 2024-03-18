from app.constants import INDENT_LENGTH


class TreeNode:
    """
    Класс, представляющий узел в структуре дерева.

    Attributes:
        - value (значение): Значение, хранящееся в узле.
        - children (дети): Список объектов TreeNode, которые являются детьми этого узла.

    Methods:
        - add_child(self, child_node): Добавляет объект TreeNode в список детей.
        - display_tree(self, level=0, prefix='', is_root=True): Рекурсивно выводит структуру дерева,
            начиная с узла, на котором вызван этот метод. Дерево отображается с отступами,
            представляющими глубину каждого узла, и визуальным представлением отношений родитель-ребенок.
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.children: list[TreeNode] = []

    def add_child(self, child_node: "TreeNode") -> None:
        self.children.append(child_node)

    def display_tree(self, level: int = 0, last: bool = True, prefix: str = "") -> None:
        indent = ""
        connector = "-" * (INDENT_LENGTH - len(str(self.value))) + "+" if self.children else ""
        if level == 0:
            print(f"{self.value}{connector}")
        else:
            print(f"{prefix}{indent}{self.value}{connector}")

        if self.children:
            new_prefix = prefix + (" " * INDENT_LENGTH if last else "|" + " " * (INDENT_LENGTH - 1))
            for i, child in enumerate(self.children):
                is_last = i == len(self.children) - 1
                child.display_tree(level + 1, is_last, new_prefix)
