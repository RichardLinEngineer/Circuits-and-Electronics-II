#!/usr/bin/env python

# Used to calculate values for a split-branch circuit with diodes in opposite directions, each with a series resistor
# Both diode has a forward voltage of 0.7
# D1 is reverse-biased
# D2 is forward-baised

import sys
import math
import numpy as np


def main(argv):
    if len(sys.argv) < 4:
        print("Usage: python Diode_Analysis.py <V value in V> <R1 value in ohms> <R2 value in ohms>")
        return

    Vs = float(sys.argv[1])             # Volts
    R1 = float(sys.argv[2])             # Ohms
    R2 = float(sys.argv[3])             # Ohms

    V_D1 = 0.7        #Volts
    V_D2 = 0.7        #Volts

    # Currents
    I_1 = 0             #resistor 1 side [Amps]  
    I_2 = (Vs-V_D2)/R2  #resistor 2 side [Amps]

    #Find the voltage across resistor R1 in Volts?
    print("The voltage across resistor R1 is 0V")

    #Find the power dissipated through resistor R1 in Watts?
    print("The power dissipated through resistor R1 is 0W")

    #Find the voltage across resistor R2 in Volts?
    V_R2 = Vs-V_D2
    print(f"The voltage across resistor R2 is {V_R2:.4f}V")

    #Find the power dissipated through resistor R2 in Watts?
    P_R2 = (Vs-V_D2)**2/R2
    print(f"The power dissipated through resistor R2 is {P_R2:.4f}W")

    #Find the power dissipated through diode D2 in Watts?
    P_D2 = I_2*V_D2
    print(f"The power dissipated through diode D2 is {P_D2:.4gf}W")

    #Find the power dissipated through diode D1 in Watts?
    print("The power dissipated through diode D1 is 0W")


if __name__ == "__main__":
    main(sys.argv[0:])
#End of file