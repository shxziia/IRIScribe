import streamlit as st
import pandas as pd
import plotly.express as px

from ingest import load_csv
from normalize import clean_data
from detection import detect_attacks


st.set_page_config(
    page_title="IRIScribe SOC Console",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
    }
    h1 {
        color: #00ffcc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("IRIScribe SOC Console")

st.caption("Real-time Incident Analysis Dashboard (CICIDS2017)")


DATA_PATH = "data/cicids/Tuesday-WorkingHours.pcap_ISCX.csv"

df = load_csv(DATA_PATH)
df = clean_data(df)

incidents = detect_attacks(df)

if not incidents:
    st.error("No incidents detected.")
    st.stop()

inc_df = pd.DataFrame(incidents)


st.sidebar.header("Controls")

severity_filter = st.sidebar.multiselect(
    "Severity Filter",
    options=inc_df["severity"].unique(),
    default=list(inc_df["severity"].unique())
)

type_filter = st.sidebar.multiselect(
    "Attack Type",
    options=inc_df["type"].unique(),
    default=list(inc_df["type"].unique())
)

min_risk = st.sidebar.slider("Minimum Risk Score", 0, 100, 0)

filtered = inc_df[
    (inc_df["severity"].isin(severity_filter)) &
    (inc_df["type"].isin(type_filter)) &
    (inc_df["risk_score"] >= min_risk)
]


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Incidents", len(filtered))
col2.metric("Critical", len(filtered[filtered["severity"] == "CRITICAL"]))
col3.metric("High", len(filtered[filtered["severity"] == "HIGH"]))
col4.metric("Avg Risk Score", round(filtered["risk_score"].mean(), 2))

st.divider()


left, right = st.columns(2)

with left:
    st.subheader("Attack Type Distribution")
    fig1 = px.pie(filtered, names="type", title="")
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.subheader("Risk Score Distribution")
    fig2 = px.bar(filtered, x="type", y="risk_score", color="severity")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()


st.subheader("Incident Table")

def color_severity(val):
    if val == "CRITICAL":
        return "color: red; font-weight: bold"
    elif val == "HIGH":
        return "color: orange; font-weight: bold"
    elif val == "MEDIUM":
        return "color: yellow"
    else:
        return "color: white"

styled_df = filtered.style.map(color_severity, subset=["severity"])

st.dataframe(styled_df, use_container_width=True)


with st.expander("View Raw Incident JSON"):
    st.json(filtered.to_dict(orient="records"))