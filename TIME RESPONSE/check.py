import sympy as sp

# Define symbols
s = sp.symbols('s')

# Function to calculate Laplace transform
def laplace_transform(f):
    return sp.laplace_transform(f, t, s)

# Function to calculate inverse Laplace transform
def inverse_laplace_transform(F):
    return sp.inverse_laplace_transform(F, s, t)

# Coefficients of numerator and denominator of R(s)
num_R = list(map(float, input("Enter coefficients of numerator of R(s) separated by space: ").split()))
den_R = list(map(float, input("Enter coefficients of denominator of R(s) separated by space: ").split()))

# Constructing transfer function R(s)
R_s = sp.Poly(num_R, sp.Symbol('s')) / sp.Poly(den_R, sp.Symbol('s'))

# Coefficients of numerator and denominator of G(s)
num_G = list(map(float, input("Enter coefficients of numerator of G(s) separated by space: ").split()))
den_G = list(map(float, input("Enter coefficients of denominator of G(s) separated by space: ").split()))

# Constructing transfer function G(s)
G_s = sp.Poly(num_G, sp.Symbol('s')) / sp.Poly(den_G, sp.Symbol('s'))

# Coefficients of numerator and denominator of H(s)
num_H = list(map(float, input("Enter coefficients of numerator of H(s) separated by space: ").split()))
den_H = list(map(float, input("Enter coefficients of denominator of H(s) separated by space: ").split()))

# Constructing transfer function H(s)
H_s = sp.Poly(num_H, sp.Symbol('s')) / sp.Poly(den_H, sp.Symbol('s'))


# Calculate C(s)
C_s = G_s / (1 + G_s * H_s) * R_s

# Calculate c(t) by taking inverse Laplace transform
c_t = inverse_laplace_transform(C_s)

# Display c(t)
print("c(t) =", c_t)

# Calculate undamped natural frequency and damping ratio
omega_n = sp.sqrt(num_G[-1] / den_G[-1])
zeta = den_G[-2] / (2 * omega_n)

print("Undamped natural frequency (omega_n):", omega_n)
print("Damping ratio (zeta):", zeta)
