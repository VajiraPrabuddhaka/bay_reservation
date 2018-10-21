from constraint import *
import bay_resv_algo


problem = Problem()

flights, bays, occupied_bays, un_occupied_bays = bay_resv_algo.read_data('data/Research_Wimali.xlsx')

flight_names = []
for flight in flights:
    flight_names.append(flight.flight_name)

bays_list = []
for bay in bays:
    bays_list.append(bay.bay_id)



problem.addVariables(flight_names, bays_list)

time_constraints = {'MI428':(1,3) , 'UL867':(4,7), 'QR664':(8,9), 'TK730':(15,16), 'UL303':(16,17)}
problem.addConstraint(lambda MI428: 'A1' in ['A1', 'A2'], ["MI428"])
solutions = problem.getSolutions()

print (solutions)

