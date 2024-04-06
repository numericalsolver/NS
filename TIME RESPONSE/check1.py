import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import control
from sympy import Symbol, Poly, expand, lambdify, inverse_laplace_transform, collect
from scipy.signal import TransferFunction


def mark_specifications(c_t):
    # Define the time points for simulation
    t_values = np.linspace(0, 10, 1000)  # Adjust time range as needed

    # Convert c(t) to a numerical function for plotting
    c_t_numeric = sp.lambdify(sp.Symbol('t'), c_t, modules=['numpy'])

    # Compute the response of c(t) over time
    c_response = c_t_numeric(t_values)

    # Plot the response
    plt.plot(t_values, c_response, color='b')
    plt.xlabel('Time (s)')
    plt.ylabel('Response')
    plt.title('System Response')
    plt.grid(True)

    # Find specifications
    final_value = c_response[-1]
    threshold = 0.632 * final_value
    crossing_index = np.argmax(c_response > threshold)
    time_constant = t_values[crossing_index]

    rise_time_index = np.argmax(c_response > 0.9 * final_value)
    rise_time = t_values[rise_time_index]
    rise_value = c_response[rise_time_index]

    peak_time_index = np.argmax(c_response)
    peak_time = t_values[peak_time_index]
    peak_value = c_response[peak_time_index]

    settling_time_index = np.argmax(np.abs(c_response - final_value) < 0.02 * final_value)
    settling_time = t_values[settling_time_index]
    settling_value = c_response[settling_time_index]

    delay_time_index = np.argmax(c_response > 0.5 * final_value)
    delay_time = t_values[delay_time_index]
    delay_value = c_response[delay_time_index]

    # Mark specifications on the plot
    # Mark time response specifications on the plot
    plt.axvline(x=rise_time, color='red', linestyle='--', ymax=rise_value/final_value, label=f'Rise time($t_r$): {rise_time:.2f} s')
    plt.text(rise_time, -0.05, r'$t_r$', color='red', ha='center')
    plt.text(-0.5, rise_value, f'{rise_value:.2f}', color='red', va='center')

    plt.axvline(x=peak_time, color='green', linestyle='--', ymax=peak_value/final_value, label=f'Peak time($t_p$): {peak_time:.2f} s')
    plt.text(peak_time, -0.05, r'$t_p$', color='green', ha='center')


    plt.axvline(x=settling_time, color='magenta', linestyle='--', ymax=settling_value/final_value, label=f'Settling time($t_s$): {settling_time:.2f} s')
    plt.text(settling_time, -0.05, r'$t_s$', color='magenta', ha='center')
    plt.text(-0.5, settling_value, f'{settling_value:.2f}', color='magenta', va='center')

    plt.axvline(x=delay_time, color='orange', linestyle='--', ymax=delay_value/final_value, label=f'Delay time($t_d$): {delay_time:.2f} s')
    plt.text(delay_time, -0.05, r'$t_d$', color='orange', ha='center')
    plt.text(-0.5, delay_value, f'{delay_value:.2f}', color='orange', va='center')

    # Mark time constant on the plot
    plt.axvline(x=time_constant, color='purple', linestyle='--', ymax=threshold/final_value, label=f'Time Constant: {time_constant:.2f} s')
    plt.text(time_constant, -0.05, r'Time', color='purple', ha='center', va='bottom')
    plt.text(time_constant, -0.08, r'Constant', color='purple', ha='center', va='bottom')
    plt.text(-0.5, threshold, f'{threshold:.2f}', color='purple', va='center')

    # Draw horizontal dotted lines
    plt.plot([0, delay_time], [delay_value, delay_value], color='orange', linestyle='--')
    plt.plot([0, rise_time], [rise_value, rise_value], color='red', linestyle='--')
    plt.plot([0, peak_time], [peak_value, peak_value], color='green', linestyle='--')
    plt.plot([0, settling_time], [settling_value, settling_value], color='magenta', linestyle='--')
    plt.plot([0, time_constant], [threshold, threshold], color='purple', linestyle='--')

    # show plot
    # Show the legend outside the graph
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()




import sympy as sp
import numpy as np

import sympy as sp
import numpy as np

def main():
    # Coefficients of numerator and denominator of R(s)
    num_R = list(map(float, input("Enter coefficients of numerator of R(s) separated by space: ").split()))
    den_R = list(map(float, input("Enter coefficients of denominator of R(s) separated by space: ").split()))

    # Coefficients of numerator and denominator of G(s)
    num_G = list(map(float, input("Enter coefficients of numerator of G(s) separated by space: ").split()))
    den_G = list(map(float, input("Enter coefficients of denominator of G(s) separated by space: ").split()))

    # Coefficients of numerator and denominator of H(s)
    num_H = list(map(float, input("Enter coefficients of numerator of H(s) separated by space: ").split()))
    den_H = list(map(float, input("Enter coefficients of denominator of H(s) separated by space: ").split()))

    # Construct transfer functions R(s), G(s), and H(s)
    R_s = sp.Poly(num_R, sp.Symbol('s')) / sp.Poly(den_R, sp.Symbol('s'))
    G_s = sp.Poly(num_G, sp.Symbol('s')) / sp.Poly(den_G, sp.Symbol('s'))
    H_s = sp.Poly(num_H, sp.Symbol('s')) / sp.Poly(den_H, sp.Symbol('s'))

    # Calculate the transfer function C(s)
    C_s = G_s / (1 + G_s * H_s) * R_s
    C_s = sp.simplify(C_s)

    # Extract numerator and denominator coefficients of C(s)
    num_C, den_C = C_s.as_numer_denom()

    # Calculate natural frequency and damping ratio
    b_m = sp.degree(num_C)
    a_n = sp.degree(den_C)

    if a_n == -sp.oo:
        print("The denominator polynomial is zero. Cannot calculate natural frequency.")
        return
    elif a_n == 0:
        print("The denominator polynomial is constant. Natural frequency and damping ratio are undefined.")
        return

    den_C_poly = den_C.as_poly()
    omega_n = np.sqrt(den_C_poly.coeffs()[-2] / den_C_poly.coeffs()[-1])
    damping_ratio = -den_C_poly.coeffs()[-2] / (2 * omega_n * den_C_poly.coeffs()[-1])


    # Print the results
    print("Degree of denominator polynomial:", a_n)
    print("Natural Frequency:", omega_n)
    print("Damping Ratio:", damping_ratio)

if __name__ == "__main__":
    main()





