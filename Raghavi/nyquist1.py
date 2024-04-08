import control as ct
import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.patches as patches
from tabulate import tabulate
# numerator= [1]#(input("enter the value of the numerator:"))
# denomenator= [1,2,1]#(input("enter the value of the denomenator:"))
numerator=[1]
denominator=[1,2,1]
transfer_function=ct.tf(numerator,denominator)
#step:1
freq_range = np.logspace(-2, 2, 1000)  # Adjust the frequency range as needed

# Initialize arrays to store the real and imaginary parts of the transfer function
real_part = []
imag_part = []

# Compute the frequency response for each frequency
for omega in freq_range:
    s = 1j * omega  # complex frequency s
    H = np.polyval(numerator, s) / np.polyval(denominator, s)  # transfer function H(s)
    real_part.append(H.real)
    imag_part.append(H.imag)
   

# Plot the Nyquist plot
plt.plot(real_part, imag_part, label='Nyquist Plot', color='blue')
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=9, ha='left', va='top',weight='bold', transform=plt.gca().transAxes)


plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Nyquist Plot: s=jω')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()


plt.show()

#step:2
R = 1  # Adjust radius as needed

# Define theta range from 90 to -90 degrees
theta = np.linspace(90, -90, 1000)  # Angle range from 90 to -90 degrees in 1000 steps

# Convert theta to radians
theta_rad = np.deg2rad(theta)

# Compute the complex number s = R * exp(j * theta)
s = R * np.exp(1j * theta_rad)
# Define the transfer function H(s)
def transfer_function(s):
    numerator_value = np.polyval(numerator, s)
    denominator_value = np.polyval(denominator, s)
    return numerator_value / denominator_value

# Compute the frequency response of the transfer function
H = np.array([transfer_function(si) for si in s])

plt.plot(H.real, H.imag)
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=9, ha='left', va='top',weight='bold', transform=plt.gca().transAxes)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Nyquist Plot: Transfer Function')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axis('equal')  # Equal aspect ratio
plt.show()

#step:3
freq_range = np.logspace(-2, 2, 1000)  # Adjust the frequency range as needed

# Initialize arrays to store the real and imaginary parts of the transfer function
real_part = []
imag_part = []

# Compute the frequency response for each frequency
for omega in freq_range:
    s = -1j * omega  # complex frequency s
    H = np.polyval(numerator, s) / np.polyval(denominator, s)  # transfer function H(s)
    real_part.append(H.real)
    imag_part.append(H.imag)

# Plot the Nyquist plot
plt.plot(real_part, imag_part, label='Nyquist Plot', color='blue')
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=9, ha='left', va='top',weight='bold', transform=plt.gca().transAxes)
# Plot settings
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Nyquist Plot: s=-jω')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

# Show plot
plt.show()

#step:4
R = 0  # Adjust radius as needed

# Define theta range from 90 to -90 degrees
theta = np.linspace(-90, 90, 1000)  # Angle range from 90 to -90 degrees in 1000 steps

# Convert theta to radians
theta_rad = np.deg2rad(theta)

# Compute the complex number s = R * exp(j * theta)
s = R * np.exp(1j * theta_rad)

# Define a transfer function representing an integrator
numerator = [1]  # Coefficients of the numerator polynomial
denominator = [1,2,2]  # Coefficients of the denominator polynomial (for an integrator)
transfer_function=ct.tf(numerator,denominator)
# Define the transfer function H(s)
def transfer_function(s):
    numerator_value = np.polyval(numerator, s)
    denominator_value = np.polyval(denominator, s)
    return numerator_value / denominator_value
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=9, ha='left', va='top',weight='bold', transform=plt.gca().transAxes)
# Compute the frequency response of the transfer function
H = np.array([transfer_function(si) for si in s])

# Plot the Nyquist plot
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=9, ha='left', va='top',weight='bold', transform=plt.gca().transAxes)
plt.plot(H.real, H.imag)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Nyquist Plot: Transfer Function')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axis('equal')  # Equal aspect ratio
plt.show()

