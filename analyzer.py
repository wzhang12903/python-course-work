def calculate_average(df):
    return df["Score"].mean()

def highest_score(df):
    return df["Score"].max()

def lowest_score(df):
    return df["Score"].min()
