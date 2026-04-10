import pandas as pd

def load_data(filename):
    """Load CSV data safely."""
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print("Error loading file:", e)
        return None
    