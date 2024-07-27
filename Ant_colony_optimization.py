import numpy as np

class AntColony:
    def __init__(self, distances, n_ants, n_iterations, decay_rate=0.5, alpha=1, beta=2, evaporation_rate=0.5):
        self.distances = distances
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay_rate = decay_rate
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.n_cities = len(distances)
        self.pheromones = np.ones((self.n_cities, self.n_cities))
        
    def run(self):
        best_path = None
        best_distance = float('inf')
        for _ in range(self.n_iterations):
            paths = self._generate_paths()
            self._update_pheromones(paths)
            current_best_path, current_best_distance = self._find_best_path(paths)
            if current_best_distance < best_distance:
                best_path = current_best_path
                best_distance = current_best_distance
        return best_path, best_distance
    
    def _generate_paths(self):
        paths = []
        for _ in range(self.n_ants):
            path = self._generate_path()
            paths.append(path)
        return paths
    
    def _generate_path(self):
        path = []
        visited = set()
        current_city = np.random.randint(self.n_cities)
        path.append(current_city)
        visited.add(current_city)
        for _ in range(self.n_cities - 1):
            next_city = self._select_next_city(current_city, visited)
            path.append(next_city)
            visited.add(next_city)
            current_city = next_city
        return path
    
    def _select_next_city(self, current_city, visited):
        probabilities = self.pheromones[current_city] ** self.alpha * \
                        ((1.0 / self.distances[current_city]) ** self.beta)
        probabilities[list(visited)] = 0
        probabilities /= probabilities.sum()
        next_city = np.random.choice(range(self.n_cities), p=probabilities)
        return next_city
    
    def _update_pheromones(self, paths):
        self.pheromones *= (1 - self.evaporation_rate)
        for path in paths:
            path_length = self._calculate_path_length(path)
            for i in range(self.n_cities - 1):
                self.pheromones[path[i], path[i+1]] += 1.0 / path_length
            self.pheromones[path[-1], path[0]] += 1.0 / path_length
            
    def _calculate_path_length(self, path):
        length = 0
        for i in range(len(path) - 1):
            length += self.distances[path[i], path[i+1]]
        length += self.distances[path[-1], path[0]]
        return length
    
    def _find_best_path(self, paths):
        best_path = None
        best_distance = float('inf')
        for path in paths:
            path_length = self._calculate_path_length(path)
            if path_length < best_distance:
                best_path = path
                best_distance = path_length
        return best_path, best_distance

# Example usage:
if __name__ == "__main__":
    # Define distances between cities (example data)
    distances = np.array([[0, 10, 15, 20],
                          [10, 0, 35, 25],
                          [15, 35, 0, 30],
                          [20, 25, 30, 0]])

    # Initialize the ACO algorithm
    aco = AntColony(distances, n_ants=10, n_iterations=100)

    # Run the ACO algorithm
    best_path, best_distance = aco.run()

    # Print the best path found
    print("Best Path:", best_path)
    print("Best Distance:", best_distance)
