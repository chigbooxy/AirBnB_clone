#!/usr/bin/python3
"""Describes this module as a package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
