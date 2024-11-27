from flight import Flight
from ds import*

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        # No.of cities take O(m)
        self.n = max(max([flight.start_city for flight in flights]) , max([flight.end_city for flight in flights])) + 1
        # No.of flights take O(1)
        self.m = len(flights)
        # Initiating adjacency list takes O(n) or O(m)
        self.flights_from_city = [[] for _ in range(self.n)]
        # Adjacency list with index as starting city
        for flight in flights:
            self.flights_from_city[flight.start_city].append(flight)
        
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        if start_city == end_city:
            return []
        
        queue = Queue()
        # Initiate the Queue
        queue.enqueue((None,start_city, 0, 0))
        
        PathMap = HashMap(self.m)

        visited = [[] for _ in range(self.n)]

        least_flights = float('INF')

        req_path = None

        while not queue.is_empty():

            current_flight, current_city, last_arrival, path = queue.dequeue()

            if path < least_flights:
                # Try all possible next flights from this city
                possible_flights = self.flights_from_city[current_city]

                for flight in possible_flights:
                    # Check if this is a valid next flight
                    if path == 0:  # First flight
                        if flight.departure_time < t1 or flight.arrival_time > t2:
                            continue
                    else:  # Connecting flight
                        if flight.departure_time < last_arrival + 20 or flight.arrival_time > t2:
                            continue

                    new_path = (flight, flight.arrival_time)

                    PathMap.insert((new_path,(current_flight,last_arrival)))
                    
                    if flight.end_city == end_city:
                        if req_path == None or req_path[0].arrival_time > flight.arrival_time :
                            req_path = new_path
                            least_flights = path + 1
    
                    if flight.arrival_time not in visited[flight.end_city]:
                        visited[flight.end_city].append(flight.arrival_time)
                        queue.enqueue((flight, flight.end_city, flight.arrival_time, path+1))

        f_path = []
        while req_path is not None and req_path[0] is not None:
            f_path.append(req_path[0])
            req_path = PathMap.find(req_path)
        
        return f_path[::-1] 
    
    def compare_fares(self,t1,t2):
        return t1[3]<t2[3] 
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        if start_city == end_city:
            return []
        
        stack = Heap(self.compare_fares,[(start_city, 0, 0, 0, None)])

        visited = [[] for _ in range(self.n)]

        req_path = None

        PathMap = HashMap(self.m)

        least_fare = float('INF')

        while stack.init_array:
            current_city, last_arrival, path, fare, current_flight = stack.extract()
            
            # Try all possible next flights from this city
            possible_flights = self.flights_from_city[current_city]

            for flight in possible_flights:
                # Check if this is a valid next flight
                if path == 0:  # First flight
                    if flight.departure_time < t1 or flight.arrival_time > t2:
                        continue
                else:  # Connecting flight
                    if flight.departure_time < last_arrival + 20 or flight.arrival_time > t2:
                        continue
                
                new_path = (flight, flight.arrival_time)
                new_fare = fare + flight.fare

                PathMap.insert((new_path,(current_flight,last_arrival)))
                
                if flight.end_city == end_city:
                        if req_path == None or least_fare > new_fare :
                            req_path = new_path
                            least_fare = new_fare

                if flight.arrival_time not in visited[flight.end_city]:
                        visited[flight.end_city].append(flight.arrival_time)
                        stack.insert((flight.end_city, flight.arrival_time, path+1, new_fare, flight))
            
        f_path = []
        while req_path is not None and req_path[0] is not None:
            f_path.append(req_path[0])
            req_path = PathMap.find(req_path)
        
        return f_path[::-1]
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        if start_city == end_city:
            return []
        
        queue = Queue()
        # Initiate the Queue
        queue.enqueue((None,start_city, 0, 0, 0))
        
        PathMap = HashMap(self.m)

        visited = [[] for _ in range(self.n)]

        least_flights = float('INF')

        req_path = None

        least_fare = 0 

        while not queue.is_empty():

            current_flight, current_city, last_arrival, path, fare = queue.dequeue()

            if path < least_flights:
                # Try all possible next flights from this city
                possible_flights = self.flights_from_city[current_city]

                for flight in possible_flights:
                    # Check if this is a valid next flight
                    if path == 0:  # First flight
                        if flight.departure_time < t1 or flight.arrival_time > t2:
                            continue
                    else:  # Connecting flight
                        if flight.departure_time < last_arrival + 20 or flight.arrival_time > t2:
                            continue

                    new_path = (flight, flight.arrival_time)
                    new_fare = fare + flight.fare 

                    PathMap.insert((new_path,(current_flight,last_arrival)))

                    if flight.end_city == end_city:
                        if req_path == None or least_fare > new_fare :
                            req_path = new_path
                            least_flights = path + 1
                            least_fare = new_fare 
    
                    if flight.arrival_time not in visited[flight.end_city]:
                        visited[flight.end_city].append(flight.arrival_time)
                        queue.enqueue((flight, flight.end_city, flight.arrival_time, path+1, new_fare))
                        
        f_path = []
        while req_path is not None and req_path[0] is not None:
            f_path.append(req_path[0])
            req_path = PathMap.find(req_path)
        
        return f_path[::-1]