#!/usr/bin/env python

# Used to calculate values for a circuit with 3 diode and 3 resistors in series
# Both diode has a forward voltage of 0.7
# All diodes are forward-baised
# Equation:
# Ohm's Law: V=IR
# Power: P=IV


import sys
import math
import numpy as np


def main(argv):
    if len(sys.argv) < 5:
        print("Usage: python Diode_Simulation.py <V value in V> <R1 value in kilohms> <R2 value in kilohms> <R3 value in kilohms>")
        return

    Vs = float(sys.argv[1])                 # Volts
    R1 = float(sys.argv[2])*10**3           # Ohms
    R2 = float(sys.argv[3])*10**3           # Ohms
    R3 = float(sys.argv[4])*10**3           # Ohms

    V_D1 = 0.7        #Volts
    V_D2 = 0.7        #Volts
    V_D3 = 0.7        #VOlts
    
    #Conversion Factor
    base_to_mil = 1000  #base_to_mil


    #Equivalent resistance
    R_tot = R1+R2+R3

    #What is the value of current I [mA]?
    I = (Vs-V_D1-V_D2-V_D3)/R_tot       #A
    I_mA = I*base_to_mil   #mA
    print(f"The value of current I is {I_mA:.3f}mA")
    
    #What is the value of V_R1 [V]?
    V_R1 = R1*I     #V
    print(f"The value of V_R1 is {V_R1:.3f}V")

    #What is the power dissipated through resistor R1 in mW?
    P_R1 = (I**2)*R1    #W
    P_R1_mW = P_R1*base_to_mil  #mW
    print(f"The power dissipated through resistor R1 is {P_R1_mW:.3f}mW")

    #What is the value of V_R2 [V]?
    V_R2 = R2*I     #V
    print(f"The value of V_R2 is {V_R2:.3f}V")

    #What is the power dissipated through resistor R2 in mW?
    P_R2 = (I**2)*R2    #W
    P_R2_mW = P_R2*base_to_mil  #mW
    print(f"The power dissipated through resistor R2 is {P_R2_mW:.3f}mW")

    #What is the value of V_R3 [V]?
    V_R3 = R3*I     #V
    print(f"The value of V_R3 is {V_R3:.3f}V")

    #What is the power dissipated through resistor R3 in mW?
    P_R3 = (I**2)*R3    #W
    P_R3_mW = P_R3*base_to_mil  #mW
    print(f"The power dissipated through resistor R3 is {P_R3_mW:.3f}mW")

    #What is the power dissipated through Diode D1 in mW?
    P_D1 = I*V_D1
    P_D1_mW = P_D1*base_to_mil
    print(f"The power dissipated through Diode D1 is {P_D1_mW:.3f}mW")

    #What is the power dissipated through Diode D2 in mW?
    P_D2 = I*V_D2
    P_D2_mW = P_D2*base_to_mil
    print(f"The power dissipated through Diode D2 is {P_D2_mW:.3f}mW")

    #What is the power dissipated through Diode D3 in mW?
    P_D3 = I*V_D3
    P_D3_mW = P_D3*base_to_mil
    print(f"The power dissipated through Diode D3 is {P_D3_mW:.3f}mW")


if __name__ == "__main__":
    main(sys.argv[0:])
#End of file