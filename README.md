# Python BEMT Propeller Solver

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

# Reynold's Number

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

Run:
main.py

The solver will:

1. Load propeller geometry
2. Estimate Reynolds number
3. Select airfoil polar data
4. Compute propeller performance
5. Plot results

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
