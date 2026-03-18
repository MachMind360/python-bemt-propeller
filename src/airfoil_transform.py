import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def airfoil_transform(airfoil: str ,chord: float, aoa: float, thickness_ratio: float, z_translate: float, visualisation: bool, save_csv: bool):
    """Returns x and y coordinates of the airfoil after specified transformation that is:
    1. Dilation
    2. Rotation
    3. Thickness
    4. Translation
    \n Inputs:
    1. airfoil: airfoil (x,y) coordinates path
    2. chord: chord length
    3. aoa: angle of attack
    4. thickness ratio: required thickness ratio
    5. plot results: True/False
    6. save_results: True/False"""

    airfoil_path = np.loadtxt(airfoil)
    original_thickness_ratio = np.max(airfoil_path[:, 1])

    thickness_scaling_factor = thickness_ratio/original_thickness_ratio
    airfoil_x = airfoil_path[:, 0]
    airfoil_y = airfoil_path[:, 1]*thickness_scaling_factor

    move_x = 1 - chord
    move_y = 0

    radius = chord - airfoil_x*chord
    h = np.sqrt(radius**2 + (airfoil_y*chord)**2)

    alpha = np.arctan2(chord*airfoil_y, radius)
    x_transform = chord - h*np.cos(aoa*np.pi/180 + alpha) + move_x
    y_transform = h*np.sin(aoa*np.pi/180 + alpha) + move_y

    transformed_data = {
        "X": x_transform,
        "Y": y_transform
    }

    transformed_data["Z"] = z_translate

    if visualisation:
        plt.plot(airfoil_path[:, 0], airfoil_path[:, 1], "r")
        plt.plot(x_transform, y_transform, "k")
        plt.axis('equal')
        plt.legend(['Original', 'Transformed'])
        plt.grid(True)
        plt.show()

    if save_csv:
        df = pd.DataFrame(transformed_data)
        df.to_csv(f"Tranformed_c{chord}_aoa{aoa}_tr{thickness_ratio}_zt{z_translate}_airfoil.csv", index=False)

    return transformed_data
    


