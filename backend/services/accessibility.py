from geopy.distance import geodesic
from typing import List, Tuple

class AccessibilityService:
    @staticmethod
    def calculate_accessibility_score(
        facility_latitude: float,
        facility_longitude: float,
        avg_population_density: float,
        services_offered: int,
        telemedicine_enabled: bool,
        doctors_count: int,
        beds_available: int
    ) -> float:
        score = 0.0
        service_score = min(services_offered * 10, 30)
        score += service_score
        if telemedicine_enabled:
            score += 20
        resource_score = min((doctors_count * 5 + beds_available * 2) / 10, 30)
        score += resource_score
        if avg_population_density > 0:
            coverage_score = min((100 / (avg_population_density / 10)), 20)
            score += coverage_score
        return round(min(score, 100), 2)
    
    @staticmethod
    def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        return geodesic((lat1, lon1), (lat2, lon2)).kilometers