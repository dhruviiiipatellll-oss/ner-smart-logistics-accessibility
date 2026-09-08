import numpy as np
from sklearn.cluster import KMeans
from typing import List, Tuple, Dict

class LogisticsOptimizer:
    def __init__(self, num_vehicles: int = 10):
        self.num_vehicles = num_vehicles
    
    def optimize_supply_routes(
        self,
        depot_location: Tuple[float, float],
        facilities: List[Dict],
        demands: List[int],
        vehicle_capacity: int = 500
    ) -> Dict:
        routes = []
        current_load = 0
        current_route = [depot_location]
        
        for facility, demand in zip(facilities, demands):
            if current_load + demand > vehicle_capacity:
                current_route.append(depot_location)
                routes.append(current_route)
                current_route = [depot_location, facility]
                current_load = demand
            else:
                current_route.append(facility)
                current_load += demand
        
        if current_route:
            current_route.append(depot_location)
            routes.append(current_route)
        
        return {
            "routes": routes,
            "num_vehicles_used": len(routes),
            "total_demand": sum(demands),
            "optimization_method": "greedy"
        }
    
    def cluster_elderly_patients(
        self,
        patients: List[Dict],
        num_clusters: int = 5
    ) -> Dict:
        if not patients or len(patients) < num_clusters:
            return {"clusters": [], "error": "Insufficient data"}
        
        coordinates = np.array([[p['latitude'], p['longitude']] for p in patients])
        kmeans = KMeans(n_clusters=min(num_clusters, len(patients)), random_state=42)
        clusters = kmeans.fit_predict(coordinates)
        
        clustered_data = {}
        for idx, cluster_id in enumerate(clusters):
            if cluster_id not in clustered_data:
                clustered_data[cluster_id] = []
            clustered_data[cluster_id].append(patients[idx])
        
        return {
            "clusters": clustered_data,
            "num_clusters": len(clustered_data),
            "cluster_centers": kmeans.cluster_centers_.tolist()
        }