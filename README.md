# Python BEMT Propeller Solver

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Research%20Grade-success)

A high-performance Python implementation of the **Blade Element Momentum Theory (BEMT)** for predicting the aerodynamic and hydrodynamic performance of propellers.

The solver computes:

- Thrust
- Torque
- Power
- Propeller efficiency

The code has been validated against:

- APC propeller performance data (aerial and marine)
- UIUC wind tunnel measurements
- CFD simulations
- QBlade simulations

The results show **excellent agreement with experiments** and **improved accuracy compared to QBlade** for the tested cases.

---

## Features

- Blade Element Momentum Theory (BEMT) solver
- Supports **aerial and marine propellers**
- Automatic **Reynolds number estimation**
- Airfoil **360° polar interpolation**
- Automatic **airfoil selection based on Reynolds number**
- Comparison with **experimental data**
- Efficient root-solving method for inflow angle
- Modular Python architecture

---

## Code Architecture

The solver is divided into three modules.

### `propeller_geometry.py`

Handles:

- Propeller geometry
- Blade discretization
- Propeller radius
- Chord distribution
- Pitch distribution
- Reynolds number estimation
- Freestream conditions

---

### `airfoil_selection.py`

Responsible for:

- Selecting airfoil polar data
- Choosing correct **360° polar files**
- Interpolating aerodynamic coefficients

Selection is based on:
Reynold's Number

---

### `main.py`

Main solver implementing **Blade Element Momentum Theory**.

Calculates:

- thrust
- torque
- power
- propeller efficiency

Uses a **root-finding method** to determine the inflow angle for each blade element.

---

## Validation

The solver has been validated using multiple datasets.

### APC Propeller Data

Comparison against:

- APC aerial propeller performance data
- APC marine propeller performance data

---

### UIUC Wind Tunnel Data

The model predictions were compared against experimental measurements from the **UIUC propeller database**.

Results show **strong agreement in thrust and power curves**.

---

### CFD Validation

The solver has also been compared with **CFD simulation results**, demonstrating good agreement across operating conditions.

---

### QBlade Comparison

The solver was benchmarked against **QBlade simulations**.

For the tested propellers:

- The present implementation shows **better agreement with experimental data**.

---

## Example Output

The solver generates plots for:

- Thrust vs freestream velocity
- Torque vs freestream velocity
- Power vs freestream velocity
- Propeller efficiency vs freestream velocity

Experimental data is overlaid for comparison.

---

## Applications

This code can be used for:

### Aerospace

- UAV propeller performance prediction
- Drone propulsion system design
- Electric aircraft propeller analysis
- Propeller optimization studies

---

### Marine Engineering

- Marine propeller analysis
- Small boat propeller design
- Hydrodynamic propeller performance prediction

---

### Research

- BEMT method development
- Propeller aerodynamic studies
- Validation against experimental datasets
- Rapid propeller performance estimation

---

### Education

The code can be used as a **teaching tool** for:

- Blade Element Momentum Theory
- Propeller aerodynamics
- Numerical methods in aerodynamics

---

## Advantages

Compared to many existing BEMT implementations, this solver provides:

### Modular architecture

Clear separation between:

- geometry
- airfoil selection
- solver

---

### Experimental validation

Validated against:

- APC propeller data
- UIUC wind tunnel experiments
- CFD results

---

### Fast computation

The solver uses a **numerical root solver** instead of brute-force search, significantly improving performance.

---

### Flexible airfoil handling

Supports **360° airfoil polar data** for accurate prediction across wide operating conditions.

---

## Requirements

Install dependencies: pip install numpy scipy matplotlib

---

## Running the Code

Step-by-step implementation:

1. Go to: "./geometry_and_performance_data/geometry.dat"
2. Update the propellor geometry, providing propeller elemental data (radial location, chord and pitch other data is optional) without the field names. Go to: "./APC propeller geometry/4x4E-3-PERF.PE0" for reference. Or use propeller geometries data availabe in "./APC propeller geometry"
3. Update the propeller performance in "./geometry_and_performance_data/Performance.dat", providing freestream velocity data. Go to: "./APC Propeller Performance Data/Aerial propeller data/PER3_4X4E-3.dat" for reference. Or use corresponding propeller perfromance data available in "./APC Propeller Performance Data/Aerial propeller data"
4. Update the airfoil used in the propeller, add the geometry data in "./Airfoil_geometry".
5. Update the airfoil 360 polar data in "./Airfoil_360_polar_data" for various Reynold's number.
6. Update the new airfoil information in "./src/airfoil_selection.py"
7. Run: main.py

To convert the code from aerial to marine, just update the density and kinematic viscosity values in "./src/main.py".

The solver will:

- Load propeller geometry
- Estimate Reynolds number
- Select airfoil polar data
- Compute propeller performance
- Plot results

## Author

Developed as part of research in **propeller aerodynamic and hydrodynamic performance prediction using Blade Element Momentum Theory**.

---

## License

MIT License

---

## Acknowledgements

Data used for validation:

- APC Propeller Performance Data
- UIUC Propeller Database
