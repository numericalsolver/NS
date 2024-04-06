import numpy as np
from scipy.signal import lti, lsim, impulse
import matplotlib.pyplot as plt

# Define circuit parameters (R, C values)
R = 1.0
C = 1.0

# Define the transfer function of the circuit (first-order)
numerator = [1]
denominator = [R*C, 1]
system = lti(numerator, denominator)

# Step 1: Define time points for simulation
t = np.linspace(0, 10, 1000)

# Step 2: Define unit parabolic input signal
u_parabolic = t**2

# Step 3: Simulate the circuit's response to the unit parabolic input
t_response, y_response, _ = lsim(system, U=u_parabolic, T=t)


# Create a figure and axis for the plot
plt.figure()
plt.plot(t_response, y_response, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Parabolic Response of the First-Order RC Circuit')
plt.grid(True)

# Plot the unit parabolic input signal
plt.plot(t, u_parabolic, 'r--', label='Unit Parabolic Input')

# Show the legend outside the graph
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()




