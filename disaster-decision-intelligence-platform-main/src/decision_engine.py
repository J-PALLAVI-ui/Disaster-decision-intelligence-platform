from typing import Dict, List


class DecisionEngine:

    @staticmethod
    def analyze(
        magnitude: float,
        depth: float,
        temperature: float,
        humidity: float
    ) -> Dict:

        # =====================================================
        # Emergency Level & Priority
        # =====================================================

        if magnitude >= 7.5:
            level = "RED"
            priority = "P1 - CRITICAL"

        elif magnitude >= 6.0:
            level = "ORANGE"
            priority = "P2 - HIGH"

        elif magnitude >= 4.5:
            level = "YELLOW"
            priority = "P3 - MEDIUM"

        else:
            level = "GREEN"
            priority = "P4 - LOW"

        # =====================================================
        # Risk Score (0–100)
        # =====================================================

        risk_score = 0

        # Magnitude (60%)
        risk_score += min(magnitude * 8, 60)

        # Depth (20%)
        if depth <= 20:
            risk_score += 20
        elif depth <= 70:
            risk_score += 12
        else:
            risk_score += 5

        # Weather (20%)

        if temperature >= 35:
            risk_score += 10

        if humidity >= 80:
            risk_score += 10

        risk_score = round(min(risk_score, 100), 2)

        # =====================================================
        # Estimated Response Time
        # =====================================================

        if level == "RED":
            response_time = "Immediate (0-15 minutes)"

        elif level == "ORANGE":
            response_time = "Within 30 minutes"

        elif level == "YELLOW":
            response_time = "Within 1 hour"

        else:
            response_time = "Routine monitoring"

        # =====================================================
        # Recommended Actions
        # =====================================================

        actions: List[str] = []

        if level == "GREEN":

            actions = [
                "Continue monitoring seismic activity",
                "Store event in database",
                "Update monitoring dashboard"
            ]

        elif level == "YELLOW":

            actions = [
                "Notify local authorities",
                "Monitor possible aftershocks",
                "Inspect public utilities",
                "Update emergency dashboard"
            ]

        elif level == "ORANGE":

            actions = [
                "Notify emergency response teams",
                "Alert nearby districts",
                "Inspect bridges, hospitals and schools",
                "Prepare evacuation shelters",
                "Monitor aftershocks continuously"
            ]

        else:

            actions = [
                "Activate Disaster Management Center",
                "Deploy emergency response teams",
                "Issue public emergency alerts",
                "Begin evacuation of high-risk zones",
                "Inspect critical infrastructure",
                "Coordinate medical response",
                "Monitor aftershocks continuously"
            ]

        # =====================================================
        # Risk Description
        # =====================================================

        if risk_score >= 80:
            description = "Extreme Risk"

        elif risk_score >= 60:
            description = "High Risk"

        elif risk_score >= 40:
            description = "Moderate Risk"

        else:
            description = "Low Risk"

        # =====================================================
        # Final Output
        # =====================================================

        return {

            "predicted_risk_score": risk_score,

            "risk_description": description,

            "emergency_level": level,

            "priority": priority,

            "estimated_response_time": response_time,

            "recommended_actions": actions

        }