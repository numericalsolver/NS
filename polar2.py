import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

def transfer_function(w, input_function):
    # Define the transfer function
    s = symbols('s')
    H = lambdify(s, input_function)(1j * w)
    return H

input_function = input("Enter the transfer function (use 's' for the Laplace variable): ")

# Replace '^' with '**' for exponentiation
input_function = input_function.replace('^', '**')

# Generate frequency range
w = np.linspace(0, 8*np.pi, 1000)

# Calculate the transfer function
H = transfer_function(w, input_function)

# Exclude frequencies where division by zero occurs
valid_indices = np.where(np.abs(H) != np.inf)[0]
w_valid = w[valid_indices]
H_valid = H[valid_indices]

# Identify points where the curve touches the real axis
real_axis_points = []
for i in range(len(H_valid) - 1):
    if np.imag(H_valid[i]) * np.imag(H_valid[i+1]) < 0:
        # Curve crosses the real axis between these points
        # Linear interpolation to find the crossing point
        t = np.imag(H_valid[i]) / (np.imag(H_valid[i]) - np.imag(H_valid[i+1]))
        crossing_point = (1 - t) * w_valid[i] + t * w_valid[i+1]
        real_axis_points.append(crossing_point)

# Plot real and imaginary axes
plt.figure(figsize=(8, 6))
plt.plot([-np.max(np.abs(H_valid)), np.max(np.abs(H_valid))], [0, 0], 'k')  # Real axis
plt.plot([0, 0], [-np.max(np.abs(H_valid)), np.max(np.abs(H_valid))], 'k')  # Imaginary axis

# Plot polar plot
plt.plot(np.real(H_valid), np.imag(H_valid))
plt.scatter(np.real(real_axis_points), np.zeros_like(real_axis_points), color='red', marker='o', label='Crossing Points')

# Plot arrows indicating direction of the curve (if there are crossing points)
if real_axis_points:
    for point in real_axis_points:
        idx = np.argmin(np.abs(w_valid - point))
        if idx > 0 and idx < len(w_valid) - 1:
            direction = np.sign(np.imag(H_valid[idx + 1]) - np.imag(H_valid[idx - 1]))
            plt.arrow(np.real(point), 0, direction * 0.1, 0, color='blue', head_width=0.1, head_length=0.05)

plt.title('Polar Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)
plt.legend()

# Set equal aspect ratio for better visualization
plt.gca().set_aspect('equal', adjustable='box')

# Tabulate first 40 magnitude and phase values
mag = np.abs(H_valid)
phase = np.angle(H_valid, deg=True)
print("Frequency\tMagnitude\tPhase")
for i in range(40):
    print(f"{w_valid[i]:.2f}\t\t{mag[i]:.4f}\t\t{phase[i]:.4f}")

plt.tight_layout()
plt.show()
