# from __future__ import annotations
from dataclasses import dataclass

class ModelError(Exception):
    """Base class for model-related exceptions."""
    pass

@dataclass(unsafe_hash=True)
class User:
    id: int
    name: str