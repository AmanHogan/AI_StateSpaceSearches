# Aman Hogan-Bailey

## MavId: 1001830469
## Date: 2/25/2023

## Programming Language: 3.11.2 64 Python
## Environment: VsCode and Microsoft CMD command line prompt

## Structure

The driver code is specified in `expense_8_puzzle.py`. This Python file is responsible for calling the BFS, DFS, UCS, Greedy, A*, DLS, and DLS search algorithms. Each search algorithm's implementation code is separated into their own respective Python modules: 

- `a_star.py`
- `breadth.py`
- `depth.py`
- `greedy.py`
- `iterative_deep.py`
- `uniform.py`
- `depth_limited.py`
- `depth.py`

Additionally, there are original helper modules: 

- `eight.py` - responsible for the puzzle logic
- `nodes.py` - responsible for keeping track of all information regarding each created node
- `file2puzzle.py` - responsible for reading the `start.txt` and `goal.txt` files and converting them into puzzles

Additional files:

- `goal.txt` - the example goal file provided by the instructor
- `start.txt` - the example start file provided by the instructor
- `dfs.txt` - a file that will be created by `depth.py` due to stdin overflow
- `trace_<date>-<time>.txt` - a file that logs all dump information for the algorithms

## Program Logic

1. `expense_8_puzzle` calls `file2puzzle` to translate the puzzle into a state.
2. `expense_8_puzzle` then calls an algorithm implementation and sends in the start and goal states, along with command-line arguments.
3. The algorithm calls `nodes.py` and `eight.py` to handle the puzzle and node logic.
4. The algorithm returns the goal state to `expense_8_puzzle`.
5. `expense_8_puzzle` then calls `nodes.py` to print out the series of actions that led to the goal state.

## How to Run

There are two ways to run this program:

### Windows CMD:

1. Unzip the downloaded file.
2. Open your Windows terminal.
3. Make sure you have Python version 3 or higher installed.
4. Locate the directory where the source code is located (where `expense_8_puzzle.py` is located): `cd C:\Users\ .... \expense_8_puzzle`
5. Then, from the command line, run: `python expense_8_puzzle.py <start file> <goal file> <method>`
6. The code should then output the results.

### Vscode:

1. Unzip the downloaded file.
2. Open the folder in Vscode and select "Trust this folder."
3. Set up your Vscode to have a Python environment:
   - Hold down SHIFT+CTRL+P and select "Python: Select Interpreter."
   - Choose the path where Python is installed on your system.
4. Find the `expense_8_puzzle.py` file, right-click, and select "Run Python File in Terminal."
   - This will open a terminal in Vscode using a Python interpreter.
5. Now, with the terminal open, enter `python expense_8_puzzle.py <start file> <goal file> <method>`.
6. The program should then run and print the necessary outputs.

## Notes

- `dfs()` in `depth.py` generally has a large solution output. For this reason, upon finishing, `dfs()` will not print to the console but will print the solution in a file called `dfs.txt`.
- This implementation uses a significant
