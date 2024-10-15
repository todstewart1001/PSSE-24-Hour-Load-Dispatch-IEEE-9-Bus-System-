import psspy

# Initialize PSSE
psspy.psseinit(9) 
psspy.case('IEEE-9.sav')

#Load profiles for each hour based on expected load patterns
load_profile = {
    5: [90, 95, 100, 110, 120, 130, 135, 140, 145, 150, 140, 130, 120, 110, 100, 90, 85, 80, 75, 70, 65, 60, 55, 50],  # MW at bus 5
    6: [100, 105, 110, 120, 130, 140, 145, 150, 155, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 65, 60, 55, 50, 45],  # MW at bus 6
    8: [125, 130, 135, 145, 155, 165, 170, 175, 180, 185, 175, 165, 155, 145, 135, 125, 115, 105, 95, 85, 75, 65, 55, 50]   # MW at bus 8
}

# Loop over 24 hours to run OPF at each hour and apply contingency at a specific hour
for hour in range(24):
    print("Running hour {}".format(hour+1))

    # Update loads for each hour at each load bus
    psspy.load_chng_5(5, "1", [1], [load_profile[5][hour]])  # Update bus 5 load
    psspy.load_chng_5(6, "1", [1], [load_profile[6][hour]])  # Update bus 6 load
    psspy.load_chng_5(8, "1", [1], [load_profile[8][hour]])  # Update bus 8 load

    # Calculate the total load for each hour (sum of load at buses 5, 6, and 8)
    total_load = load_profile[5][hour] + load_profile[6][hour] + load_profile[8][hour]

    # Set fixed generation for each generator
    psspy.machine_chng_2(1, '1', [1], [0.5 * total_load])  # Generator at Bus 1
    psspy.machine_chng_2(2, '1', [1], [0.3 * total_load])  # Generator at Bus 2
    psspy.machine_chng_2(3, '1', [1], [0.2 * total_load])  # Generator at Bus 3
    
    # Run load flow for the current hour
    ierr = psspy.fnsl([0,0,0,1,1,0,99,0])
    if ierr != 0:
        print("Power flow did not converge for hour {}".format(hour + 1))

    # Retrieve generator dispatch results
    ierr, generator_output = psspy.amachreal(-1, 4, 'PGEN')  # Generator real power output (MW)
    ierr, generator_bus_numbers = psspy.amachint(-1, 4, 'NUMBER')  # Bus numbers of generators

    print("Generator Dispatch for Hour {}".format(hour+1))
    for i in range(len(generator_bus_numbers[0])):
        print("Generator at Bus {}: {:.2f} MW".format(generator_bus_numbers[0][i], generator_output[0][i]))

    # Retrieve and print bus voltage results
    ierr, bus_voltages = psspy.abusreal(-1, 2, 'PU')  # Bus voltage in p.u.
    ierr, bus_numbers = psspy.abusint(-1, 2, 'NUMBER')  # Bus numbers

    print("\nBus Voltages (p.u.):")
    for i in range(len(bus_numbers[0])):
        print("Bus {}: {:.3f} p.u.".format(bus_numbers[0][i], bus_voltages[0][i]))
    
    # Retrieve real power (P) and reactive power (Q) flow on each branch
    # (-1 for all branches, 1 for in-service lines)
    ierr, real_power_from_to = psspy.abrnreal(-1, 1, 1, 1, 1, ['P'])   # MW flow from "from" bus to "to" bus
    ierr, reactive_power_from_to = psspy.abrnreal(-1, 1, 1, 1, 1, ['Q'])   # Mvar flow from "from" bus to "to" bus
    ierr, real_losses = psspy.abrnreal(-1, 1, 1, 1, 1, ['PLOSS'])  # Real power losses (MW)
    ierr, reactive_losses = psspy.abrnreal(-1, 1, 1, 1, 1, ['QLOSS'])  # Reactive power losses (MVAR)
 
    # Calculate power flow at the "to bus" side
    real_power_to_from = [real_losses[0][i] - real_power_from_to[0][i] for i in range(len(real_power_from_to[0]))]
    reactive_power_to_from = [reactive_losses[0][i] - reactive_power_from_to[0][i] for i in range(len(reactive_power_from_to[0]))]

    # Get the bus numbers of the branches
    ierr, from_buses = psspy.abrnint(-1, 1, 1, 1, 1, 'FROMNUMBER')  # Sending bus number
    ierr, to_buses = psspy.abrnint(-1, 1, 1, 1, 1, 'TONUMBER')      # Receiving bus number

    # Print line flow data
    print("Branch Flows (MW and Mvar):")
    for i in range(len(from_buses[0])):
        print("Line from Bus {} to Bus {}".format(from_buses[0][i], to_buses[0][i]))
        print("  MW flow (From -> To): {:.2f}, MW flow (To -> From): {:.2f}".format(real_power_from_to[0][i], real_power_to_from[i]))
        print("  Mvar flow (From -> To): {:.2f}, Mvar flow (To -> From): {:.2f}".format(reactive_power_from_to[0][i], reactive_power_to_from[i]))

    # Save snapshot of the system state for this hour
    psspy.save("ieee9_hour_{}.sav".format(hour+1))
