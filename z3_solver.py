from z3 import *

# Flights
Flight, (MI428, UL867, QR664, TK730, UL303) = EnumSort('Flight', ('MI428', 'UL867', 'QR664', 'TK730', 'UL303'))
flights = [MI428, UL867, QR664, TK730, UL303]

# Planes
Plane, (B320, B777, B235) = EnumSort('Plane', ('B320', 'B777', 'B235'))

# Bays
Bay, (A1, A2, B1, B2, C1) = EnumSort('Bay', ('A1', 'A2', 'B1', 'B2', 'C1'))
bays = [A1, A2, B1, B2, C1]

# Get a solver
s = Solver()

# Mapping flights to planes
plane = Function('plane', Flight, Plane)
gh = plane(MI428) == B320
s.add(plane(MI428) == B320)
s.add(plane(UL867) == B320)
s.add(plane(QR664) == B777)
s.add(plane(TK730) == B235)
s.add(plane(UL303) == B235)

# Bay constraints. Here're we're assuming a B320 can only land in A1 or A2,
# A B777 can only land on C1, and a B235 can land anywhere.
compatible = Function('compatible', Plane, Bay, BoolSort())

def mkCompat(p, bs):
    s.add(And([(compatible(p, b) if b in bs else Not(compatible(p, b))) for b in bays]))

mkCompat(B320, [A1, A2])
mkCompat(B777, [C1])
mkCompat(B235, bays)

# Allocation function
allocate = Function('allocate', Flight, Bay)
s.add(And([compatible(plane(f), allocate(f)) for f in flights]))
s.add(Distinct([allocate(f) for f in flights]))

# Get a model:
if s.check() == sat:
   m = s.model()
   print ([(f, m.eval(allocate(f))) for f in flights])
else:
   print ("Cannot find a satisfying assignment")