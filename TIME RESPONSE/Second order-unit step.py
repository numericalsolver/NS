import numpy as np
from scipy.signal import lti, step
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define circuit parameters (R, L, C values)
R = 1.0
L = 1.0
C = 1.0

# Define the transfer function of the circuit (second-order)
numerator = [1]
denominator = [L*C, R*C, 1]
system = lti(numerator, denominator)

# Step 1: Define time points for simulation
t = np.linspace(0, 10, 1000)

# Step 2: Input signal (for example, a unit step function)
u = np.ones_like(t)

# Step 3: Simulate the circuit's response
t_response, y_response = step(system, T=t)

# Create a figure and axis for the plot
plt.figure()
plt.plot(t_response, y_response, color='b')
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response of the Second-Order RLC Circuit')
plt.grid(True)

# Find the index where the response crosses 63.2% of its final value
final_value = y_response[-1]
threshold = 0.632 * final_value
crossing_index = np.argmax(y_response > threshold)
time_constant = t_response[crossing_index]

# Function to mark time response specifications on x-axis and corresponding values on y-axis
def mark_specifications():
    # Calculate time response specifications
    rise_time_index = np.argmax(y_response > 0.9)
    rise_time = t_response[rise_time_index]
    rise_value = y_response[rise_time_index]

    peak_time_index = np.argmax(y_response)
    peak_time = t_response[peak_time_index]
    peak_value = y_response[peak_time_index]

    settling_time_index = np.argmax(np.abs(y_response - 1) < 0.02)
    settling_time = t_response[settling_time_index]
    settling_value = y_response[settling_time_index]

    # Calculate delay time
    delay_time_index = np.argmax(y_response > 0.5)  # 50% of the final value
    delay_time = t_response[delay_time_index]
    delay_value = y_response[delay_time_index]

    # Calculate peak overshoot
    steady_state_value = 1.0  # Steady-state value assuming a unit step input
    peak_overshoot = (peak_value - steady_state_value) / steady_state_value * 100  # Convert to percentage

    # Annotate peak overshoot
    plt.text(peak_time, peak_value, f'Peak overshoot percentage{peak_overshoot:.2f}%', color='black', va='bottom', ha='left')

    # Draw a horizontal line indicating the steady-state value
    plt.axhline(y=steady_state_value, color='gray', linestyle='--', label='Steady State')

    # Annotate the steady-state value
    plt.text(-0.5, steady_state_value, f'Steady State: {steady_state_value}', color='gray', va='bottom')

    # Mark time response specifications on the plot
    plt.axvline(x=rise_time, color='red', linestyle='--', ymax=rise_value, ymin=0, label=f'$t_r$: {rise_time:.2f} s')
    plt.text(rise_time, -0.1, r'$t_r$', color='red', ha='center')
    plt.text(-0.5, rise_value, f'{rise_value:.2f}', color='red', va='center')

    plt.axvline(x=peak_time, color='green', linestyle='--', ymax=peak_value, ymin=0, label=f'$t_p$: {peak_time:.2f} s')
    plt.text(peak_time, -0.1, r'$t_p$', color='green', ha='center')
    plt.text(-0.5, peak_value, f'{peak_value:.2f}', color='green', va='center')

    plt.axvline(x=settling_time, color='magenta', linestyle='--', ymax=settling_value, ymin=0, label=f'$t_s$: {settling_time:.2f} s')
    plt.text(settling_time, -0.1, r'$t_s$', color='magenta', ha='center')
    plt.text(-0.5, settling_value, f'{settling_value:.2f}', color='magenta', va='center')

    plt.axvline(x=delay_time, color='orange', linestyle='--', ymax=delay_value, ymin=0, label=f'$t_d$: {delay_time:.2f} s')
    plt.text(delay_time, -0.1, r'$t_d$', color='orange', ha='center')
    plt.text(-0.5, delay_value, f'{delay_value:.2f}', color='orange', va='center')

    # Mark time constant on the plot
    plt.axvline(x=time_constant, color='purple', linestyle='--', ymax=threshold, ymin=0, label=f'Time Constant: {time_constant:.2f} s')
    plt.text(time_constant, -0.1, r'Time', color='purple', ha='center', va='bottom')
    plt.text(time_constant, -0.15, r'Constant', color='purple', ha='center', va='bottom')
    plt.text(-0.5, threshold, f'{threshold:.2f}', color='purple', va='center')

    # Draw horizontal dotted lines
    plt.plot([0, delay_time], [delay_value, delay_value], color='orange', linestyle='--')
    plt.plot([0, rise_time], [rise_value, rise_value], color='red', linestyle='--')
    plt.plot([0, peak_time], [peak_value, peak_value], color='green', linestyle='--')
    plt.plot([0, settling_time], [settling_value, settling_value], color='magenta', linestyle='--')
    plt.plot([0, time_constant], [threshold, threshold], color='purple', linestyle='--')

# Call the function to mark time response specifications
mark_specifications()

# Show the legend outside the graph
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

