import numpy as np
from scipy.signal import lti, step
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

# Step 2: Input signal (for example, a unit step function)
u = np.ones_like(t)

# Step 3: Simulate the circuit's response
t_response, y_response = step(system, T=t)

# Create a figure and axis for the plot
plt.figure()
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response Animation of the First-Order RC Circuit')
plt.grid(True)

# Function to update the plot for each frame of the animation
for i in range(len(t_response)):
    plt.plot(t_response[:i], y_response[:i], color='b')
    plt.draw()
    plt.pause(0.01)  # Delay between frames

plt.show()
