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

    df_arr[:, 1] = np.where(
        df_arr[:, 3] <= 0,
        0,
        df_arr[:, 1]
    )

    df_arr[:, 1] = np.where(
        df_arr[:, 2] <= 0,
        0,
        df_arr[:, 1]
    )

    df_arr[:, 1] = np.where(
        df_arr[:, 1] < 0,
        0,
        df_arr[:, 1]
    )

    df_arr[:, 1] = np.where(
        np.floor(df_arr[:, 1] / df_arr[:, 2]) > df_arr[:, 3],
        df_arr[:, 2] * df_arr[:, 3],
        df_arr[:, 1]
    )

    df_arr[:, 1]  = np.where(
        df_arr[:, 1] %  df_arr[:, 2] != 0,
        np.floor(df_arr[:, 1] / df_arr[:, 2]) * df_arr[:, 2],
        df_arr[:, 1]
    )

    return pd.DataFrame(
        {
            'sku': df_arr[:, 0],
            'gmv': np.float64(df_arr[:, 1]),
            'price': np.float64(df_arr[:, 2]),
            'stock': df_arr[:, 3],
        }
    )
