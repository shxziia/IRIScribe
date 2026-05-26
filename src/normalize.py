def clean_data(df):

    df.columns = df.columns.str.strip()

    return df