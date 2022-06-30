# import pygame
# import time
# import dokusan
# pygame.font.init()

from dokusan import generators, renderers, solvers
from dokusan.boards import BoxSize, Sudoku
import numpy as np

sudoku = generators.random_sudoku(avg_rank=150)
# print(sudoku)

sudoku_np_array = np.array(list(str(sudoku))).reshape(9, 9)
sudoku_list = 
# print(sudoku_np_array)

# print(list(sudoku_np_array))

temp = Sudoku.from_list(
    list(sudoku_np_array),
    box_size=BoxSize(3, 3),
)

sudoku.update(temp.cells())
print(sudoku)

# print(renderers.colorful(sudoku))

# print(sudoku.is_valid())

# sudoku = Sudoku.from_list(
#     [
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 3, 0, 8, 5],
#         [0, 0, 1, 0, 2, 0, 0, 0, 0],
#         [0, 0, 0, 5, 0, 7, 0, 0, 0],
#         [0, 0, 4, 0, 0, 0, 1, 0, 0],
#         [0, 9, 0, 0, 0, 0, 0, 0, 0],
#         [5, 0, 0, 0, 0, 0, 0, 7, 3],
#         [0, 0, 2, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 4, 0, 0, 0, 9],
#     ],
#     box_size=BoxSize(3, 3),
# )

# sudoku1 = Sudoku.from_list(
#     [
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 3, 0, 8, 5],
#         [0, 0, 1, 0, 2, 0, 0, 0, 0],
#         [0, 0, 0, 5, 0, 7, 0, 0, 0],
#         [0, 0, 4, 0, 0, 0, 1, 0, 0],
#         [0, 9, 0, 0, 0, 0, 0, 0, 0],
#         [5, 0, 0, 0, 0, 0, 0, 7, 3],
#         [0, 0, 2, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 4, 0, 0, 0, 9],
#     ],
#     box_size=BoxSize(3, 3),
# )

# sudoku2 = Sudoku.from_string("100080000000100030500000092003098000005070243040000000900000706000009408060002000", box_size=BoxSize(3, 3))
# print(renderers.colorful(sudoku2))

# sudoku.update(sudoku1.cells())
# solution = solvers.backtrack(sudoku)

# print(renderers.colorful(sudoku))
# print(sudoku.)

# print(renderers.colorful(solution))
