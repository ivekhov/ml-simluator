import numpy as np
import pandas as pd


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
    first = np.clip(
        df_arr[:, 1],
        df_arr[:, 1],
        df_arr[:, 2] * df_arr[:, 3]
    )
    sec = np.clip(
        first,
        a_min = 0,
        a_max = np.floor(first / df_arr[:, 2]) * df_arr[:, 2]
    )

    result = np.where(sec < 0, 0, sec)

    return pd.DataFrame(
        {
            'sku': np.int64(df_arr[:, 0]),
            'gmv': np.float64(result),
            'price': np.float64(df_arr[:, 2]),
            'stock': np.int64(df_arr[:, 3])
        }
    )
