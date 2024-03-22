import re
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from tabulate import tabulate

def parse_transfer_function(expression):
    # Split expression into numerator and denominator parts
    num_str, den_str = re.split(r'/', expression)
    
    # Parse numerator coefficients
    num_terms = re.findall(r'(-?\d+\.\d+|-?\d+)(?:s\^?(\d*))?', num_str)
    num_coefficients = [float(term[0]) if term[0] != '' else 1.0 for term in num_terms]
    num_exponents = [int(term[1]) if term[1] != '' else 1 for term in num_terms]

    # Parse denominator coefficients
    den_terms = re.findall(r'(-?\d+\.\d+|-?\d+)(?:s\^?(\d*))?', den_str)
    den_coefficients = [float(term[0]) if term[0] != '' else 1.0 for term in den_terms]
    den_exponents = [int(term[1]) if term[1] != '' else 1 for term in den_terms]

    # Create arrays for numerator and denominator coefficients
    num = np.zeros(max(num_exponents) + 1)
    den = np.zeros(max(den_exponents) + 1)
    print("Numerator coefficients:", num)
    print("Denominator coefficients:", den)


    # Assign coefficients based on exponents
    for coefficient, exponent in zip(num_coefficients, num_exponents):
        num[exponent] = coefficient

    for coefficient, exponent in zip(den_coefficients, den_exponents):
        den[exponent] = coefficient

    return num, den


def plot_polar(num, den):
    # Create transfer function
    tf = ctrl.TransferFunction(num, den)
    
    # Calculate frequency response
    omega = np.logspace(-3, 3, 1000)
    magnitude, phase, _ = ctrl.bode_plot(tf, omega)

    # Plot polar plot
    plt.figure()
    plt.plot(phase * np.pi / 180, magnitude)
    plt.title('Polar Plot')
    plt.xlabel('Phase (radians)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)
    plt.show()

    # Format magnitude and phase into a table
    table = []
    for w, mag, ph in zip(omega, magnitude, phase):
        table.append([w, mag, ph])

    headers = ["Frequency (rad/s)", "Magnitude (dB)", "Phase (degrees)"]

    return table, headers

# User input
expression = input("Enter the transfer function expression (e.g., '1 + 4s / 2s^2 + 3s + 5'): ")

# Parse transfer function expression
num, den = parse_transfer_function(expression)

# Plot polar plot
table, headers = plot_polar(num, den)

# Display magnitude and phase values in a table
print(tabulate(table, headers=headers, tablefmt="grid"))
print("Numerator coefficients:", num)
print("Denominator coefficients:", den)
