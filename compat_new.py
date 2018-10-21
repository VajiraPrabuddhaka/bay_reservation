from constraint import *

problem = Problem()

flight_names = ['MI428', 'UL867', 'QR664', 'TK730', 'UL303']
flight_times = ['T-' + name for name in flight_names]
times = range(18)

bays_list = ['A1', 'A2', 'B1', 'B2', 'C1']

problem.addVariables(flight_names, bays_list)
problem.addVariables(flight_times, times)

bay_compat = {'MI428': ['A1', 'A2', 'B1'], 'UL867': ['B1', 'B2'], 'QR664': ['A2', 'B1', 'B2'], 'TK730': ['C1', 'A1'],
              'UL303': ['B2', 'C1']}

def func(bay, flight, bay_compat):
    return bay in bay_compat[flight]

for flight in flight_names:
    problem.addConstraint(lambda fl: fl in bay_compat[flight].copy(), [str(flight)])

time_constraints = {'T-MI428':(1,3) , 'T-UL867':(4,7), 'T-QR664':(8,9), 'T-TK730':(15,16), 'T-UL303':(16,17)}

# for flight_time in flight_times:
#     start, end = time_constraints[flight_time]
#     problem.addConstraint(lambda fl: fl in range(start, end+1), [flight_time])

for flight_one, time_one in zip(flight_names, flight_times):
    for flight_two, time_two in zip(flight_names, flight_times):
        if flight_one == flight_two:
            continue
        problem.addConstraint(
            lambda fl_one, t_one, fl_two, t_two: fl_one != fl_two or t_one != t_two,
            [flight_one, time_one, flight_two, time_two]
        )

solutions = problem.getSolutions()

print(solutions)

