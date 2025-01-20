'''Utility functions for calculating angle-based metrics'''


def angle_distance(a, b):
    '''A function that takes in two angles and returns the
    absolute values of the interior angle between them.

    Parameters
    ----------
    a : float
        The first angle in degrees
    b : float
        The second angle in degrees

    Returns
    -------
    d : float
        The absolute value of the interior angle between a and b
        in degrees
    '''
    return abs(b - a)
