class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_routes = set()

        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses

            for route in stop_to_routes[stop]:
                if route not in visited_routes:
                    visited_routes.add(route)
                    for next_stop in routes[route]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses + 1))

        return -1
