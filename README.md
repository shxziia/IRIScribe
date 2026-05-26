# IRIScribe

# Objective
[Brief Objective]

This IRIScribe projects objectives is to analyze network traffic data and detect potential cyber attacks. This system aims to classify threats, assign severity levels, map them to MITRE ATT&CK framework, and present the results in an interactive dashboard. This is to simulate real world security monitoring and incident response.

# Skills Gained

- Cybersecurity fundamentals - SOC workflow
- Network traffic analysis
- Threat detection logic
- Data proccessing with Pandas
- Dashboard development with Streamlit
- MITRE ATT&CK framework mapping
- Risk score and incident classification

# Tools Used

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

  pip install -r requirments.txt
  streamlit run src/app.py
