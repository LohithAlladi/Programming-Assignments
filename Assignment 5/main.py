from flight import Flight
from planner import Planner

def test_no_route():
    # def _init_(flight_no, start_city, departure_time, end_city, arrival_time, fare)
    flights = [
        Flight(0, 0, 0, 1, 50, 100),
        Flight(1, 1, 60, 2, 120, 150),
        Flight(2, 2, 130, 3, 200, 250)
    ]
    
    flight_planner = Planner(flights)
    # Try to find a route between cities with no connection
    # def least_flights_ealiest_route(start_city, end_city, t1, t2):
    route1 = flight_planner.least_flights_ealiest_route(0, 4, 0, 300)
    
    if route1 == []:
        print("Test Case 1 PASSED: No route available")
    else:
        print("Test Case 1 FAILED")

def test_tight_time_window():
    # def _init_(flight_no, start_city, departure_time, end_city, arrival_time, fare)
    flights = [
        Flight(0, 0, 10, 1, 50, 100),    # City 0 to 1
        Flight(1, 1, 70, 2, 100, 120),   # City 1 to 2
        Flight(2, 2, 150, 4, 200, 130),  # City 2 to 4
        Flight(3, 1, 70, 4, 140, 200),   # City 1 to 4 (tight window)
    ]
    
    flight_planner = Planner(flights)
    
    # Try to find a route within a tight window
    # def least_flights_ealiest_route(start_city, end_city, t1, t2):
    route2 = flight_planner.cheapest_route(0, 4, 10, 150)
    
    if route2 == [flights[0], flights[3]]:
        print("Test Case 2 PASSED: Route found within a tight time window")
    else:
        print("Test Case 2 FAILED")

def test_circular_routes():
    # def _init_(flight_no, start_city, departure_time, end_city, arrival_time, fare)
    flights = [
        Flight(0, 0, 0, 1, 40, 50),    # City 0 to 1
        Flight(1, 1, 60, 0, 100, 30),  # City 1 to 0 (loop)
        Flight(2, 1, 70, 2, 120, 90),  # City 1 to 2
        Flight(3, 2, 140, 3, 180, 80), # City 2 to 3
        Flight(4, 0, 10, 2, 130, 120), # City 0 to 2 directly (fixed flight number)
    ]
    
    flight_planner = Planner(flights)
    # def least_flights_ealiest_route(start_city, end_city, t1, t2):
    route3 = flight_planner.least_flights_cheapest_route(0, 3, 0, 300)
    
    if route3 == [flights[0], flights[2], flights[3]]:
        print("Test Case 3 PASSED: Correct route avoiding circular paths")
    else:
        print("Test Case 3 FAILED: InCorrect route avoiding circular paths")
        print(route3)
        for flight in route3:
            print(flight.flight_no)


def test_min_layover_time():
    flights = [
        Flight(0, 0, 0, 1, 50, 100),   # City 0 to 1
        Flight(1, 1, 65, 2, 120, 90),  # City 1 to 2 (insufficient layover)
        Flight(2, 1, 80, 2, 150, 120), # City 1 to 2 (sufficient layover)
        Flight(3, 2, 170, 3, 210, 200) # City 2 to 3
    ]
    
    flight_planner = Planner(flights)
    
    route4 = flight_planner.least_flights_ealiest_route(0, 3, 0, 300)
    
    if route4 == [flights[0], flights[2], flights[3]]:
        print("Test Case 4 PASSED: Correct route considering minimum layover time")
    else:
        print("Test Case 4 FAILED")

def test_multiple_optimal_routes():
    flights = [
        Flight(0, 0, 0, 1, 40, 100),   # City 0 to 1
        Flight(1, 0, 10, 2, 50, 100),  # City 0 to 2
        Flight(2, 1, 60, 3, 100, 80),  # City 1 to 3
        Flight(3, 2, 70, 3, 110, 80),  # City 2 to 3
        Flight(4, 1, 60, 3, 110, 75)   # Another 1 to 3 (same arrival as above)
    ]
    
    flight_planner = Planner(flights)
    
    route5 = flight_planner.cheapest_route(0, 3, 0, 200)
    
    if route5 == [flights[0], flights[4]] or route5 == [flights[1], flights[3]]:
        print("Test Case 5 PASSED: Handled multiple optimal routes")
    else:
        print("Test Case 5 FAILED")

if __name__ == "__main__":
    test_no_route()
    test_tight_time_window()
    test_circular_routes()
    test_min_layover_time()
    test_multiple_optimal_routes()