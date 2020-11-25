from question5 import *

# Setting Up Controller to feedback to the Cart, instead of Rod
controller = -pid(best_solution[0], best_solution[1], best_solution[2])
x_closed = ctrl.feedback(x_tf, controller)
t_imp, x_imp = ctrl.impulse_response(x_closed, T=time_span)

# Plotting the Response of the Cart for 1s
plt.plot(t_imp, x_imp)
plt.title(f"Response of Cart")
plt.xlabel("Time, t(s)")
plt.ylabel("Position of Car, x(m)")
plt.savefig("Figures\Response_Cart.eps", format="eps")
plt.show()

# Printing the Transfer Function of the feedback system.
print(x_closed)