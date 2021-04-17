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
    Song Data Model.

    """
    # todo: validate as a required field.

    id = db.Column(db.Integer,
                   unique=True,
                   primary_key=True,
                   autoincrement=True,
                   nullable=True)

    name = db.Column(db.String(100),
                     nullable=True)

    duration = db.Column(db.Integer,
                         nullable=True)

    uploaded_time = db.Column(db.DateTime,
                              default=datetime.datetime.utcnow(),
                              nullable=True)

    def __init__(self, name, duration, uploaded_time):
        """
        Init Song Data Model.

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


class Podcast(db.Model):
    """
    Podcast Data Model.

    """
    # todo: Add Column Validation Layer to Podcast.

    id = db.Column(db.Integer,
                   unique=True,
                   autoincrement=True,
                   primary_key=True,
                   nullable=True)

    name = db.Column(db.String(100),
                     nullable=True)

    duration = db.Column(db.Integer,
                         nullable=True)

    uploaded_time = db.Column(db.Datetime,
                              defualt=datetime.datetime.utcnow(),
                              nullable=True)

    host = db.Column(db.String(100),
                     nullable=False)

    participants = db.Column(db.PickleType,
                             nullable=False)

    def __init__(self, name, duration, uploaded_time, host, participants):
        """
        Init Podcast Data Model.

        Parameters
        ----------
        name: str, max = 100 char
            Name of the Podcast
        duration: int
            Duration of the Podcast
        uploaded_time: datetime, default = Current time UTC
            DataTime of the file upload
        host: str, max = 100 char
            Name of the Podcast Host.
        participants: pkl (list of string), max = 10 participants.
            Name of Participants.

        """
        self.name = name
        self.duration = duration
        self.uploaded_time = uploaded_time
        self.host = host
        self.participants = participants


class AudioBook(db.Model):
    """
    AudioBook Data Model.

    """
    # todo: Add Column Validation Layer to Audiobook.

    id = db.Column(db.Integer,
                   unique=True,
                   autoincrement=True,
                   primary_key=True,
                   nullable=True)

    title = db.Column(db.String(100),
                      nullable=True)

    author = db.Column(db.String(100),
                       nullable=True)

    narrator = db.Column(db.String(100),
                         nullable=True)

    duration = db.Column(db.Integer,
                         nullable=True)

    uploaded_time = db.Column(db.Datetime,
                              defualt=datetime.datetime.utcnow(),
                              nullable=True)

    def __init__(self, title, author, narrator, duration, uploaded_time):
        """
        Init Podcast Data Model.

        Parameters
        ----------
        title: str, max = 100 char
            Title of the Audiobook.
        author: str, max = 100 char
            Author of the Audiobook.
        narrator: str, max = 100 char
            Narrator of the Audiobook.
        duration: int
            Duration of the Podcast
        uploaded_time: datetime, default = Current time UTC
            DataTime of the file upload

        """
        self.title = title
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.uploaded_time = uploaded_time