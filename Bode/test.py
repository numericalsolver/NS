import numpy as np
import matplotlib.pyplot as plt
import control
from matplotlib.animation import FuncAnimation

# Suppress warnings for this example
import warnings
warnings.filterwarnings('ignore')

# Define the system
G = 0.2*control.tf([0.5, 1], [1.5, 0.5, 1])
(num, den) = control.pade(0.25, 3)
Gp = control.tf(num, den) * G

# Initialize the plot
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title("Bode Magnitude")
ax1.set_ylabel("Magnitude (dB)")
ax2.set_title("Bode Phase")
ax2.set_ylabel("Phase (degrees)")
ax2.set_xlabel("Frequency (rad/sec)")

# Initialize empty lines for the plot
line_mag, = ax1.semilogx([], [], 'b-', label='Magnitude')
line_phase, = ax2.semilogx([], [], 'b-', label='Phase')

# Initialize the frequencies and magnitudes
frequencies = np.logspace(-1.5, 1, 200)
magnitudes = np.zeros_like(frequencies)
phases = np.zeros_like(frequencies)

# Function to update the plot
def update(frame):
    # Add one frequency point and calculate magnitude and phase
    f = frequencies[:frame]
    mag, phase, _ = control.bode(Gp, f)
    magnitudes[:frame] = mag
    phases[:frame] = phase

    # Update the plot data
    line_mag.set_data(f, magnitudes[:frame])
    line_phase.set_data(f, phases[:frame])

    return line_mag, line_phase

# Create the animation
ani = FuncAnimation(fig, update, frames=len(frequencies), blit=True)

# Show the plot
plt.legend()
plt.show()
