# sudoku-solver
Solving sudoku with backtracking algorithm

Given a sudoku problem, the algorithm runs through the board and solves it using backtracking method.
The idea is to put the first possible solution in each cell and move forward, once it is not possible to fit any number in the given cell, the algorithm goes back to the lastly changed cell and changes it to the next possible number. The principle is continued untill the board is solved. Therefore, the algorithm is expectidly slow.
