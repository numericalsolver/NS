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

plt.xlabel('Real axis',fontsize=14)
plt.ylabel('Imaginary axis',fontsize=14)
plt.title('NYQUIST PLOT',fontsize=16)
plt.axhline(0, color='black',linewidth=2)
plt.axvline(0, color='black',linewidth=2)

def random_color():
   return (random.random(), random.random(), random.random())

contour=ct.nyquist_plot(transfer_function,return_contour=True ,color=random_color(),arrows =2 ,arrow_size=20,start_marker='o',start_marker_size=10,linewidth=4)
for arrow in plt.gca().findobj(patches.FancyArrowPatch):
    color ="black"
    arrow.set_color(color)
    arrow.set_zorder(30)
   
plt.text(0.95, 0.95, r'$0 < \omega < \infty$', fontsize=12, ha='right', va='top',weight='bold', transform=plt.gca().transAxes)
plt.text(0.95, 0.9, r'$-\infty < \omega < 0$', fontsize=12, ha='right', va='top',weight='bold', transform=plt.gca().transAxes)
plt.text(0.05, 0.95, f'Transfer Function: {transfer_function}', fontsize=12, ha='left', va='top',weight='bold', transform=plt.gca().transAxes)


plt.plot(-1, 0, marker='o', markersize=8, color='blue')
plt.text(-1, 0, '(-1, 0)', fontsize=10, ha='left', va='bottom')

omega = np.logspace(-2, 2, 10)
frequency_response = ct.freqresp(transfer_function, omega)
print("Frequency Response:")
print(frequency_response)
contour = frequency_response[1]  
def count_encirclements(contour):
      num_encirclements = 0
      threshold = -1  # Define the threshold for encirclement
      crossed_threshold = False
      for i in range(len(contour) - 1):
          if contour[i].real < threshold and contour[i + 1].real > threshold:
              num_encirclements += 1
              crossed_threshold = True  # Mark as having crossed the threshold
          elif contour[i].real > threshold and contour[i + 1].real < threshold:
              num_encirclements -= 1
              crossed_threshold = True
      
      # Check for encirclement if the contour ends on or left of the threshold
      if crossed_threshold and contour[-1].real <= threshold:
          num_encirclements += 1

      return num_encirclements

# Call the function to count encirclements
num_encirclements = count_encirclements(contour)
plt.text(
    0.5,  # x-coordinate (center alignment)
    0.01,  # y-coordinate (slightly above bottom)
    f"Number of encirclements: {num_encirclements}",
    ha='center',  # horizontal alignment
    va='bottom',  # vertical alignment
    fontsize=10,  # adjust font size as needed
    bbox=dict(facecolor='white', alpha=0.7)  # optional white background
)

w = np.logspace(-1, 3, 10)

# Compute magnitude and phase for each point in the contour
mag = np.abs(transfer_function(1j * w))
phase = np.angle(transfer_function(1j * w), deg=True)

# Calculate the magnitude and phase for s = j*w
mag_jw = np.abs(transfer_function(1j * w[-1]))
phase_jw = np.angle(transfer_function(1j * w[-1]), deg=True)

# Calculate the magnitude and phase for s = Re^j*teta
teta = np.linspace(np.pi/2, -np.pi/2, 2)
R = 10
w = R * np.exp(1j * teta)
mag_re_jteta = np.abs(transfer_function(1j * w))
phase_re_jteta = np.angle(transfer_function(1j * w), deg=True)
# Calculate the magnitude and phase for s = -j*w
mag_minus_jw = np.abs(transfer_function(-1j * w[-1]))
phase_minus_jw = np.angle(transfer_function(-1j * w[-1]), deg=True)

# Calculate the magnitude and phase for s = re^j*teta
teta = np.linspace(-np.pi/2, np.pi/2, 2)
r = 0
w = r * np.exp(1j * teta)
mag_r_ej_teta = np.abs(transfer_function(1j * w))
phase_r_ej_teta = np.angle(transfer_function(1j * w), deg=True)


# Position table slightly above the bottom with margins
table_y = -0.5  # Adjust as needed
table_x = -1.05 # Adjust as needed
data = []
if num_encirclements != 0:
  # Include "s = re^j*teta" row only if encirclements exist
  data.append(["s = Re^j*teta", f"{mag_re_jteta[0]:.2f}", f"{phase_re_jteta[0]:.2f}"])

# Add remaining data entries (always included)
data.extend([
  ["s = j*w", f"{mag_jw:.2f}", f"{phase_jw:.2f}"],
  ["s = Re^j*teta", f"{mag_re_jteta[0]:.2f}", f"{phase_re_jteta[0]:.2f}"],
  ["s = -j*w", f"{mag_minus_jw:.2f}", f"{phase_minus_jw:.2f}"],
])

       

# Add the tabular column at the bottom
plt.text(
    table_x, table_y,
    tabulate( data,headers=["s", "Magnitude", "Phase"], tablefmt="grid"),
    fontsize=8, ha='left', va='center', bbox=dict(facecolor='white', alpha=0.7),fontweight='bold'
)
stability_margins = ct.stability_margins(transfer_function)
gm = stability_margins[0]
pm = stability_margins[1]


# Position text for stability status
status_text_x = 0.6  # Adjust as needed (x-coordinate)
status_text_y = 0.8  # Adjust as needed (y-coordinate)

# Determine and display system stability using plt.text
if gm > 1 and pm > 0:
  stability_text = "SYSTEM IS STABLE"
  
else:
  stability_text = "SYSTEM IS UNSTABLE"
 

# Add system stability status text
plt.text(
    status_text_x, status_text_y, stability_text,
    ha='left', va='top', fontsize=12, weight='bold', bbox=dict(facecolor='white', alpha=0.7)
)
plt.show()