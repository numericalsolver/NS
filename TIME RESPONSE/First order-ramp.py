import numpy as np
from scipy.signal import lti, lsim
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

# Step 2: Define ramp input signal
u_ramp = t

# Step 3: Simulate the circuit's response to the ramp input
t_response, y_response, _ = lsim(system, U=u_ramp, T=t)


# Create a figure and axis for the plot
plt.figure()
plt.plot(t_response, y_response)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Ramp Response of the First-Order RC Circuit')
plt.grid(True)

plt.plot(t, t, 'r--', label='Steady state')

# Show the legend outside the graph
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

