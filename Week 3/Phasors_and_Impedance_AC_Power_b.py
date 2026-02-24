#!/usr/bin/env python

# Used to calculate values for an RLC circuit with all components in series and set frequency

import sys
import math
import numpy as np


def main(argv):
    if len(sys.argv) < 5:
        print("Usage: python Phasors_and_Impedance_AC_Power_b.py <V_m value in V> <R value in ohms> <C value in  microfarad> <L in millihenry>")
        return
    
    Vm = int(sys.argv[1])           # Volts
    R = int(sys.argv[2])            # Ohms
    C = float(sys.argv[3])*10**-6   # Farads
    L = float(sys.argv[4])*10**-3   # Henries

    f = 100 # Hz
    w = 2*math.pi*f # Radians

    ZC = 1/(1j*w*C)
    ZL = 1j*w*L
    ZR = R

    #Calculate rms voltage [V]
    Vrms = Vm/math.sqrt(2)  #Volts
    print(f"The rms voltage of the voltage source is {Vrms:.3f} [V]")

    #Calculate Real Impedance [ohms]
    Zab = ZR + ZC + ZL      #Ohms
    print(f"The Real Impedance is {Zab.real:.3f} [ohms]")

    #Calculate Imaginary Impedance [ohms]
    print(f"The Imaginary Impedance is {Zab.imag:.3f} [ohms]")
    
    #Calculate amplitude of Time Domain current i(t) [mA]
    I_t = Vm/Zab    # Amps
    I_mag = abs(I_t)
    print(f"The amplitude of Time Domain current i(t) is {I_mag*1000:.3f} [mA]")

    #Calculate rms Current i(t) [mA]
    Irms = I_mag/math.sqrt(2) # Amps
    print(f"The rms value of current i(t) is {Irms*1000:.3f} [mA]")

    #Calculate average power of the Zab (using passive sign convention) [mW]
    P_Used =(Irms ** 2) * R # Watts
    print(f"The average power consumed is {P_Used*1000:.3f} [mW]")

    #Calculate average power of the Zab (using passive sign convention) [mW    
    P_Source = -P_Used  #Watts
    print(f"The average power supplied is {P_Source*1000:.3f} [mW]")


if __name__ == "__main__":
    main(sys.argv[0:])
# End of file