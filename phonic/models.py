"""
Module to Define Database Tables & Schemas.

Tables
------
- Song
- Podcast
- Audiobook

Schemas
-------
# todo: Add Schemas overview.

"""
# Standard Imports.
import datetime

# Local Imports.
from phonic import db, ma


class Song(db.Model):
    """
    Class for creating Song Table.

    """
    # todo: validate as a required field.

    id = db.Column(db.Integer,
                   unique=True,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    uploaded_time = db.Column(db.DateTime,
                              default=datetime.datetime.utcnow())

    def __init__(self, name, duration, uploaded_time):
        """
        Init Song Table.

        Parameters
        ----------
        name: str, max = 100 char
            Name of the song
        duration: int
            Duration of the song
        uploaded_time: datetime, default = Current time UTC
            DataTime of the file upload

        """
        self.name = name
        self.duration = duration
        self.uploaded_time = uploaded_time
