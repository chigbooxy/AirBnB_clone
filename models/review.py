#!/usr/bin/python3
"""Module contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Review model"""
    place_id = ""
    user_id = ""
    text = ""
