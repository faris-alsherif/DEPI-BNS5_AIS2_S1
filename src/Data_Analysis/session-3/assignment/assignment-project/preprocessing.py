import pandas as pd

def Read_data_file(file_path: pd.DataFrame):
    """
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: Unable to read the file. {e}")
        return None

def Drop_unnecessary_features(df: pd.DataFrame, cols_to_drop: dict[str]):
    """
    """
    df.drop(cols_to_drop, axis=1, inplace=True)
    return df

def Check_data_type(df: pd.DataFrame):
    """
    """
    return pd.DataFrame({"Columns name":df.columns, "Dtypes":df.dtypes, "Num_uniqe": df.nunique()}).T