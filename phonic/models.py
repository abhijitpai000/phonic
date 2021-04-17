"""
Module to Define Database Data Models & Schemas.

Tables & Schemas
----------------
- Song
- Podcast
- Audiobook

"""
# Standard Imports.
import datetime

# Local Imports.
from phonic.database import db
from phonic.schema import ma


class Base(db.Model):
    """
    Base Class for Phonic Data Models.
    """
    __abstract__ = True

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
        Base Data Model.

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


class Song(Base):
    """
    Song Data Model.

    """

    # todo: validate as a required field.

    def __init__(self):
        """
        Init Song Data Model.

        """
        super(Song, self).__init__()


class Podcast(Base):
    """
    Podcast Data Model.

    """
    # todo: Add Column Validation Layer to Podcast.

    host = db.Column(db.String(100),
                     nullable=False)

    participants = db.Column(db.PickleType,
                             nullable=False)

    def __init__(self, host, participants):
        """
        Init Podcast Data Model.

        Parameters
        ----------
        host: str, max = 100 char
            Name of the Podcast Host.
        participants: pkl (list of string), max = 10 participants.
            Name of Participants.

        """
        super(Podcast, self).__init__()

        self.host = host
        self.participants = participants


class AudioBook(Base):
    """
    AudioBook Data Model.

    """
    # todo: Add Column Validation Layer to Audiobook.

    author = db.Column(db.String(100),
                       nullable=True)

    narrator = db.Column(db.String(100),
                         nullable=True)

    def __init__(self, name, author, narrator):
        """
        Init Podcast Data Model.

        Parameters
        ----------
        name: str, max = 100 char
            Title of the Audiobook.
        author: str, max = 100 char
            Author of the Audiobook.
        narrator: str, max = 100 char
            Narrator of the Audiobook.

        """
        super(AudioBook, self).__init__()
        self.name = name
        self.author = author
        self.narrator = narrator


class SongSchema(ma.Schema):
    """
    Song Data Model Schema

    """

    class Meta:
        fields = ("id", "name", "duration", "uploaded_time")


class PodcastSchema(ma.Schema):
    """
    Podcast Data Model Schema

    """

    class Meta:
        fields = ("id", "name", "duration", "uploaded_time", "host", "participants")


class AudioBookSchema(ma.Schema):
    """
    Audiobook Data Model Schema

    """

    class Meta:
        fields = ("id", "name", "author", "narrator", "duration", "uploaded_time")


def init_db(app):
    """
    Create Databases using Schemas Defined.

    Parameters
    ----------
    app: object.
        Flask App Instance.

    Returns
    -------
    db: object.
        Database Instance.
    """

    # Create Tables.
    with app.app_context():
        db.create_all()
        db.session.commit()

    return db
