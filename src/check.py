from ingest import load_csv

df = load_csv("data/cicids/Tuesday-WorkingHours.pcap_ISCX.csv")

df.columns = df.columns.str.strip()

print(df["Label"].value_counts().head(20))