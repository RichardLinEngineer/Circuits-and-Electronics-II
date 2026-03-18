#!/usr/bin/env python

# Used to calculate values for a half-wave rectifier circuit
# The diodes is forward-baised
# Equation:
# Ohm's Law: V=IR
# Power: P=IV


import sys
import math
import numpy as np


def main(argv):
    if len(sys.argv) < 4:
        print("Usage: python Diode_Simulation.py <Vs value in V> <RL value in kilohms> <VF value in V>")
        return

    Vs = float(sys.argv[1])                 # AC Source [Volts]
    RL = float(sys.argv[2])*10**3           # Ohms
    VF = float(sys.argv[3])                 # LED Forward Voltage [V]
    

    #Conversion Factor
    base_to_mil = 1000  #base_to_mil

    #Calculate the peak output voltage V_out [V]?
    V_out = Vs-VF   #V
    print(f"The peak output voltage V_out is {V_out:.4f}V")

    #Calculate the peak output current I_out [mA]?
    I_out = V_out/RL      #A
    I_out_mA = I_out*base_to_mil        #mA
    print(f"The peak output current I_out is {I_out_mA:.4f}mA")


if __name__ == "__main__":
    main(sys.argv[0:])
#End of file