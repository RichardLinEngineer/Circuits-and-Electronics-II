#!/usr/bin/env python

import sys
import math
import numpy as np

def transfer(R, L, f, key):
    """
    Return the magnitude (dB) and phase (degrees) of RL transfer function
    key = "R" -> low-pass
    key = "L" -> high-pass
    """

    w = 2*math.pi*f     #rads

    ZL = 1j*w*L         #ohms
    ZR = R              #ohms

    if key == "R":
        H = ZR/(ZR + ZL)
    elif key == "L":
        H = ZL/(ZR + ZL)
    else:
        print("Key must be 'R' or 'L'")
        sys.exit()
    
    magnitude = abs(H)
    magnitude_dB = 20*np.log10(magnitude)
    phase_deg = np.angle(H, deg=True)

    return magnitude_dB, phase_deg

def main(argv):
    if len(sys.argv) < 5:
        print("Usage: python RC_Frequency_Response.py <R value in kilohms> <L value in  millihenry> <f in Hz> <Key: L for high-pass filter, R for low-pass filter>")
        return

    R = float(sys.argv[1])*10**3    # Ohms
    L = float(sys.argv[2])*10**-3   # Henry
    f = float(sys.argv[3])          # Hertz
    key = sys.argv[4].upper()   #R or L

    magnitude_dB, phase_deg = transfer(R, L, f, key)

    #Converstion Factor
    Hz_to_kHz = 1000 #Hz_to_kHz

    #Calculate cutoff frequency
    fc = R/(2*np.pi*L*Hz_to_kHz)  #[kHz]

    print("Filter type: High-pass (V_L/V_S)" if key == "L" else "Filter type: Low-pass (V_R/V_S)")
    print(f"At {f} Hz:")
    print(f"The magnitude is {magnitude_dB: .3f} dB")
    print(f"The phase is {phase_deg: .3f} degrees")
    print(f"The cutoff frequency is {fc: .3f} kHz")


if __name__ == "__main__":
    main(sys.argv[0:])
#End of file