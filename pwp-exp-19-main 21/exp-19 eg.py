import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import dlti, dbode

def analyze_z_transfer_function(num, den):
    # Create DISCRETE LTI system
    system = dlti(num, den)

    # Poles and Zeros
    zeros = system.zeros
    poles = system.poles
    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability |z| < 1
    stable = np.all(np.abs(poles) < 1)
    print("Stability:", "Stable" if stable else "Unstable")

    # (Simple causality check)
    causal = len(num) <= len(den)
    print("Causality:", "Causal" if causal else "Non-Causal")

    print("Time Invariance: Time Invariant")

    # Bode plot
    w, mag, phase = dbode(system)

    plt.figure(figsize=(12, 8))

    # Magnitude plot
    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)
    plt.title("Bode Magnitude Plot")
    plt.xlabel("Frequency [rad/sample]")
    plt.ylabel("Magnitude [dB]")
    plt.grid(True)

    # Phase plot
    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)
    plt.title("Bode Phase Plot")
    plt.xlabel("Frequency [rad/sample]")
    plt.ylabel("Phase [degrees]")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Example system H(z) = (z^2 + 0.5) / (z^2 - 1.5z + 0.5)
num = [1, 0.5]
den = [1, -1.5, 0.5]

analyze_z_transfer_function(num, den)
