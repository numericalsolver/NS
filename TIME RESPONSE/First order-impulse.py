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

# Step 2: Define the impulse input signal
impulse_input = np.zeros_like(t)
impulse_input[0] = 1  # Unit impulse at t = 0

# Step 3: Simulate the circuit's response to the impulse input
t_response, y_response= impulse(system, T=t)

# Create a figure and axis for the plot
plt.figure()
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Impulse Response Animation of the First-Order RC Circuit')
plt.grid(True)

# Find the index where the response crosses 63.2% of its final value
final_value = y_response[-1]
threshold = 0.632 * final_value
crossing_index = np.argmax(y_response > threshold)
time_constant = t_response[crossing_index]

# Plot the impulse input signal as a vertical arrow at t=0
plt.arrow(0, 0, 0, 1, head_width=0.1, head_length=0.05, fc='r', ec='r', label='Impulse Input')

# Show the legend outside the graph
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


# Function to update the plot for each frame of the animation
frames = 100  # Number of frames
step_size = len(t_response) // frames

for i in range(0, len(t_response), step_size):
    remaining_points = len(t_response) - i
    if remaining_points < step_size:
        step_size = remaining_points
    plt.plot(t_response[:i], y_response[:i], color='b')
    
    plt.draw()
    plt.pause(0.005)  # Decreased delay between frames
    
# Calculate the time constant (tau)
time_constant = R * C

# Mark the time constant on the plot
threshold = np.exp(-1)  # 1/e or approximately 36.8% of the initial amplitude
plt.axvline(x=time_constant, color='purple', linestyle='--', ymax=threshold, ymin=0, label=f'Time Constant: {time_constant:.2f} s')
plt.text(time_constant, -0.1, r'Time', color='purple', ha='center', va='bottom')
plt.text(time_constant, -0.15, r'Constant', color='purple', ha='center', va='bottom')
plt.plot([0, time_constant], [threshold, threshold], color='purple', linestyle='--')
plt.text(-0.5, threshold, f'{threshold:.2f}', color='purple', va='center')

plt.show()



