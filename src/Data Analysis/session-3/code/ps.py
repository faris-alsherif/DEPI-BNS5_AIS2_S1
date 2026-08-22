import pandas as pd

def uniqe(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    dtypes = df.dtypes
    n_uniq = df.nunique()
    return pd.DataFrame({"Dtypes":dtypes, "Num_uniqe": n_uniq })