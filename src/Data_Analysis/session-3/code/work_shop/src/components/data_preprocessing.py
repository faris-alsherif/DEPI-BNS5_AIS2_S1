import pandas as pd
from config.config import drop_columns
def uniqe(df: pd.DataFrame) -> pd.DataFrame:
    """
    """
    dtypes = df.dtypes
    n_uniq = df.nunique()
    return pd.DataFrame({"Dtypes":dtypes, "Num_uniqe": n_uniq })

def drop_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    """
    return df.drop(columns = cols)