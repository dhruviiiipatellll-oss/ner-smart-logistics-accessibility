import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from typing import Dict, List

class CognitiveAssessmentModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = [
            'age', 'education_level', 'previous_cognitive_tests',
            'family_history', 'health_conditions', 'medication_count',
            'sleep_quality', 'physical_activity', 'social_engagement'
        ]
    
    def predict_cognitive_risk(self, patient_data: Dict) -> Dict:
        age = patient_data.get('age', 60)
        base_risk = min((age - 50) * 2, 95) if age >= 50 else 10
        return {
            "risk_probability": base_risk / 100,
            "risk_level": self._get_risk_level(base_risk),
            "confidence": 0.65,
            "recommendations": self._get_recommendations(base_risk)
        }
    
    @staticmethod
    def _get_risk_level(score: float) -> str:
        if score < 30:
            return "low"
        elif score < 70:
            return "medium"
        else:
            return "high"
    
    @staticmethod
    def _get_recommendations(risk_score: float) -> List[str]:
        recommendations = []
        if risk_score >= 50:
            recommendations.append("Schedule cognitive assessment with specialist")
            recommendations.append("Increase social engagement activities")
        if risk_score >= 70:
            recommendations.append("Consider cognitive therapy sessions")
            recommendations.append("Schedule MRI/CT scan if not done recently")
        recommendations.extend([
            "Maintain regular sleep schedule",
            "Engage in physical activity 30 minutes daily"
        ])
        return recommendations[:5]