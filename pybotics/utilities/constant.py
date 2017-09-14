"""Constants used in pybotics."""
from enum import Enum


class Constant(Enum):
    """Constant class."""

    GRAVITY = -9.80665,  # m/s^2, ISO 80000-3
    TRANSFORM_MATRIX_SHAPE = (4, 4),
    TRANSFORM_VECTOR_LENGTH = 6,
    POSITION_VECTOR_LENGTH = 3
