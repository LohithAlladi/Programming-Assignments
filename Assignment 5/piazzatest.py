from planner import Planner
from flight import Flight

def read_flights_from_file(filename):
    flights = []
    with open(filename, 'r') as file:
        # First line contains n (vertices) and m (edges)
        n, m = map(int, file.readline().strip().split())
        
        # Next m lines contain flight details
        for _ in range(m):
            # Parse each flight line as: flight_no, start_city, dep_time, end_city, arr_time, fare
            start_city, end_city,fare, dep_time, arr_time = map(int, file.readline().strip().split())
            # For simplicity, we're assigning the index as flight_no (0, 1, ...)
            flight_no = _
            #fare = 0  # Placeholder for fare if it's not provided
            
            # Create a Flight object and add to flights list
            flights.append(Flight(flight_no, start_city, dep_time, end_city, arr_time, fare))
    
    return flights, n, m

# Example usage
flights, n, m = read_flights_from_file('C_test.txt')
planner = Planner(flights)

# Define a test case
start_city = 0
end_city = 100
t1 = 0
t2 = 1000000

# # Run each route-finding method
print("Fewest Flights and Earliest Arrival Route:")
x = planner.least_flights_ealiest_route(start_city, end_city, t1, t2)
f=0
for i in x:
    print(i.flight_no,end=" ")
    print(" ")
    f+=i.fare
print(x[-1].arrival_time)

print("Cheapest Route:")
x=planner.cheapest_route(start_city, end_city, t1, t2)
f=0
#print(x)
for i in x:
    f+=i.fare
print(f)
print("Fewest Flights and Cheapest Route:")
x=planner.least_flights_cheapest_route(start_city, end_city, t1, t2)
f=0
#print(x)
for i in x:
    f+=i.fare
print(f)

# Define a test case
start_city = 0
end_city = 110
t1 = 0
t2 = 100000

# Run each route-finding method
print("Fewest Flights and Earliest Arrival Route:")
x=planner.least_flights_ealiest_route(start_city, end_city, t1, t2)
for i in x:
    print(i.flight_no,end=" ")
    print(" ")
    f+=i.fare
print(x[-1].arrival_time)
print("Cheapest Route:")
x=planner.cheapest_route(start_city, end_city, t1, t2)
f=0
#print(x)
for i in x:
    f+=i.fare
print(f)
print("Fewest Flights and Cheapest Route:")
x=planner.least_flights_cheapest_route(start_city, end_city, t1, t2)
f=0
#print(x)
for i in x:
    f+=i.fare
print(f)


'''
Fewest Flights and Earliest Arrival Route:
56057  
54551  
86153  
365
Cheapest Route:
15786123
Fewest Flights and Cheapest Route:
15786123
Fewest Flights and Earliest Arrival Route:
56057  
54551  
67938  
537
Cheapest Route:
17953837
Fewest Flights and Cheapest Route:
17953837
'''