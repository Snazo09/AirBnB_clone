#!/usr/bin/env python3
"""Module containing Review class implementation."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class."""

    place_id = ''
    user_id = ''
    text = ''
