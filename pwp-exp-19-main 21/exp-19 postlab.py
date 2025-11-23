# #1.
# import sympy as sp

# def z_transform_unit_step():
#     n = sp.symbols('n')
#     u = sp.Heaviside(n)  # unit step
#     z = sp.symbols('z')

#     U = sp.summation(u * z**(-n), (n, 0, sp.oo))
#     return sp.simplify(U)

# U_z = z_transform_unit_step()
# print("Z-transform of unit step u[n] =", U_z)

#2.
import numpy as np
from scipy.signal import TransferFunction

num = [1]
den = [1, -0.5]  # 1 - 0.5z^-1

system = TransferFunction(num, den)

poles = system.poles
print("Poles:", poles)

if all(abs(p) < 1 for p in poles):
    print("System is Stable")
else:
    print("System is Unstable")
