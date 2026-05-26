from collections import defaultdict

def detect_attacks(df):

    grouped = defaultdict(int)

    for _, row in df.iterrows():

        label = str(row["Label"]).strip()

        if label.upper() == "BENIGN":
            continue

        grouped[label] += 1

    incidents = []
    incident_id = 1

    for label, count in grouped.items():

        severity, score = classify(label)
        mitre = mitre_mapping(label)

        incidents.append({
            "incident_id": f"IR-{incident_id:03d}",
            "type": label,
            "count": count,
            "severity": severity,
            "risk_score": score,
            "mitre": mitre
        })

        incident_id += 1

    return incidents


def classify(label):

    label = label.lower()

    if "ddos" in label:
        return "CRITICAL", 95

    if "dos" in label:
        return "HIGH", 80

    if "patator" in label:
        return "HIGH", 75

    if "portscan" in label:
        return "MEDIUM", 60

    return "LOW", 30


def mitre_mapping(label):

    label = label.lower()

    if "patator" in label:
        return "T1110 - Brute Force"

    if "portscan" in label:
        return "T1595 - Active Scanning"

    if "ddos" in label:
        return "T1498 - Network DoS"

    if "dos" in label:
        return "T1499 - Endpoint DoS"

    return "T0000 - Unknown"