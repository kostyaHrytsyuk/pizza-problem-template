from init_solver import InitSolverSilly
from solution import Solution

import time

class Solver:

    problem = None
    trace = None

    def __init__(self, problem):
        self.problem = problem

    def description(self):
        """
        :return: String with the description of the approach
        """
        # TODO: Place your algorithm's description here
        return ""

    def initial_solution(self):
        """
        Finds an initial solution for the problem
        :return: Solution object
        """
        # TODO: If you want you may change an initial solution generation
        # init_solver = InitSolverSilly()
        init_solver = InitBetterSolverSilly()
        solution = init_solver.run(self.problem)
        return solution

    def search(self, solution, time_limit=float('inf')):
        """
        Runs a search to optimize the solution. The run is limited by time limit (in seconds)
        :param solution: the initial solution object
        :param time_limit: run time limit (in seconds)
        :return: Solution object after optimization, list of the traced solutions' score
        """
        # TODO: implement your search procedure. Do not forget about time limit!
        raise Exception("Implement your search procedure")
        return optimized_solution

    def get_search_trace(self):
        return self.trace


class InitBetterSolverSilly:
    possible_to_fill_row = True

    def run(self, problem):
        """
        @type problem: Problem
        :rtype: Solution
        """
        sol = Solution(problem)
        formats = problem.slices_formats()
        formats = sorted(formats, key=lambda x: x[0]*x[1], reverse=True)
        row, col = 0, 0
        while True:
            for f in formats:
                if self.possible_to_fill_row and sol.is_free_space(row, col, f[0], f[1]) and problem.is_valid_slice(row, col, f[0], f[1]):
                    sol.create_new_slice(row, col, f[0], f[1])
                    if not self.check_possibility_to_fill_row(sol, row, col+f[1]):
                        row += 1
                        col = 0
                    else:
                        col += f[1]
                    break
            else:
                col += 1
            if col >= problem.max_width:
                row += 1
                col = 0
            if row >= problem.max_height:
                break
            # print(row, col)
        return sol

    def check_possibility_to_fill_row(self, solution, row, column):
        if column >= len(solution.free[0]):
            return True
        for i in range(column, len(solution.free[row])):
            if solution.free[row][i] == True:
                return True
        return False
