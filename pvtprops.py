#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 20:31:08 2021

@author: Toghrul Nasirli
"""

import numpy as np

def critical_presssure_Sutton(sg_gas):
    Ppc = 756.8 - 131*sg_gas - 3.6*(sg_gas**2)
    return Ppc

def critical_temperature_Sutton(sg_gas):
    Tpc = 169.2 + 349*sg_gas - 74*(sg_gas**2)
    return Tpc

def carr_kobayashi_temperature(sg_gas, CO2, H2S, N2):
    temperature_corrected = critical_temperature_Sutton(sg_gas) - (80*CO2) + (130*H2S) - (250*N2)
    return temperature_corrected

def carr_kobayashi_pressure(sg_gas, CO2, H2S, N2):
    pressure_corrected = critical_presssure_Sutton(sg_gas) + (440*CO2) + (600*H2S) - (170*N2)
    return pressure_corrected

def wichert_aziz_temperature(sg_gas, CO2, H2S):
    A = CO2 + H2S
    B = H2S
    epsilon = 120*(A**0.9 - A**1.6) + 15*(B**0.5 - B**4)
    tpc_corrected = critical_temperature_Sutton(sg_gas) - epsilon
    return tpc_corrected

def wichert_aziz_pressure(sg_gas, CO2, H2S):
    A = CO2 + H2S
    B = H2S
    epsilon = 120*(A**0.9 - A**1.6) + 15*(B**0.5 - B**4)
    pressure_corrected = (critical_presssure_Sutton(sg_gas)*wichert_aziz_temperature(sg_gas, CO2, H2S))/(critical_temperature_Sutton(sg_gas) + H2S*(1-H2S)*epsilon)
    return pressure_corrected

def redlich_kwong_eos(P, T, sg_gas, CO2, H2S, method, N2):#INSERT T AS FAHRENHEIT
    R = 10.73
    if method == "WichertAziz":
        a = (0.42727*(R**2)*(wichert_aziz_temperature(sg_gas, CO2, H2S)**2.5))/(wichert_aziz_pressure(sg_gas, CO2, H2S))
        b = 0.08664*(R*wichert_aziz_temperature(sg_gas, CO2, H2S))/(wichert_aziz_pressure(sg_gas, CO2, H2S))
    elif method == "CarrKobayashi":
        a = (0.42727*(R**2)*(carr_kobayashi_temperature(sg_gas, CO2, H2S, N2)**2.5))/(carr_kobayashi_pressure(sg_gas, CO2, H2S, N2))
        b = 0.08664*(R*carr_kobayashi_temperature(sg_gas, CO2, H2S, N2))/(carr_kobayashi_pressure(sg_gas, CO2, H2S, N2))
    A = (a*P)/((R**2)*((T+460)**2.5))
    B = (b*P)/(R*(T+460))
    eqn = np.poly1d([1,-1,(A-B-(B**2)), -A*B])
    for i in eqn.roots:
        if np.imag(i) == 0 and i > 0:
            solution = i
    return solution.real


def lee_gonzales_eakin(P,T,sg_gas,CO2,H2S,method, N2):#INSERT T AS FAHRENHEIT
    molecular_weight = sg_gas*29
    density = P*molecular_weight/(redlich_kwong_eos(P,T,sg_gas,CO2,H2S,method,N2)*10.73*(T+460))
    X = 3.5 + (986/(T+460)) + 0.01*molecular_weight
    Y = 2.4 - 0.2*X
    K = (9.4+0.02*molecular_weight)*((T+460)**1.5)*(10**-4)/(209 + 19*molecular_weight + (T+460))
    viscosity = K*np.exp(X*((density/62.4)**Y))
    return viscosity

