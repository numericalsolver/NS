num_encirclements = 0

# Loop through the contour points and check for encirclements
for i in range(len(real_part) - 1):
    # Check if the contour crosses the critical point (-1, 0)
    if real_part[i] < -1 < real_part[i + 1]:
        # Check if the imaginary part changes sign from negative to positive
        if imag_part[i] < 0 and imag_part[i + 1] > 0:
            num_encirclements += 1

print("Number of encirclements:", num_encirclements)