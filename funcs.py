import pandas as pd
import numpy as np

def InfoColumns(df):
    d = {"column_name": [], "dtype":[], "Null_Values": []}
    for c in df.columns:
        col = pd.isnull(df[c])
        d["column_name"].append(c)
        d["dtype"].append(df[c].dtype)
        d["Null_Values"].append(np.shape(df[col])[0])
    dd = pd.DataFrame(d)
    return dd