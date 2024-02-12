#!/usr/bin/python3
"""Module contains the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city model"""
    state_id = ""
    name = ""
