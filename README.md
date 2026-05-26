# IRIScribe

## Objective
[Brief Objective]

This IRIScribe projects objectives is to analyze network traffic data and detect potential cyber attacks. This system aims to classify threats, assign severity levels, map them to MITRE ATT&CK framework, and present the results in an interactive dashboard. This is to simulate real world security monitoring and incident response.

## Skills Gained

- Cybersecurity fundamentals - SOC workflow
- Network traffic analysis
- Threat detection logic
- Data proccessing with Pandas
- Dashboard development with Streamlit
- MITRE ATT&CK framework mapping
- Risk score and incident classification

## Tools Used

- Python - used to build the whole project
- Pandas - used to read and process the data
- Streamlit - used to create the dashboard
- Plotly - used to make charts and graphs
- CICIDS2017 dataset - used as a data source for deteckting attacks

### How It Works

  1. Load the CICIDS2017 network traffic dataset. This contains real world network flow data which is used to simulate cybersecurity environments.
  2. Cleans and prepares the dataset which is used for analysis by handling and structuring raw network traffic features.
  3. Detects suspicious network activitybased on predefined attack patterns.
  4. Classifies different types of attacks such as brute force and scanning activities.
  5. Assigns severity levels and then calculates risk scores for each detected incident.
  6. Maps the detected attacks to MITRE ATT&CK framework.
  7. Generates structures incident reports for each detected threat.
  8. Displays all results on interactive SOC style Streamlit dashboard.
 
### How To Run

Run these command in the terminal:
pip install -r requirements.txt
streamlit run src/app.py

### CICIDS2017 Dataset

Download CICIDS2017 Dataset from:
https://www.unb.ca/cic/datasets/ids-2017.html

Due to the datasets large size, the dataset is not included in this repository.
  pip install -r requirments.txt
  streamlit run src/app.py

### SOC Dashboard Overview

Main SOC Dashboard:

<img width="1885" height="737" alt="image" src="https://github.com/user-attachments/assets/15999125-fd81-46e8-9930-4f4107baeae8" />

The main dashboard provides a high level overview of the detected network activity within the CICIDS2017 dataset. The dashboard displays key security metrics such as detected incidents, severity distribution, critical and high deverity alerts, and the average risk score. This represents the primary monitoring interface which is used to simulate a SOC environment where analysts can quickly assess the overall security status of the system.

Attack Type Distribution:

<img width="711" height="657" alt="image" src="https://github.com/user-attachments/assets/b9a6fc85-7ff2-4159-9f24-e1877d87b33a" />

This charts is a visualisation of the distribution of detected attack types within the dataset. This chart highlights which type of network attacks are most frequent such as brute force or scanning based intrusion. This chart helps to understand the dominant threat patterns present in the network traffic data.

Risk Score Distribution:

<img width="690" height="662" alt="image" src="https://github.com/user-attachments/assets/75b45bff-65f7-4142-8ed1-544a70f5b56c" />

This chart is used to display the distribution of risks crossed across all the detected incidents. The chart helps classify how severe each incident is and it shows how many low medium or high risk threats exist in the system. This helps prioritise Security events based on their potential impact. 

Incident Table:

<img width="1392" height="312" alt="image" src="https://github.com/user-attachments/assets/d7eb1b7a-76c6-465b-962e-1cb82856bf0d" />

The incident table provides a detailed breakdown of all the security incidents. Each incident includes the incident ID, attack type, number of occurrences, severity level, risk score, and MITRE ATT&CK classification. The incident table is used for deeper investigation and it simulates how SOC analysts would review and triage security incidents in real world environments. 
