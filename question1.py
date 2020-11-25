import sympy as sym


# Evaluate expressions at F=0, x3=0 and x4=0
def evaluate_at_equilibrium(equation):
    '''
    Substitutes in equilibrium values of F, x3, x4
    :param equation: Represents the equation which the equilibrium values will be substituted into
    :return: equation with equilibrium values substituted in an simplified
    '''
    return equation.subs([(F, 0), (x3, 0), (x4, 0)])


# Defining Symbols
M, m, ell, g, x1, x2, x3, x4, F = sym.symbols('M, m, ell , g, x_1 , x_2 , x_3 , x_4 , F')
phi_numer = 4 * m * ell * x4 ** 2 * sym.sin(x3) + 4 * F - 3 * m * g * sym.sin(x3) \
            * sym.cos(x3)
phi_denom = 4 * (M + m) - 3 * m * sym.cos(x3) ** 2
phi = phi_numer / phi_denom  # Equation for Phi

psi_numer = m * ell * x4 ** 2 * sym.sin(x3) * sym.cos(x3) + F * sym.cos(x3) - (M + m) \
            * g * sym.sin(x3)
psi_denom = (4 * (M + m) - 3 * m * sym.cos(x3) ** 2) * ell
psi = -3 * psi_numer / psi_denom  # Equation for Psi

# Used to get properly formatted LaTeX output
functions = (phi, psi)
str_functions = ("phi", "psi")
equilibriate_at = (F, x3, x4)

answers_diff = []  # Holds all the equilibrated values

# Computing derivatives of phi and psi at the equilibrium point
for function in functions:
    derivative_answer = []
    for value in equilibriate_at:
        # Computing each derivative at the equilibrium point
        diff = evaluate_at_equilibrium(function.diff(value))
        derivative_answer.append(diff)
    answers_diff.append(derivative_answer)

if __name__ == '__main__':
    print("Question 1\n----------")
    print(f"Functions Derivated at {equilibriate_at}:")
    for x in range(len(answers_diff)):
        for y in range(len(answers_diff[x])):
            # Generating LaTeX
            print("\\frac{\\partial \\" + str_functions[x]
                  + f"{equilibriate_at}"+"}{\\partial " + sym.latex(equilibriate_at[y])
                  + "}" + f" &= {sym.latex(answers_diff[x][y])}\\cr")
        print("\\cr")
    print()
