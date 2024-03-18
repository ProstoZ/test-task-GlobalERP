# TEST-TASK-GlobalERP

>       Before running, make sure you have Python 3.12 installed on the computer where you are going to run this
>
>       Next, to launch and build a tree in the console according to the specifications, you need to run the `main.py` file

### Example

    for string = `(1 (2 (4 5 6 (7) 108 (9)) 3))`

    The program will display the following result in the console:

        1-------+
                2-------+
                |       4
                |       5
                |       6-------+
                |       |       7
                |       108-----+
                |               9
                3

### Ruff

    To check the project code with the ruff linter, enter the following command in 
    the console (being in the project root):
    
        - ruff check .