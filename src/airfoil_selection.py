import propeller_geometry as pg
import numpy as np

def airfoil_selections(propeller_geometry_path, performance_file_path, nu):
    """Selects the airfoil polar data and returns them for the given Airfoil"""
    Re = pg.renolds_number_finder(propeller_geometry_path, performance_file_path, nu)
    if Re <= 20000:
        Airfoil1 = np.loadtxt("./Airfoil_360_polar_data/CLARK_Y_20k.plr")
        Airfoil2 = np.loadtxt("./Airfoil_360_polar_data/E63_20k.plr")
        Airfoil3 = np.loadtxt("./Airfoil_360_polar_data/NACA_4412_20k.plr")
    elif Re > 20000 and Re <= 35000:
        Airfoil1 = np.loadtxt("./Airfoil_360_polar_data/CLARK_Y_20k.plr")
        Airfoil2 = np.loadtxt("./Airfoil_360_polar_data/E63_20k.plr")
        Airfoil3 = np.loadtxt("./Airfoil_360_polar_data/NACA_4412_20k.plr")
    elif Re > 35000 and Re <= 65000:
        Airfoil1 = np.loadtxt("./Airfoil_360_polar_data/CLARK_Y_50k.plr")
        Airfoil2 = np.loadtxt("./Airfoil_360_polar_data/E63_50k.plr")
        Airfoil3 = np.loadtxt("./Airfoil_360_polar_data/NACA_4412_50k.plr")
    elif Re > 65000 and Re <= 90000:
        Airfoil1 = np.loadtxt("./Airfoil_360_polar_data/CLARK_Y_75k.plr")
        Airfoil2 = np.loadtxt("./Airfoil_360_polar_data/E63_75k.plr")
        Airfoil3 = np.loadtxt("./Airfoil_360_polar_data/NACA_4412_75k.plr")
    elif Re > 90000 and Re <= 115000:
        Airfoil1 = np.loadtxt("./Airfoil_360_polar_data/CLARK_Y_100k.plr")
        Airfoil2 = np.loadtxt("./Airfoil_360_polar_data/E63_100k.plr")
        Airfoil3 = np.loadtxt("./Airfoil_360_polar_data/NACA_4412_100k.plr")
    else:
        Airfoil1 = np.loadtxt("./Airfoil_360_polar_data/CLARK_Y_200k.plr")
        Airfoil2 = np.loadtxt("./Airfoil_360_polar_data/E63_200k.plr")
        Airfoil3 = np.loadtxt("./Airfoil_360_polar_data/NACA_4412_200k.plr")
    
    return (Airfoil1, Airfoil2, Airfoil3)

