import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import control
from sympy import Symbol, Poly, expand, lambdify, inverse_laplace_transform, collect
import base64
from io import BytesIO


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


def main():
    # Coefficients of numerator and denominator of R(s)
    num_R = list(map(float, input("Enter coefficients of numerator of R(s) separated by space: ").split()))
    den_R = list(map(float, input("Enter coefficients of denominator of R(s) separated by space: ").split()))

    # Constructing transfer function R(s)
    R_s = sp.Poly(num_R, sp.Symbol('s')) / sp.Poly(den_R, sp.Symbol('s'))

    
    # Coefficients of numerator and denominator of G(s)
    num_G = list(map(float, input("Enter coefficients of numerator of G(s) separated by space: ").split()))
    den_G = list(map(float, input("Enter coefficients of denominator of G(s) separated by space: ").split()))

    # Constructing transfer function G(s)
    G_s = sp.Poly(num_G, sp.Symbol('s')) / sp.Poly(den_G, sp.Symbol('s'))

    # Coefficients of numerator and denominator of H(s)
    num_H = list(map(float, input("Enter coefficients of numerator of H(s) separated by space: ").split()))
    den_H = list(map(float, input("Enter coefficients of denominator of H(s) separated by space: ").split()))

    # Constructing transfer function H(s)
    H_s = sp.Poly(num_H, sp.Symbol('s')) / sp.Poly(den_H, sp.Symbol('s'))

    # Calculating C(s)
    C_s = G_s / (1 + G_s * H_s) * R_s
    C_s = sp.simplify(C_s)

    # Calculate c(t) by inverse Laplace transform
    c_t = sp.inverse_laplace_transform(C_s, sp.Symbol('s'), sp.Symbol('t'))

    # Simplify and format c(t)
    c_t = sp.simplify(c_t)
    c_t = sp.collect(c_t, sp.exp(-sp.Symbol('t')))




   # Initialize empty lists to store steps and results
    steps = []
    results = []

    # Step 1: Calculate Laplace Transform of the given input signal r(t) to get R(s)
    steps.append("Generalized Transfer Function of 1st order system = C(s)/R(s) = G(s)/[1 + G(s)H(s)]",
                 "Step 1: Calculate Laplace Transform of the given input signal r(t) to get R(s)")
    results.append("Result for Step 1: R(s) = " + str(R_s))

    # Step 2: Substitute the given G(s) i.e open loop transfer function in the above formula
    steps.append("Step 2: Substitute the given G(s) i.e open loop transfer function in the above formula")  
    results.append("Result for Step 2: G(s) = " + str(G_s))

    # Step 3: Substitute the given H(s) i.e negative feedback in the above formula
    steps.append("Step 3: Substitute the given H(s) i.e negative feedback in the above formula")
    results.append("Result for Step 3: H(s) = " + str(H_s))

    # Step 4: Simplify the above equation to get C(s)
    steps.append("Step 4: Simplify the above equation to get C(s)")
    results.append("Result for Step 4: C(s) = " + str(C_s))

    # Step 5: Calculate Inverse Laplace Transform of C(s) to get the output signal c(t)
    steps.append("Step 5: Calculate Inverse Laplace Transform of C(s) to get the output signal c(t)") 
    results.append("Result for Step 5: Output signal c(t) = " + str(c_t))

    # Print the result
  
    print("Transfer Function R(s) =", R_s)
    print("Transfer Function G(s) =", G_s)
    print("Transfer Function H(s) =", H_s)
    print("Transfer Function C(s) =", C_s, "where C(s) is the Laplace transform of the output signal c(t)")
    print("Inverse Laplace Transform of C(s) to get the output signal c(t)=", c_t)

    # Call mark_specifications() to plot the response and mark specifications
    mark_specifications(c_t)

    # Save the plot image to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Close the plot to free up resources

    # Convert to a base64-encoded string
    steps = base64.b64encode('\n'.join(steps).encode('utf-8')).decode('utf-8')
    results = base64.b64encode('\n'.join(results).encode('utf-8')).decode('utf-8')
    image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_data,steps,results


if __name__ == "__main__":
    main()
