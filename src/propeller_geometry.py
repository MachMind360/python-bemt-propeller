import numpy as np

def propeller_geometry_creation(geometry_file_path, number_of_blades):
    """Loads the given propeller data in the specified format and returns 
    elemental cord, pitch, solidity and stations with hub radius, tip radius and number of blades"""
    df_geom = np.loadtxt(geometry_file_path)

    chord = df_geom[:, 1]/39.37
    propeller_pitch = df_geom[:, 7]*(np.pi/180)
    hub_radius = df_geom[0, 0]/39.37
    tip_radius = df_geom[-1, 0]/39.37

    elements = len(df_geom)
    division = (tip_radius - hub_radius)/elements
    r = np.linspace(hub_radius, tip_radius, elements)

    solidity = number_of_blades*df_geom[:, 1]/(2*np.pi*df_geom[:, 0])     

    prop_geom = {
        "chord": chord,
        "prop_pitch": propeller_pitch,
        "rhub": hub_radius,
        "rtip": tip_radius,
        "division": division,
        "r": r,
        "solidity": solidity,
        "B": number_of_blades
    }

    return prop_geom

def freestream_data(performance_file_path):
    """Loads the experimental data of the propeller in the specified format 
    if available and returns the freestream velocity, measured thrust, torque, power and efficiency"""
    df_perf = np.loadtxt(performance_file_path)
    free_stream_velocity = df_perf[:, 0]/2.237 #The code requires freestream velocity infromation

    try:
        #Experimental thrust data is optional, can be inputted if comparison is required
        thrust = df_perf[:, 10]
        torque = df_perf[:, 9]
        power = df_perf[:, 8]
        eta = df_perf[:, 2]

        free_stream_data = {
        "vinf": free_stream_velocity,
        "thrust": thrust,
        "torque": torque,
        "power": power,
        "eff": eta
        }
        
        return free_stream_data

    except ValueError:
        free_stream_data = {
        "vinf": free_stream_velocity,
        }
        
        return free_stream_data

def renolds_number_finder(geometry_file_path, performance_file_path, nu):
    """Returns the calculated Reynold's number at 70% cord length"""
    df_geom = np.loadtxt(geometry_file_path)
    vinf = freestream_data(performance_file_path)
    seventy_percent = round(len(vinf["vinf"])*0.7)
    seventy_percent_cord = df_geom[round(len(df_geom[:, 1])*0.7), 1]
    velocity_at_seventy_percent_cord = vinf["vinf"][seventy_percent]

    Re = np.sqrt((60)**2 + velocity_at_seventy_percent_cord**2)*seventy_percent_cord/nu

    return Re
