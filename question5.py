from question4 import *

# Creating a Control PID Controller
def pid(kp, kd, ki):
    return ctrl.TransferFunction([kd, kp, ki], [1, 0])

# Finds the element number which first passes split_var
def elementAt(arr, split_val):
    for x in range(len(arr)):
        if (arr[x] >= split_val):
            return x


t_final = 1  # Simulate for 1s
num_points = 501
time_span = np.linspace(0, t_final, num_points)
cutAt = elementAt(time_span, 0.4)

plot_number = 0  # Counts the number of graphs plotted
best_range = 100  # Keeps track of current best values
best_solution = [0, 0, 0]  # Values of the current best PID values

# Keeps track of the difference between maximum and minimum
# deviation from equilibrium position
ranges = []

# Range of 0.085deg is good enough, for the overall system. So remove last 2 values
# test_values = [0.001, 0.01, 0.1, 1, 10, 100, 10 ** 3, 10 ** 4, 10 ** 5, 10**6, 10**7]

# First 2 values don't seem to show up for any of the constants. So remove first 2 values
# test_values = [0.001, 0.01, 0.1, 1, 10, 100, 10 ** 3, 10 ** 4, 10 ** 5]

test_values = [0.1, 1, 10, 100, 10 ** 3]

for kp in test_values:
    for kd in test_values:
        for ki in test_values:
            # -ve for Negative Feedback.
            controller = -pid(kp, kd, ki)  # PID Controller

            # PID Controller Inputting to Rod
            theta_closed = ctrl.feedback(theta_tf, controller)

            # Kick the system
            t_imp, theta_imp = ctrl.impulse_response(theta_closed, T=time_span)

            theta_imp = np.rad2deg(theta_imp)  # Convert degrees to radians

            # Filtering

            # Valid Solution must only have peaks at -0.5 and 0.5
            if (not (max(theta_imp) > 5 or min(theta_imp) < -5)):
                theta2_imp = theta_imp[cutAt:]

                # After t=0.4, Valid Solution must only have peaks at 0 and 0.1
                if (not (max(theta2_imp) > 0.1 or min(theta2_imp) < 0)):
                    range = max(theta_imp) - min(theta_imp)

                    # Plot the graph only if it has better characteristics than last graph
                    if (range < best_range):
                        best_range = range
                        plt.plot(t_imp, theta_imp, label=f"[{kp}, {kd}, {ki}]")
                        # plt.title(f"[{kp} {kd} {ki}] : {range}")
                        # plt.show()
                        plot_number += 1
                        print(f"{plot_number} : [{kp}, {kd}, {ki}] : {range}")
                        best_solution = [kp, kd, ki]
                        ranges.append(range)

print(best_solution)

if __name__ == '__main__':
    plt.legend()
    plt.title("Effects of Changing PID Constants on Response of the System")
    plt.xlabel("Time, t(s)")
    plt.ylabel("Rotation of Rod, θ(°)")
    plt.savefig("Figures\Changing_PID_Constants.eps", format="eps")
    plt.show()

    # Re-Simulate the best solution
    controller = -pid(best_solution[0], best_solution[1], best_solution[2])
    theta_closed = ctrl.feedback(theta_tf, controller)
    t_imp, theta_imp = ctrl.impulse_response(theta_closed, T=time_span)
    theta_imp = np.rad2deg(theta_imp)

    # Plot the best solution
    plt.plot(t_imp, theta_imp)
    plt.title(f"Response of Rod with kp={best_solution[0]}, kd={best_solution[1]}, ki={best_solution[2]}")
    plt.xlabel("Time, t(s)")
    plt.ylabel("Rotation of Rod, θ(°)")
    plt.savefig("Figures\Best_Solution.eps", format="eps")
    plt.show()
else:
    plt.clf()
