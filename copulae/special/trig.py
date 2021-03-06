import numpy as np

from copulae.types import Numeric


def cospi(x: Numeric):
    """
    Cosine function where every element is multiplied by pi.

    .. math::

        cospi(x) = cos(x * pi)

    Parameters
    ----------
    x: array like
        Input array in degrees

    Returns
    -------
    ndarray
        The corresponding cosine values. This is a scalar if x is a scalar.
    """
    return np.cos(x * np.pi)


def cospi2(x: Numeric):
    """
    Cosine function where every element is multiplied by pi / 2.

    .. math::

        cospi(x) = cos(x * pi / 2)

    Parameters
    ----------
    x: array like
        Input array in degrees

    Returns
    -------
    ndarray
        The corresponding cosine values. This is a scalar if x is a scalar.
    """
    return np.cos(x * np.pi / 2)


def sinpi(x: Numeric):
    """
    Sine function where every element is multiplied by pi.

    .. math::

        sinpi(x) = sin(x * pi)

    Parameters
    ----------
    x: array like
        Input array in degrees

    Returns
    -------
    ndarray
        The corresponding sine values. This is a scalar if x is a scalar.
    """
    return np.sin(x * np.pi)


def sinpi2(x: Numeric):
    """
    Sine function where every element is multiplied by pi / 2.

    .. math::

        sinpi(x) = sin(x * pi / 2)

    Parameters
    ----------
    x: array like
        Input array in degrees

    Returns
    -------
    ndarray
        The corresponding sine values. This is a scalar if x is a scalar.
    """
    return np.sin(x * np.pi / 2)


def tanpi(x: Numeric):
    """
    Tangent function where every element is multiplied by pi.

    .. math::

        tanpi(x) = tan(x * pi)

    Parameters
    ----------
    x: array like
        Input array in degrees

    Returns
    -------
    ndarray
        The corresponding tangent values. This is a scalar if x is a scalar.

    """
    return np.tan(x * np.pi)


def tanpi2(x: Numeric):
    """
    Tangent function where every element is multiplied by pi / 2.

    .. math::

        tanpi(x) = tan(x * pi / 2)

    Parameters
    ----------
    x: array like
        Input array in degrees

    Returns
    -------
    ndarray
        The corresponding Tangent values. This is a scalar if x is a scalar.
    """
    return np.tan(x * np.pi / 2)
