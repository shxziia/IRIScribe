from ingest import load_csv
from normalize import clean_data
from detection import detect_attacks
import json
from datetime import datetime


def main():

    path = "data/cicids/Tuesday-WorkingHours.pcap_ISCX.csv"

    df = load_csv(path)
    df = clean_data(df)

    incidents = detect_attacks(df)

    print("\n==============================")
    print(" IRISCRIBE SOC INCIDENT REPORT")
    print("==============================\n")

    timeline = []

    for inc in incidents:

        print("\n------------------------------")
        print("INCIDENT ID :", inc["incident_id"])
        print("TYPE        :", inc["type"])
        print("COUNT       :", inc["count"])
        print("SEVERITY    :", inc["severity"])
        print("RISK SCORE  :", inc["risk_score"])
        print("MITRE       :", inc["mitre"])

        timeline.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event": inc["type"]
        })

    print("\nTOTAL INCIDENTS:", len(incidents))

    
    with open("reports/incidents.json", "w") as f:
        json.dump(incidents, f, indent=4)

    
    generate_html_report(incidents, timeline)

    print("\nReports saved in /reports")


def generate_html_report(incidents, timeline):

    html = """
    <html>
    <head>
        <title>IRIScribe SOC Report</title>
        <style>
            body { font-family: Arial; background: #111; color: #eee; }
            .card { background: #222; padding: 10px; margin: 10px; border-radius: 8px; }
            .critical { color: red; }
            .high { color: orange; }
            .medium { color: yellow; }
        </style>
    </head>
    <body>
        <h1>IRIScribe SOC Incident Report</h1>
    """

    for inc in incidents:

        html += f"""
        <div class='card'>
            <h2>{inc['incident_id']} - {inc['type']}</h2>
            <p>Count: {inc['count']}</p>
            <p>Severity: {inc['severity']}</p>
            <p>Risk Score: {inc['risk_score']}</p>
            <p>MITRE: {inc['mitre']}</p>
        </div>
        """

    html += "<h2>Timeline</h2>"

    for t in timeline:

        html += f"<p>{t['time']} to {t['event']}</p>"

    html += "</body></html>"

    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(html)


main()