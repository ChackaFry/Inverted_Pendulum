import sympy as sym
from sympy import Eq
import numpy as np

# Symbols
M, m, ell, g, x1, x2, x3, x4, F = sym.symbols('M, m, ell , g, x1 , x2 , x3 , x4 , F', real=True)

# Equations
phi_numer = 4 * m * ell * x4 ** 2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) * sym.cos(x3)
phi_denom = 4 * (M + m) - 3 * m * sym.cos(x3) ** 2
phi = phi_numer / phi_denom
psi_numer = m * ell * x4 ** 2 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) * g * sym.sin(x3)
psi_denom = (4 * (M + m) - 3 * m * sym.cos(x3) ** 2) * ell
psi = -3 * psi_numer / psi_denom


# Now implement the following function that takes a symbolic
# expression that depends on F, x3 and x4 and evaluates it
# at F=0, x3=0 and x4=0
def evaluate_at_equilibrium(equation):
    '''
    Substitutes in equilibrium values of F, x3, x4
    :param equation: Represents the equation which the equilibrium values will be substituted into
    :return: equation with equilibrium values substituted in an simplified
    '''
    return equation.subs([(F, 0), (x3, 0), (x4, 0)])


def evaluate_linearised_constants(constant, subs):
    return constant.subs(subs)


# Compute phi at the equilibrium point
# Compute the derivatives of phi at the equilibrium point
# Do the same for psi
functions = (phi, psi)
equilibriate_at = (F, x3, x4)

answers_diff = []

for function in functions:
    # Computing each function at the equilibrium point
    # equil = evaluate_at_equilibrium(function)
    derivative_answer = []

    for value in equilibriate_at:
        # Computing each derivative at the equilibrium point
        diff = evaluate_at_equilibrium(function.diff(value))
        derivative_answer.append(diff)
    answers_diff.append(derivative_answer)

print(f"Functions Derivated at {equilibriate_at}\n {answers_diff}\n")

x1_dot, x2_dot, x3_dot, x4_dot = sym.symbols("x1_dot, x2_dot, x3_dot, x4_dot")  # states
a, b, c, d = sym.symbols("a, b, c, d", real=True, positive=True)  # constants

# Linearise the System by Taylor's Theorem
eq1 = Eq(x2, x1_dot)
eq2 = Eq(a * (F - 0) - b * (x3 - 0), x2_dot)
eq3 = Eq(x4, x3_dot)
eq4 = Eq(- c * (F - 0) + d * (x3 - 0), x4_dot)

equations = [eq1, eq2, eq3, eq4]
print(f"Linearised Equation: \n{equations}\n")

# Question 2
# Laplace Functions
X1, X2, X3, X4, F_lap, s = sym.symbols("X1, X2, X3, X4, F_lap, s")
t = sym.symbols("t", real=True, positive=True)

laplace_functions = []
for equation in equations:
    new = equation.subs(([x1_dot, s * X1], [x2_dot, s * X2],
                         [x3_dot, s * X3], [x4_dot, s * X4],
                         [x1, X1], [x2, X2], [x3, X3], [x4, X4],
                         [F, F_lap]))
    laplace_functions.append(new)
    # print(new)
print(f"Laplace Equations: \n{laplace_functions}\n")

# Question3
G_theta = -c / (s ** 2 - d)
G_x = a / (s ** 2) \
      - b * c / (d * (s ** 2 - d)) \
      + b * c / (d * s ** 2)

transfers = [G_theta, G_x]

omega = sym.symbols("w", real=True)
inputs = [(1), (1 / s), (omega / (s ** 2 + omega ** 2))]

lap_responses = []
responses = []

for G in transfers:
    lap_outputs = []
    outputs = []
    for F_lap_val in inputs:
        # Laplace Outputs
        lap_output = G * F_lap
        lap_output = lap_output.subs(F_lap, F_lap_val)
        lap_outputs.append(lap_output)
        # Time Domain Outputs
        output = (sym.inverse_laplace_transform(lap_output, s, t)).simplify()
        outputs.append(output)
        print(f"Transfer Function: {G} \nLaplace Input: {F_lap_val}"
              f"\nLaplace Output: {lap_output} \nTime Domain: {output}\n")
    lap_responses.append(lap_outputs)
    responses.append(outputs)

print("LaTex Time Domain Outputs:")
for r in responses:
    for o in r:
        print(f"\[{sym.latex(o)}\]\n")

# Post Q3
# Constants
substitutions = [(M, 0.3), (m, 0.1), (ell, 0.35), (g, 9.81)]
a_val = evaluate_linearised_constants(answers_diff[0][0], substitutions)
b_val = -evaluate_linearised_constants(answers_diff[0][1], substitutions)
c_val = -evaluate_linearised_constants(answers_diff[1][0], substitutions)
d_val = evaluate_linearised_constants(answers_diff[1][1], substitutions)

print(f"Values of a, b, c, d at {substitutions}: ")
for val in [a_val, b_val, c_val, d_val]:
    print(val)
print()