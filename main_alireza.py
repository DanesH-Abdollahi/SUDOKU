import numpy as np
from dokusan import generators, renderers, solvers
from dokusan.boards import BoxSize, Sudoku

sudoku = generators.random_sudoku(avg_rank=150)  # Generate a Sudoku
print(renderers.colorful(sudoku))  # Print Sudoku

solution = solvers.backtrack(sudoku)  # Solve a Sudoku
print(renderers.colorful(solution))  # Print Solved Sudoku

sudoku_np_array = np.array(list(str(sudoku)), dtype=int).reshape(9, 9)  # Make np_array

sudoku.update(  # Update Sudoku
    Sudoku.from_list(
        sudoku_np_array.tolist(),
        box_size=BoxSize(3, 3),
    ).cells()
)