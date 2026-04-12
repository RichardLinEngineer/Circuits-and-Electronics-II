#!/usr/bin/env python

# Used to determine the status of PMOS transistor (Cutoff, Saturation, Triode)
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

def NMOS_status(V_SG, V_SD, V_th):
    V_OV = V_SG - V_th
    if V_SG < V_th:
        region = 1      #cutoff
    if V_SD >= abs(V_OV):
        region = 2      #saturation
    else:
        region = 3      #triode
    return region, V_OV

def find_width(I_D, μ_nC_ox, L, V_OV, region, V_SD=1):
    if region == 2:  #saturation
        return (2*I_D*L)/(μ_nC_ox*V_OV**2)
    elif region == 3: #triode
        return (I_D*L)/(μ_nC_ox * (V_OV - V_SD * 0.5) * V_SD)
    else:
        print("Error: region must be triode or saturation to solve for width")
        exit(1)

def main(argv):
    if len(argv) < 5:
        print("Usage: python PMOS.py 2 <V_th in V> <μ_nC_ox in μA/V^2> <L in μm> <I_D in μA> <V_D in V>")
        return
    
    V_DD = 1.8    #volts

    V_th = abs(float(argv[1]))          #volts
    μ_nC_ox = float(argv[2])*10**-6     #A/V^2
    L = float(argv[3])*10**-6           #m
    I_D = float(argv[4])*10**-6         #A
    V_D = float(argv[5])                #volts

    V_G = V_D   #volts
    V_S = V_DD   #volts

    #What region should transistor be operating? Cutoff(1), Saturation (2), and triode (3)
    V_SG = V_S - V_G
    V_SD = V_S - V_D
    region, V_OV = NMOS_status(V_SG, V_SD, V_th)
    print (f"The region of transistor is {region}")
   
    #Calculate the value of R in kΩ?
    R_ohms = V_D/I_D
    R_kilohms = R_ohms/1000
    print(f"The resistor value is {R_kilohms:.2f} kΩ")
    
    #What is the width of the transistor (W) in μm and 4 decimal places?
    W_m = find_width(I_D, μ_nC_ox, L, V_OV, region, V_SD)
    W_μm = W_m*10**6
    print(f"The width of the transistor is {W_μm:.4f} μm")

if __name__ == "__main__":
    main(sys.argv)
#End of file