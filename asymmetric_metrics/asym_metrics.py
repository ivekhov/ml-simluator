"""Module for life-time value task. Level Intern. Task 7-1."""
import numpy as np


def turnover_error(y_true: np.array, y_pred: np.array) -> float:
    '''
    Calculate metric of quality for retail orders.

    Parameters
    ----------
    y_true : Numpy array
            Values of real labels.

    y_pred : Numpy array
            Predicted values.

    Returns
    -------
    float
        Quality metric of prediction.

    '''
    return np.mean(np.where(y_pred < y_true, np.abs(y_true - y_pred), np.abs(y_true - y_pred) ** 2))
