from flight import Flight
from planner import *

f = open("C_test.txt", "r")
str = f.readline()
n, m = [int(i) for i in str.split()]
flights = []
for i in range(m):
    line = f.readline()
    start_city, end_city, cost, departure_time, arrival_time = [int(i) for i in line.split()]
    flight = Flight(i, start_city, departure_time, end_city, arrival_time, cost)
    flights.append(flight)

flight_planner = Planner(flights)

route1 = flight_planner.least_flights_ealiest_route(0, 110, 0, float('INF'))
print(route1)

route2 = flight_planner.least_flights_cheapest_route(0, 110, 0, float('INF'))
print(route2)

route3 = flight_planner.cheapest_route(0, 100, 0, float('INF'))
print(route3)

print('Done')