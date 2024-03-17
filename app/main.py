class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display_tree(self, level=0, prefix='', is_root=True):
        indent = ' ' * (level * 4) if level > 0 else ''
        if level > 0 and not is_root:
            indent = prefix[:-4] + '    '
        print(f"{indent}{self.value}", end='')
        if self.children:
            print('---+')
            new_prefix = prefix + ('    ' if level == 0 else '|    ')
            for i, child in enumerate(self.children):
                child.display_tree(level + 1, new_prefix, False)
        else:
            print('')


def build_tree(s):
    stack = []
    num = ''
    for char in s:
        if char.isdigit():
            num += char
        elif char == ' ' and num:
            stack.append(TreeNode(int(num)))
            num = ''
        elif char == '(':
            if num:
                stack.append(TreeNode(int(num)))
                num = ''
            stack.append('(')
        elif char == ')':
            if num:
                stack.append(TreeNode(int(num)))
                num = ''
            nodes = []
            while stack and stack[-1] != '(':
                nodes.append(stack.pop())
            stack.pop()
            if stack:
                parent = stack.pop()
                for node in nodes[::-1]:
                    if isinstance(node, TreeNode):
                        parent.add_child(node)
                stack.append(parent)
            else:
                stack.extend(nodes[::-1])
        elif char == ' ':
            continue
        else:
            raise ValueError("Некорректный символ в строке")
    return stack[0]


s = "(1 (2 (4 5 6 (7) 108 (9)) 3 ))"
root = build_tree(s)
root.display_tree()
