import math
import numpy as np
import pandas as pd


def vect_gmv(arr):
    """
    Calculates updated gmv.

    Parameters
    ----------
    arr : numpy array
        Array with varibales. Elements of array: [0] - sku, [1] - gmv, [2] - price, [3] - stock.

    Returns
    -------
    int
        Updated value of gmv

    """
    if arr[1] <= 0:
        return 0
    if arr[2] < 0:
        return 0
    if arr[3] <= 0:
        return 0

    if arr[1] > (arr[2] * arr[3]):
        return arr[2] * arr[3]

    if arr[1] % arr[2] != 0:
        return math.floor(arr[1] / arr[2]) * arr[2]

    return arr[1]


def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Update gmv in data frame by checking counts stored.

    Parameters
    ----------
    df : pd.DataFrame
        Starter dataframe

    Returns
    -------
    pd.DataFrame
        New data frame with metric updated

    """
    df_arr = np.array(df)
    gmv_upd = np.apply_along_axis(func1d=vect_gmv, axis=1, arr=df_arr)

    return pd.DataFrame(
        {
            'sku': df_arr[:, 0],
            'gmv': gmv_upd,
            'price': df_arr[:, 2],
            'stock': df_arr[:, 3],
        }
    )
