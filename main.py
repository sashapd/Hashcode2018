class Ride():
    def __init__(self, a, b, x, y, start, end, indx):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.start = start
        self.end = end
        self.weight = 0
        self.indx = indx
        self.invalid = False

        self.connected = []
    def dist(self):
        return abs(self.a - self.x) + abs(self.b - self.y)
    def assignWeight(self):
        if any(self.connected):
            self.weight = self.dist() + max(n.weight for n in self.connected if n)
        else:
            self.weight = self.dist()

class Car():
    def __init__(self):
        self.x = 0
        self.y = 0

inpt = open('/Users/sashapd/c_no_hurry.in')
#inpt = open('/Users/sashapd/b_should_be_easy.in')
#inpt = open('/Users/sashapd/c_no_hurry.in')

rows, columns, carsN, ridesN, bonus, Tsteps = [int(s) for s in inpt.readline().split()]

rides = []
cars = []

for i in range(carsN):
    cars.append(Car())

for i in range(ridesN):
    a, b, x, y, s, f = [int(s) for s in inpt.readline().split()]
    rides.append(Ride(a, b, x, y, s, f, i))

rides.sort(key=lambda r: r.end)
print("Connecting rides")
i = 0
for ride in rides:
    i += 1
    print("Connected " + str(i) + " out of " + str(len(rides)))
    for r in rides:
        if ride is not r:
            distBetween = abs(ride.x - r.a) + abs(ride.y - r.b)
            if r.end >= ride.end + distBetween + r.dist():
                ride.connected.append(r)
                #ride.assignWeight()
print("Assigning weights")
i = 0
for ride in reversed(rides):
    i += 1
    print("Assigned " + str(i) + " out of " + str(len(rides)))
    ride.assignWeight()

#print("Processing cars")
i = 0
carsRides = []
for car in range(carsN):
    #print("Car " + str(i) + " out of " + str(len(cars)))
    i += 1
    currentRides = []
    ride = max(rides, key=lambda r: (r.weight if r and not r.invalid else -1))
    while True:
        if ride and not ride.invalid:
            currentRides.append(ride.indx)
            ride.invalid = True
            print("len connected"  + str(len(ride.connected)))
            if ride.connected:
                ride = max(ride.connected, key=lambda r: (r.weight if r and not r.invalid else -1))
            else:
                break
        else:
            break
    carsRides.append(currentRides)

output = open("/Users/sashapd/e_out.out", "w")
for i in range(len(carsRides)):
    output.write(str(len(carsRides[i])) + ' ' + ' '.join(str(n) for n in carsRides[i]) + "\n")

print(len(carsRides))
print(carsRides)



print("Finished")








