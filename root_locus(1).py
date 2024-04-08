import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import re

# Function to parse complex numbers from string input
def parse_complex_number(s):
    s = s.strip()
    try:
        if 'j' in s:
            return complex(s.replace('j', ''))
        elif '/' in s:
            parts = s.split('/')
            return float(parts[0]) / float(parts[1])
        elif 'sqrt' in s:
            return np.sqrt(float(re.findall(r'\d+', s)[0]))
        else:
            return float(s)
    except (ValueError, TypeError):
        print("Error: Unable to parse the complex number from input:", s)
        return None

# Function to find poles and zeros of the system
def find_poles_zeros(tf_num, tf_den):
    poles = np.roots(tf_den)
    zeros = np.roots(tf_num)
    print("Step 1: The poles are:", poles)
    print("The zeros are:", zeros)
    return poles, zeros

# Function to find the number of asymptotes
def find_asymptotes(poles, zeros):
    num_asymptotes = len(poles) - len(zeros)  # Exclude poles and zeros at origin
    print("Step 2: The number of asymptotes is:", num_asymptotes, "(number of poles - number of zeros)")
    print("Poles:", len(poles))
    print("Zeros:", len(zeros))
    print("Poles - Zeros:", len(poles) - len(zeros))
    return num_asymptotes

# Function to find the angles of asymptotes
def find_asymptote_angles(poles, zeros):
    q = len(poles) - len(zeros)  # Exclude poles and zeros at origin
    angles = [(2*i + 1) * np.pi / q for i in range(abs(q))]
    angles_degrees = [angle * (180 / np.pi) for angle in angles]
    print("Step 3: The angles of asymptotes are:", angles_degrees, "(angle = (2*i + 1) * π / (number of poles - number of zeros))")
    print("Number of Poles:", len(poles))
    print("Number of Zeros:", len(zeros))
    print("Poles - Zeros:", len(poles) - len(zeros))
    print("\nSubsteps to find the angles:")
    for i, angle in enumerate(angles):
        print(f"Substep {i+1}: Angle {i+1} = (2 * {i+1} + 1) * π / ({len(poles)} - {len(zeros)})")
        print(f"          = {angle} radians")
        print(f"          ≈ {angles_degrees[i]} degrees")
    return angles

# Function to find the centroid of the poles
def find_centroid(poles, zeros):
    centroid = np.sum(poles) / len(poles)  # Include 0 as one of the poles
    print("Step 4: The centroid is: {0} (sum of poles / number of poles)".format(centroid))
    print("Sum of Poles:", np.sum(poles))
    print("Number of Poles:", len(poles))
    print("Centroid Calculation: centroid = sum of poles / number of poles")
    print("                       centroid = {0} / {1}".format(np.sum(poles), len(poles)))
    print("                       centroid =", centroid)
    return centroid

# Function to define the transfer function
def transfer_function(poles, zeros):
    return ctrl.TransferFunction(np.poly(zeros), np.poly(poles))

# Function to plot the root locus on the real axis
def plot_root_locus(poles, zeros, num_asymptotes, angles, centroid):
    if len(poles) == 0 and len(zeros) == 0:
        print("No poles or zeros provided.")
        return

    tf = transfer_function(poles, zeros)
    r, k = ctrl.root_locus(tf, Plot=False)

    plt.plot(r.real, r.imag, '.')

    for i, angle in enumerate(angles):
        x_offset = 10 * np.cos(angle)
        y_offset = 10 * np.sin(angle)
        plt.plot([centroid.real, centroid.real + x_offset], 
                 [0, y_offset], '--', color='blue', lw=0.5)
        # Mark angle text
        plt.text(centroid.real + x_offset, y_offset, f'θ{i+1} ({np.degrees(angle):.2f}°)', color='blue', ha='center')

    # Find breakaway points
    real_parts = np.real(poles)
    derivative = np.polyder(np.poly(real_parts))
    breakaway_points = np.roots(derivative)

    # Print breakaway points
    print("Step 5: Breakaway points:", breakaway_points, "(roots of derivative of real parts of poles)")

    # Plot breakaway points
    plt.plot(breakaway_points.real, np.zeros_like(breakaway_points), 'mo', label='Breakaway Points on Real Axis')

    # Plot roots on the real axis
    roots_real_axis = poles[np.abs(np.imag(poles)) < 1e-6]
    plt.plot(roots_real_axis.real, np.zeros_like(roots_real_axis), '^', color='green', label='Roots on Real Axis')

    # Plot poles and zeros
    plt.plot(poles.real, poles.imag, 'rx', label='Poles')
    plt.plot(zeros.real, zeros.imag, 'bo', label='Zeros')

    # Calculate existing root locus on the real axis
    root_locus_points = []

    # Sort poles and zeros
    poles = np.sort(poles)
    zeros = np.sort(zeros)

    # Start from negative infinity
    total_poles = 0
    total_zeros = 0
    if len(poles) > 0:
        root_locus_points.append(float('-inf'))
    for i in range(len(poles)):
        total_poles += poles[i]
        if i < len(zeros):
            total_zeros += zeros[i]
        if (len(poles) - i + len(zeros) - i) % 2 == 0:
            # Root locus exists between this pair of poles and zeros
            root_locus_points.append((total_poles - total_zeros).real)

    # End at positive infinity
    if len(poles) > 0:
        root_locus_points.append(float('inf'))

    # Plot existing root locus points
    plt.plot(root_locus_points, np.zeros_like(root_locus_points), '-', color='gray', label='Existing Root Locus')

    # Plot lines of intersection without markers
    for i in range(1, len(root_locus_points) - 1):
        plt.plot([root_locus_points[i], root_locus_points[i+1]], [0, 0], '--', color='gray', lw=0.5)

    plt.title('Root Locus Plot on Real Axis')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlim(-10, 10)  # Setting x-axis limit
    plt.ylim(-10, 10)  # Setting y-axis limit
    plt.grid(True)
    plt.legend()

    # Mark centroid
    plt.plot(centroid.real, centroid.imag, 'o', color='orange', label='Centroid')
    plt.text(centroid.real + 0.5, centroid.imag + 0.5, f'Centroid: {centroid.real:.2f}', color='orange', fontsize=10, ha='center')
    
    plt.show()

# User input for poles and zeros
poles_input = input("Enter the poles (comma-separated, e.g., 0,-1,-2,-3): ").strip()
zeros_input = input("Enter the zeros (comma-separated, e.g., 0,-1,-2,-3): ").strip()

# Parse poles and zeros
poles = np.array([parse_complex_number(pole) for pole in poles_input.split(',') if pole.strip() != ''])
zeros = np.array([parse_complex_number(zero) for zero in zeros_input.split(',') if zero.strip() != ''])

# Plot the root locus step by step

# 1. Transfer Function
print("\nStep 1: Transfer Function")
tf = transfer_function(poles, zeros)
print("Transfer function:", tf)

# 2. Number of Asymptotes
print("\nStep 2: Number of Asymptotes")
num_asymptotes = find_asymptotes(poles, zeros)

# 3. Asymptote Angles
print("\nStep 3: Asymptote Angles")
angles = find_asymptote_angles(poles, zeros)

# 4. Centroid Calculation
print("\nStep 4: Centroid Calculation")
centroid = find_centroid(poles, zeros)

# 5. Plot Root Locus
print("\nStep 5: Plotting Root Locus")
plot_root_locus(poles, zeros, num_asymptotes, angles, centroid)