#
#
# assistant_Math.py
# Author -> GoldenDuck5 (github)
# Code Parsing and Refactoring -> TheVigilante51 (github)
#
#

import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, solve, simplify, plot


def solve_equation(equation_str):
    """Solve a mathematical equation."""
    try:
        x = symbols('x')
        equation = eval(equation_str)
        solutions = solve(equation, x)
        return solutions
    except Exception as e:
        return f"Error solving equation: {e}"

def simplify_expression(expression_str):
    """Simplify a mathematical expression."""
    try:
        x = symbols('x')
        expression = eval(expression_str)
        simplified = simplify(expression)
        return simplified
    except Exception as e:
        return f"Error simplifying expression: {e}"

def plot_function(expression_str):
    """Plot a mathematical function."""
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(expression_str)
        plt.plot(x, y)
        plt.title(f"Plot of {expression_str}")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.grid()
        plt.show()
    except Exception as e:
        return f"Error plotting function: {e}"


