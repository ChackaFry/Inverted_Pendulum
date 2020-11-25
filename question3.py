from question2 import *

# Transfer Function with F_lap as input
G_theta = -c / (s ** 2 - d)  # Output is X3
G_x = a / (s ** 2) \
      + b * c / (d * (s ** 2 - d)) \
      - b * c / (d * s ** 2)  # Output is X1

transfers = [G_theta, G_x]  # Transfer Functions
str_transfers = ["G_{\\theta}", "G_x"]  # Transfer Function Names

if __name__ == '__main__':
    omega = sym.symbols("w", real=True)

    # Impulse Response is F_lap = 1 in s-domain
    # Step Response is F_lap = 1/s in s-domain
    # Frequency Response is F = sin(wt) in t-domain for this particular example
    # Frequency Response is F_lap = (w / (s**2 + w**2) in s-domain
    inputs = [(1), (1 / s), (omega**2 / (s ** 2 + omega ** 2))]
    str_inputs = ["Impulse Response", "Step Response", "Frequency Response"]

    responses_s = []  # Response in the s-domain
    responses_t = []  # Response in the t-domain

    for x in range(len(transfers)):
        G = transfers[x]  # Each Transfer Function
        str_G = str_transfers[x]  # Name fo Transfer Function

        lap_outputs = []
        outputs = []

        #print("Transfer Function:")
        #print("\\[" + str_G + "=" + sym.latex(G) + "\\]")

        for y in range(len(inputs)):
            F_lap_in = inputs[y]

            # Laplace Outputs
            lap_output = G * F_lap
            lap_output = lap_output.subs(F_lap, F_lap_in).simplify()
            lap_outputs.append(lap_output)

            # Time Domain Outputs
            output = (sym.inverse_laplace_transform(lap_output, s, t)).simplify()
            outputs.append(output)

            # Creating LaTeX Output
            print(str_inputs[y] + f" of ${str_G}$: ")
            print("\\[" + str_G + "\\times" + sym.latex(F_lap_in) + "="
                  + sym.latex(lap_output) + "\\]")
            print("\\[ \lap^{-1} \\{" + str_G + "\\times" + sym.latex(F_lap_in)
                  + "\\} (t) =" + sym.latex(output) + "\\]")

        responses_s.append(lap_outputs)
        responses_t.append(outputs)
