import random
from datetime import datetime, timedelta

SEVERITIES = ["SEV-1 (Critical)", "SEV-2 (High)", "SEV-3 (Medium)"]
SYSTEMS = [
    "Authentication Service",
    "Payment Gateway",
    "Database Cluster",
    "API Gateway"
]
ROOT_CAUSES = [
    "Memory leak after deployment",
    "Database connection pool exhaustion",
    "Misconfigured load balancer",
    "Expired SSL certificate",
    "Unexpected traffic spike"
]

def generate_incident():
    start_time = datetime.now() - timedelta(hours=random.randint(1, 24))
    end_time = start_time + timedelta(minutes=random.randint(15, 180))

    return {
        "incident_id": f"INC-{random.randint(1000,9999)}",
        "severity": random.choice(SEVERITIES),
        "system": random.choice(SYSTEMS),
        "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
        "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
        "impact": f"{random.randint(5, 80)}% users affected",
        "root_cause": random.choice(ROOT_CAUSES),
        "resolution": "Service restarted and configuration corrected",
        "preventive_action": "Add monitoring alerts and improve pre-deployment testing"
    }
