from question3 import *
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Get values for an equation
def evaluate_constants(constant, subs):
    return float(constant.subs(subs))

# Numerical values for all constants
substitutions = [(M, 0.3), (m, 0.1), (ell, 0.35), (g, 9.81)]
a_val = evaluate_constants(answers_diff[0][0], substitutions)
b_val = -evaluate_constants(answers_diff[0][1], substitutions)
c_val = -evaluate_constants(answers_diff[1][0], substitutions)
d_val = evaluate_constants(answers_diff[1][1], substitutions)

# Creating Transfer Functions in Control Module.
# the other Transfer Functions were made in SymPy.
theta_tf = ctrl.TransferFunction([-c_val], [1, 0, -d_val])
x_tf = ctrl.TransferFunction([a_val], [1, 0, 0])
x_tf += -ctrl.TransferFunction([b_val*c_val], [d_val, 0, 0])
x_tf += ctrl.TransferFunction([b_val*c_val], [d_val, 0, -1 * d_val**2])

t_final = 0.2  # Simulate for 0.2s

t_span = np.linspace(0, t_final, 501)  # Array of Time Instants
force = np.sin(100 * t_span**2)  # Input Signal

if __name__ == '__main__':
    print(f"Values of a, b, c, d at {substitutions}: ")
    for val in [a_val, b_val, c_val, d_val]:
        print(val)
    print()

    plt.title("Force Input")
    plt.ylabel("Force, F(N)")
    plt.xlabel("Time, t(s)")
    plt.plot(t_span, force)  # Plotting Input
    plt.savefig("Figures\Force_Input.eps", format="eps")
    plt.show()

    t_out, y_out, _ = ctrl.forced_response(theta_tf, t_span, force)
    y_out = np.rad2deg(y_out)
    plt.title("Response of the Rod")
    plt.ylabel("Rotation of Rod, θ(°)")
    plt.xlabel("Time, t(s)")
    plt.plot(t_out, y_out)  # Plotting Rotation of Rod
    plt.savefig("Figures\Response_Rod.eps", format="eps")
    plt.show()

    t_out, y_out, _ = ctrl.forced_response(x_tf, t_span, force)
    plt.title("Response of the Cart")
    plt.ylabel("Horizontal Displacement, x(m)")
    plt.xlabel("Time, t(s)")
    plt.plot(t_out, y_out)  # Plotting Movement of Cart
    plt.savefig("Figures\Response_Cart.eps", format="eps")
    plt.show()