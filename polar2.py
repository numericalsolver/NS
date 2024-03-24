import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

def transfer_function(w):
    # Define the transfer function
    s = symbols('s')
    H = lambdify(s, input_function)(1j * w)
    return H

input_function = input("Enter the transfer function (use 's' for the Laplace variable): ")

# Replace '^' with '**' for exponentiation
input_function = input_function.replace('^', '**')

# Generate frequency range
w = np.logspace(-1, 10, 1000)

# Calculate the transfer function
H = transfer_function(w)

# Plot real and imaginary axes
plt.figure(figsize=(8, 6))
plt.plot([-np.max(np.abs(H)), np.max(np.abs(H))], [0, 0], 'k')  # Real axis
plt.plot([0, 0], [-np.max(np.abs(H)), np.max(np.abs(H))], 'k')  # Imaginary axis

# Plot polar plot
plt.plot(np.real(H), np.imag(H))
plt.title('Polar Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)

# Set equal aspect ratio for better visualization
plt.gca().set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()

# Tabulate first 40 magnitude and phase values
mag = np.abs(H)
phase = np.angle(H, deg=True)
print("Frequency\tMagnitude\tPhase")
for i in range(40):
    print(f"{w[i]:.2f}\t\t{mag[i]:.4f}\t\t{phase[i]:.4f}")

plt.tight_layout()
plt.show() 
