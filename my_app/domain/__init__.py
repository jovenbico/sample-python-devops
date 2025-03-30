"""
my_app.domain
================
This module contains the domain logic for the application.
"""

import logging
from logging import NullHandler

from .model import ModelError, User

__all__ = [
    "ModelError",
    "User",
]

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())