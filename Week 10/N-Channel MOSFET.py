#!/usr/bin/env python

# Used to determine if a N-Channel MOSFET is ON or OFF
# Calculate the current flow 
# Equation:
# Ohm's Law: V=IR


import sys
import math
import numpy as np

def MOSFET_status(V_GS, V_th):
    return V_GS >= V_th


def main(argv):
    if len(sys.argv) < 5:
        print("Usage: python N -Channel MOSFET.py <V_DD value in V> <V_GS value in V> <V_th value in V> <R value in ohms>")
        return

    V_DD = float(argv[1])
    V_GS = float(argv[2])
    V_th = float(argv[3])
    R = float(argv[4])

    #Conversion Factor
    base_to_mil = 1000  # base_to_mil (multiply by 1000)

    #Is the N-channel MOSFET ON or OFF? In your answer use 1 for ON and 0 for OFF.
    if MOSFET_status(V_GS, V_th):
        print("MOSFET is On (1)")
        I_D = V_DD/R
    else:
        print("MOSFET is Off (0)")
        I_D = 0
    

    #Calculate the I_D in mA. Use two decimal points in your answer.
    I_D_mA = I_D * base_to_mil
    print(f"The current that flows through the MOSFET is {I_D_mA:.2f} mA")
    

if __name__ == "__main__":
    main(sys.argv)

#End of file