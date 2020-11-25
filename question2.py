from sympy import Eq
from question1 import *

x1_dot, x2_dot, x3_dot, x4_dot = sym.symbols("\dot{x_1}, \dot{x_2}, \dot{x_3}, \dot{x_4}")  # states
a, b, c, d = sym.symbols("a, b, c, d", real=True, positive=True)  # Constants

# Linearised System by Taylor's Theorem
eq1 = Eq(x1_dot, x2)
eq2 = Eq(x2_dot, a * (F - 0) - b * (x3 - 0))
eq3 = Eq(x3_dot, x4)
eq4 = Eq(x4_dot, - c * (F - 0) + d * (x3 - 0))

equations = [eq1, eq2, eq3, eq4]

X1, X2, X3, X4, F_lap, s = sym.symbols("X1, X2, X3, X4, F_lap, s")
t = sym.symbols("t", real=True, positive=True)

# Laplace of Linearised Systems
laplace_functions = []
for equation in equations:
    new = equation.subs(([x1_dot, s * X1], [x2_dot, s * X2],
                         [x3_dot, s * X3], [x4_dot, s * X4],
                         [x1, X1], [x2, X2], [x3, X3], [x4, X4],
                         [F, F_lap]))
    laplace_functions.append(new)

if __name__ == '__main__':
    print("Question 2\n----------")
    print(f"Linearised Equation:")
    print("\\begin{align}")
    for eq in equations:
        print(sym.latex(eq).replace("=", "&=") + "\\cr")
    print("\\end{align}")

    print(f"\nLaplace Equations:")
    print("\\begin{align}")
    for func in laplace_functions:
        print(sym.latex(func).replace("=", "&=") + "\\cr")
    print("\\end{align}")