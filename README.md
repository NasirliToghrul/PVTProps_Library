# PVTProps Analysis

This Python script is designed to provide various PVT (Pressure-Volume-Temperature) properties and calculations relevant to hydrocarbon gases. It includes functions to compute critical properties, corrected critical properties, and viscosity using different methods such as Sutton, Carr-Kobayashi, Wichert-Aziz, and Lee-Gonzales-Eakin. These properties and calculations are essential in the analysis and modeling of gas reservoirs and their behavior under different conditions.

## Functions Provided

### 1. Critical Properties Calculation

- `critical_pressure_Sutton(sg_gas)`: Calculates the critical pressure of a gas using Sutton's correlation.
- `critical_temperature_Sutton(sg_gas)`: Calculates the critical temperature of a gas using Sutton's correlation.

### 2. Corrected Critical Properties Calculation

- `carr_kobayashi_temperature(sg_gas, CO2, H2S, N2)`: Calculates the corrected critical temperature of a gas mixture using the Carr-Kobayashi method.
- `carr_kobayashi_pressure(sg_gas, CO2, H2S, N2)`: Calculates the corrected critical pressure of a gas mixture using the Carr-Kobayashi method.
- `wichert_aziz_temperature(sg_gas, CO2, H2S)`: Calculates the corrected critical temperature of a gas mixture using the Wichert-Aziz method.
- `wichert_aziz_pressure(sg_gas, CO2, H2S)`: Calculates the corrected critical pressure of a gas mixture using the Wichert-Aziz method.

### 3. Equations of State

- `redlich_kwong_eos(P, T, sg_gas, CO2, H2S, method, N2)`: Computes the gas volume using the Redlich-Kwong equation of state.
- `lee_gonzales_eakin(P,T,sg_gas,CO2,H2S,method, N2)`: Calculates the viscosity of a gas using the Lee-Gonzales-Eakin correlation.

## Usage

The script can be imported into other Python programs or used interactively for PVT analysis. Below is an example of how to use the functions:

```python
import pvtprops_analysis

# Example usage of critical properties calculation
sg_gas = 0.7
Ppc = pvtprops_analysis.critical_pressure_Sutton(sg_gas)
Tpc = pvtprops_analysis.critical_temperature_Sutton(sg_gas)
print("Critical Pressure:", Ppc)
print("Critical Temperature:", Tpc)

# Example usage of corrected critical properties calculation
CO2 = 0.05
H2S = 0.03
N2 = 0.02
T_corrected = pvtprops_analysis.carr_kobayashi_temperature(sg_gas, CO2, H2S, N2)
P_corrected = pvtprops_analysis.carr_kobayashi_pressure(sg_gas, CO2, H2S, N2)
print("Corrected Critical Pressure:", P_corrected)
print("Corrected Critical Temperature:", T_corrected)

# Example usage of Redlich-Kwong equation of state
P = 2000 # Pressure in psia
T = 150 # Temperature in Fahrenheit
method = "WichertAziz"
V = pvtprops_analysis.redlich_kwong_eos(P, T, sg_gas, CO2, H2S, method, N2)
print("Gas Volume (Redlich-Kwong EOS):", V)

# Example usage of Lee-Gonzales-Eakin viscosity calculation
viscosity = pvtprops_analysis.Lee_Gonzales_Eakin(P, T, sg_gas, CO2, H2S, method, N2)
print("Viscosity (Lee-Gonzales-Eakin):", viscosity)
```

## Note

- Make sure to provide correct inputs (mole fractions of CO2, H2S, and N2) for accurate calculations.
- Ensure that temperature is provided in Fahrenheit for temperature-dependent calculations.

This script can be utilized in various applications related to petroleum engineering, reservoir simulation, and gas production analysis.

## Credits

- This script was developed by Toghrul Nasirli.
---
