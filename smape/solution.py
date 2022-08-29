"""Solution of task 03 SMAPE level Intern."""
import numpy as np


def smape(y_true: np.array, y_pred: np.array) -> float:
    """
    Calcualate SMAPE metric of model quality

    Parameters
    ----------
    y_true : np.array
        Real values
    y_pred : np.array
        Predicted values

    Returns
    -------
    float
        Metric SMAPE value

    """
    return np.mean(
        np.abs(y_pred - y_true) * 2 /
        np.where(
            (np.abs(y_pred) + np.abs(y_true)) == 0,
            0.00001,
            np.abs(y_pred) + np.abs(y_true))
    )
