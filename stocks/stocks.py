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

    res = np.where(
        df_arr[:, 1] > df_arr[:, 2] * df_arr[:, 3],
        df_arr[:, 2] * df_arr[:, 3],
        df_arr[:, 1]
    )

    res = np.where(
        res % df_arr[:, 2] != 0,
        np.floor(
            res / df_arr[:, 2]
        ) * df_arr[:, 2],
        res
    )

    res = np.where(
        df_arr[:, 3] <= 0,
        0,
        res
    )

    res = np.where(
        df_arr[:, 2] <= 0,
        0,
        res
    )

    res = np.where(
        res < 0,
        0,
        res
    )
    return pd.DataFrame(
        {
            'sku': df_arr[:, 0],
            'gmv': res,
            'price': np.float64(df_arr[:, 2]),
            'stock': df_arr[:, 3],
        }
    )
