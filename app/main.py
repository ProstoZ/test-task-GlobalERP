from app.build_tree import build_tree

test_task_string = "(1 (2 (4 5 6 (7) 108 (9)) 3))"
root = build_tree(test_task_string)
root.display_tree()
