class Flight:

    def __init__(self, flight_name, reg_no, aircraft_type, arrival_time, departure_time, no_passengers):
        self.flight_name = flight_name
        self.reg_no = reg_no
        self.aircraft_type = aircraft_type
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.no_passengers = no_passengers


class Bay:

    def __init__(self, bay_id, bridged, compat):
        # bridged & occupancy must be a boolean variables and compat will be list of strings

        self.compat = compat
        self.bay_id = bay_id
        self.bridged = bridged
