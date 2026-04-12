#!/usr/bin/env python

# Used to determine the status of 2 NMOS transistor (Cutoff, Saturation, Triode)
# Calculate resistor and width of transistor
# Equation:
# Ohm's Law: V=IR

# Triode Region
# I_D = k'_n (W/L)((V_GS-V_in)V_DS - 1/2*V_DS^2)

#Saturation Region
# I_D = 1/2*k'_n (W/L)(V_GS - Vt)^2

import sys
import numpy as np
import math

def NMOS_status(V_GS, V_DS, V_th):
    V_OV = V_GS - V_th
    if V_GS < V_th:
        region = 1      #cutoff
    if V_DS >= V_OV:
        region = 2      #saturation
    else:
        region = 3      #triode
    return region, V_OV

def find_width(I_D, μ_nC_ox, L, V_OV, region, V_DS=1):
    if region == 2:  #saturation
        return (2*I_D*L)/(μ_nC_ox*V_OV**2)
    elif region == 3: #triode
        return (I_D*L)/(μ_nC_ox * (V_OV - V_DS * 0.5) * V_DS)
    else:
        print("Error: region must be triode or saturation to solve for width")
        exit(1)



def main(argv):
    if len(argv) < 2:
        print("Usage:")
        print("Mode 1: python NMOS.py 1 <V_d2 in V>")
        print("Mode 2: python NMOS.py 2 <V_th in V> <μ_nC_ox in μA/V^2> <L in μm>")
        return
    
    mode = int(argv[1])

    V_S = 1.8    # volts
    I_D = 0.0001 # amp

    V_G2 = 1.4   # volts
    V_G1 = 0.6   # volts

    V_S2 = V_G1  # volts
    V_S1 = 0     # volts

    V_D2 = V_G2  # volts
    V_D1 = V_G1  # volts

    if mode == 1:
        if len(argv) < 3:
            print("Mode 1 requires: V_d2")
            exit(1)
        #Calculate the value of R in kΩ?
        V_d2 = float(argv[2])
        R_ohms = (V_S - V_d2)/I_D
        R_kilohms = R_ohms/1000
        print(f"The resistor value is {R_kilohms:.2f} kΩ")

    elif mode == 2:
        if len(argv) < 5:
            print("Mode 2 requires: V_th μ_nC_ox L")
            exit(1)
        V_th = float(argv[2])           #volts
        μ_nC_ox = float(argv[3])*10**-6  #A/V^2
        L = float(argv[4])*10**-6       #m

        #What region should transistor Q2 be operating? Cutoff(1), Saturation (2), and triode (3)
        V_GS2 = V_G2 - V_S2
        V_DS2 = V_D2 - V_S2
        region2, V_OV2 = NMOS_status(V_GS2, V_DS2, V_th)
        print (f"The region of transistor Q2 is {region2}")

        #What region should transistor Q1 be operating? Cutoff(1), Saturation (2), and triode (3)
        V_GS1 = V_G1 - V_S1
        V_DS1 = V_D1 - V_S1
        region1, V_OV1 = NMOS_status(V_GS1, V_DS1, V_th)
        print (f"The region of transistor Q1 is {region1}")
        
        #What is the width of the transistor Q2 in μm?
        W2_m = find_width(I_D, μ_nC_ox, L, V_OV2, region2)
        W2_μm = W2_m*10**6
        print(f"The width of the transistor Q2 is {W2_μm:.2f} μm")

        #What is the width of the transistor Q1 in μm?
        W1_m = find_width(I_D, μ_nC_ox, L, V_OV1, region1, V_DS1)
        W1_μm = W1_m*10**6
        print(f"The width of the transistor Q1 is {W1_μm:.2f} μm")
        
    else:
        print("Invalid mode. Use 1 or 2")
        exit(1)

if __name__ == "__main__":
    main(sys.argv)
#End of file