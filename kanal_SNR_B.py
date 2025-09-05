# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:51:35 2023

@author: Matevz
"""

## C = B * log2(1+SNR)
from math import log2,log10


def CfromBSNR(B,SNR):
    #najprej pretvori SNR v desetiški sistem 
    SNR = 10**(SNR/10)

    #potem izračzunaš kapaciteto
    C_max = B * log2(1+SNR)

    print(f"V dani situaciji dobiš pri:\nPasovni širini: {B:.3e}\nSNR: {SNR}\nKapaciteto {C_max:6.2f}b/s")
    return C_max


def BfromCSNR(C,SNR):
    #konverzija DB-dec
    SNR = 10**(SNR/10)
    
    B = C / log2(1+SNR)
    print(f"V dani situaciji dobiš pri:\nPasovni širini: {B:.3e}\nSNR: {round(10*log10(SNR))}\nKapaciteto {C:6.2f}b/s")
    return B


def SNRfromCB(C,B,dB=True):
    SNR = 2**(C/B)-1
    print(f"V dani situaciji dobiš pri:\nPasovni širini: {B:.3e}\nSNR: {round(10*log10(SNR))}\nKapaciteto {C:6.2f}b/s")
    if dB:
        return round(10*log10(SNR))
    else:
        return SNR


B1 = 15e6 #kHz
SNR1 = 60 #dB
C1 = 44236800


def calculate_missing_variable(B=None, SNR=None, C=None):
    # Check the number of missing variables
    num_missing_variables = sum(1 for var in (B, SNR, C) if var is None)

    if num_missing_variables != 1:
        raise ValueError("Exactly one variable (B, SNR, or C) must be missing.")

    if C is None:
        # Calculate C when B and SNR are given
        C = B * log2(1 + 10**(SNR/10))
    elif B is None:
        # Calculate B when C and SNR are given
        B = C / log2(1+10**(SNR/10))
    elif SNR is None:
        # Calculate SNR when B and C are given
        SNR = round(10*log10(2**(C/B)-1))
    
    return {"B": B, "SNR": SNR, "C": C}

# Primer uporabe:
#result = calculate_missing_variable(B=2, SNR=None, C=3)
#print(result)

C1 = 1920*1080*32*90
B1 = 90e6

#CfromBSNR(B1,SNR1)
#print(calculate_missing_variable(B=B1,SNR=SNR1,C=None))

#BfromCSNR(C1,30)
#print(calculate_missing_variable(B=None,SNR=SNR1,C=C1))

print(SNRfromCB(C1,B1,False))
#C_m = CfromBSNR(B1,20)
#print(C1/C_m)
B_m = BfromCSNR(C1,30)
print(B_m/B1)
#print(calculate_missing_variable(B=B1,SNR=,C=None))