"""Solution of task 05 Cold start level Intern."""
import pandas as pd


def fillna_with_mean(df: pd.DataFrame, target: str, group: str) -> pd.DataFrame:
    """Replace NaN values by mean grouped.

    Parameters
    ----------
    df: pd.DataFrame
        Dataframe with NaNs
    target : str
        Value field with NaNs for cleaning
    group : str
        Field from which mean data is taken for missed in target

    Returns
    -------
    pd.DataFrame
        New dataframe with result

    """
    result = df.copy()
    result[target] = result.groupby(group)[target].transform(lambda x: x.fillna(x.mean()))
    return result
