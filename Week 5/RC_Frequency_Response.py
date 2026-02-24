#!/usr/bin/env python

import sys
import math
import numpy as np

def transfer(R, C, f, key):
    """
    Return the magnitude (dB) and phase (degrees) of RC transfer function
    key = "C" -> low-pass
    key = "R" -> high-pass
    """

    w = 2*math.pi*f     #rads

    ZC = 1/(1j*w*C)     #ohms
    ZR = R              #ohms

    if key == "C":
        H = ZC/(ZC + ZR)
    elif key == "R":
        H = ZR/(ZR + ZC)
    else:
        print("Key must be 'R' or 'C'")
        sys.exit()
    
    magnitude = abs(H)
    magnitude_dB = 20*np.log10(magnitude)
    phase_deg = np.angle(H, deg=True)

    return magnitude_dB, phase_deg

def main(argv):
    if len(sys.argv) < 5:
        print("Usage: python RC_Frequency_Response.py <R value in kilohms> <C value in  microfarad> <f in Hz> <Key: R for high-pass filter, C for low-pass filter>")
        return

    R = float(sys.argv[1])*10**3    # Ohms
    C = float(sys.argv[2])*10**-6   # Farads
    f = float(sys.argv[3])          # Hertz
    key = sys.argv[4]   #R or C

    magnitude_dB, phase_deg = transfer(R, C, f, key)

    #Calculate cutoff frequency
    fc = 1/(2*np.pi*R*C)

    print("For a high-pass filter VR/VS" if key == "R" else "For a low-pass filter VC/VS")
    print(f"At {f} Hz:")
    print(f"The magnitude is {magnitude_dB: .3f} dB")
    print(f"The phase is {phase_deg: .3f} degrees")
    print(f"The cutoff frequency is {fc: .3f} Hz")


if __name__ == "__main__":
    main(sys.argv[0:])
#End of file