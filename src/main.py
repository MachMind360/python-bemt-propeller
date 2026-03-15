import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import brenth, minimize_scalar
from airfoil_selection import airfoil_selections
from propeller_geometry import freestream_data, propeller_geometry_creation
import matplotlib.pyplot as plt

####################### Constants ############################
N = 6000 #Propeller RPM
omega = 2*np.pi*(N/60) #Propeller angular velocity
rho = 1.225 #1.225 density of air #997 density of water
nu = 15.7*10**(-6) #kinamatic viscosity
B = 2 #Number of blades
transition = 4.76 #Satation where the airfoil transitions

freestream_data_path = "./geometry_and_performance_data/Performance.dat"
geometry_path = "./geometry_and_performance_data/geometry.dat"
##############################################################

vinf = freestream_data(freestream_data_path)
geom = propeller_geometry_creation(geometry_path, B)
airfoils = airfoil_selections(geometry_path, freestream_data_path, nu)

total_thrust = np.zeros(len(vinf["vinf"]))
total_torque = np.zeros(len(vinf["vinf"]))
total_power = np.zeros(len(vinf["vinf"]))
efficiency = np.zeros(len(vinf["vinf"]))

for k in range(len(vinf["vinf"])):
    elemental_thrust = np.zeros(len(geom["r"]))
    elemental_torque = np.zeros(len(geom["r"]))
    for i in range(len(geom["r"])):
        r = geom["r"][i]
        solidity = geom["solidity"][i]
        pitch = geom["prop_pitch"][i]

        if transition == 0:
            cl_interp = interp1d(airfoils[0][:, 0]*(np.pi/180), airfoils[0][:, 1], kind='linear', fill_value="extrapolate")
            cd_interp = interp1d(airfoils[0][:, 0]*(np.pi/180), airfoils[0][:, 2], kind='linear', fill_value="extrapolate")
        
        elif r <= transition/39.37:
            cl_interp = interp1d(airfoils[1][:, 0]*(np.pi/180), airfoils[1][:, 1], kind='linear', fill_value="extrapolate")
            cd_interp = interp1d(airfoils[1][:, 0]*(np.pi/180), airfoils[1][:, 2], kind='linear', fill_value="extrapolate")

        else:
            cl_interp = interp1d(airfoils[2][:, 0]*(np.pi/180), airfoils[2][:, 1], kind='linear', fill_value="extrapolate")
            cd_interp = interp1d(airfoils[2][:, 0]*(np.pi/180), airfoils[2][:, 2], kind='linear', fill_value="extrapolate")
        
        def residual(phi):

            alpha = pitch - phi

            # For Aerial case
            cl = cl_interp(alpha)
            cd = cd_interp(alpha)

            Cn = cl*np.cos(phi) - cd*np.sin(phi)   # coefficient of normal force
            Ct = cl*np.sin(phi) + cd*np.cos(phi)   # coefficient of tangential force

            f = (B/2) * ((geom["rtip"] - r) / (r * abs(np.sin(phi))))
            F_1 = (2/np.pi) * np.arccos(np.exp(-f))      # Prandtl tip loss correction factor

            f_2 = (B/2) * ((r + geom["rhub"]) / (geom["rhub"] * abs(np.sin(phi))))
            F_2 = (2/np.pi) * np.arccos(np.exp(-f_2))    # Prandtl root loss correction factor

            F = F_1 * F_2

            a = (4 * F * (np.sin(phi)**2) / (solidity * Cn) - 1) ** (-1)
            b = (4 * F * np.sin(phi) * np.cos(phi) / (solidity * Ct) + 1) ** (-1)

            return (np.sin(phi)/(1 + a) - (vinf["vinf"][k] * np.cos(phi)) / (omega * r * (1 - b)))


        try:
            phi = brenth(residual, a=0.1*(np.pi/180), b=geom["prop_pitch"][0])
        except ValueError:
            res = minimize_scalar(lambda x: abs(residual(x)), bounds=(0.1*(np.pi/180),geom["prop_pitch"][0]), method='bounded')
            phi = res.x

        alpha = pitch - phi
        cl = cl_interp(alpha)
        cd = cd_interp(alpha)

        Cn = cl*np.cos(phi) - cd*np.sin(phi)
        Ct = cl*np.sin(phi) + cd*np.cos(phi)

        f = (B/2) * ((geom["rtip"] - r) / (r * abs(np.sin(phi))))
        F_1 = (2/np.pi) * np.arccos(np.exp(-f))

        f_2 = (B/2) * ((r + geom["rhub"]) / (geom["rhub"] * abs(np.sin(phi))))
        F_2 = (2/np.pi) * np.arccos(np.exp(-f_2))    # Prandtl root loss correction factor

        F = F_1 * F_2

        a = (4 * F * (np.sin(phi)**2) / (solidity * Cn) - 1) ** (-1) #Axial induction factor 
        b = (4 * F * np.sin(phi) * np.cos(phi) / (solidity * Ct) + 1) ** (-1) #Tangential induction factor
        
        w = (vinf["vinf"][k]*(1+a))**2 + (omega*geom["r"][i]*(1-b))**2
        thrust = B*0.5*rho*Cn*w*geom["chord"][i]*geom["division"]
        elemental_thrust[i] = thrust
        torque = B*Ct*0.5*rho*geom["r"][i]*w*geom["chord"][i]*geom["division"]
        elemental_torque[i] = torque
    
    total_thrust[k] = sum(elemental_thrust)
    total_torque[k] = sum(elemental_torque)
    power = 2*np.pi*N*total_torque[k]/60
    total_power[k] = power
    eff = total_thrust[k]*vinf["vinf"][k]/total_power[k]
    efficiency[k] = eff

plt.figure(figsize=(10,8))
plt.title(f"Propeller performance at {N}RPM")

plt.subplot(2,2,1)
plt.plot(vinf["vinf"], total_thrust, linewidth=2)
plt.plot(vinf["vinf"], vinf["thrust"], "k*")
plt.grid()
plt.xlabel("Freestream velocity (m/s)")
plt.ylabel("Thrust (N)")
plt.legend(["Model Three", "APC data"])

plt.subplot(2,2,2)
plt.plot(vinf["vinf"], total_torque, linewidth=2)
plt.plot(vinf["vinf"], vinf["torque"], "k*")
plt.grid()
plt.xlabel("Freestream velocity (m/s)")
plt.ylabel("Torque (Nm)")
plt.legend(["Model Three", "APC data"])

plt.subplot(2,2,3)
plt.plot(vinf["vinf"], total_power, linewidth=2)
plt.plot(vinf["vinf"], vinf["power"], "k*")
plt.grid()
plt.xlabel("Freestream velocity (m/s)")
plt.ylabel("Power (W)")
plt.legend(["Model Three", "APC data"])

plt.subplot(2,2,4)
plt.plot(vinf["vinf"], efficiency, linewidth=2)
plt.plot(vinf["vinf"], vinf["eff"], "k*")
plt.grid()
plt.xlabel("Freestream velocity (m/s)")
plt.ylabel("Efficiency")
plt.legend(["Model Three", "APC data"])

plt.tight_layout()
plt.show()