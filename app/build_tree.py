from app.entities import TreeNode


def parse_number(stack: list[TreeNode], num: str) -> str:
    """
    Добавляет число в стек как новый узел дерева.

    :param stack: Стек, содержащий узлы дерева и открывающие скобки.
    :param num: Строка, содержащая число для преобразования в узел.
    """
    if num:
        stack.append(TreeNode(int(num)))
    return ""


def handle_brackets(stack: list[TreeNode | str], char: str) -> None:
    """
    Обрабатывает скобки, формируя узлы дерева и их иерархию.

    :param stack: Стек, содержащий узлы дерева и открывающие скобки.
    :param char: Текущий обрабатываемый символ.
    """
    if char == "(":
        stack.append(char)
    elif char == ")":
        nodes = []
        while stack and stack[-1] != "(":
            nodes.append(stack.pop())
        stack.pop()
        parent = stack.pop() if stack and isinstance(stack[-1], TreeNode) else None
        for node in reversed(nodes):
            if parent:
                parent.add_child(node)
            else:
                parent = node
        if parent:
            stack.append(parent)


def build_tree(input_string: str) -> TreeNode | None:
    """
    Строит дерево из строки c вложенными скобками.

    :param input_string: Строка, содержащая числа и скобки.
    :return: Корень построенного дерева или None, если дерево не может быть построено.
    """
    stack: list[TreeNode | str] = []
    num: str = ""
    for char in input_string:
        if char.isdigit():
            num += char
        elif char in "()":
            num = parse_number(stack, num)
            handle_brackets(stack, char)
        elif char == " " and num:
            num = parse_number(stack, num)
    parse_number(stack, num)
    return stack[0] if stack else None
