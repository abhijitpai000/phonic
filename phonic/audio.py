"""
Audio Blueprint.

"""

# Flask Imports.
from flask import Blueprint, request, jsonify

# Local Imports.
from phonic import create_app
from phonic.models import init_db
from phonic.models import Song, Podcast, AudioBook
from phonic.models import SongSchema, PodcastSchema, AudioBookSchema

# Init Audio Blueprint.
audio_bp = Blueprint(name="audio",
                     import_name=__name__,
                     url_prefix="/api")

# Init Database.
app = create_app()
db = init_db(app)


@audio_bp.route("/<audioFileType>/<audioFileID>", methods=["POST"])
def post_audio(audioFileType, audioFileID):
    """
    POST Audio to the Database.

    CRUD Operation: CREATE

    Parameters
    ----------
    audioFileType: str, max = 100 char
        Audio File Type
    audioFileID: int
        Audio File ID

    Returns
    -------
    response: json.

    """
    # default response.
    response = jsonify({})

    if audioFileType == "song":
        id = audioFileID
        name = request.json["name"]
        duration = request.json["duration"]

        new_song = Song(id=id, name=name, duration=duration)

        # Add new song to db.
        db.session.add(new_song)
        db.session.commit()

        # Marshmallow Parser.
        new_song_schema = SongSchema()
        response = new_song_schema.jsonify(new_song)

    elif audioFileType == "podcast":
        id = audioFileID
        name = request.json["name"]
        duration = request.json["duration"]

        new_podcast = Podcast(id=id,
                              name=name,
                              duration=duration)

        # Add new podcast to db.
        db.session.add(new_podcast)
        db.session.commit()

        # Marshmallow Parser.
        new_podcast_schema = PodcastSchema()
        response = new_podcast_schema.jsonify(new_podcast)

    elif audioFileType == "audiobook":
        id = audioFileID
        title = request.json["name"]
        author = request.json["author"]
        narrator = request.json["narrator"]
        duration = request.json["duration"]

        new_audiobook = AudioBook(id=id,
                                  name=title,
                                  author=author,
                                  narrator=narrator,
                                  duration=duration)

        # Add new podcast to db.
        db.session.add(new_audiobook)
        db.session.commit()

        # Marshmallow Parser.
        new_audiobook_schema = AudioBookSchema()
        response = new_audiobook_schema.jsonify(new_audiobook)

    return response


@audio_bp.route("/<audioFileType>", methods=["GET"])
def get_audio(audioFileType):
    """
    GET all Audio of the audioFileType stored in the Database.

    CRUD Operation: READ

    Parameters
    ----------
    audioFileType: str, max = 100 char
        Audio File Type
    Returns
    -------
    response: json.

    """
    # default response.
    response = jsonify({})

    if audioFileType == "song":
        records = Song.query.all()
        songs_schema = SongSchema(many=True)
        response = songs_schema.jsonify(records)

    elif audioFileType == "podcast":
        records = Podcast.query.all()
        podcasts_schema = PodcastSchema(many=True)
        response = podcasts_schema.jsonify(records)

    elif audioFileType == "audiobook":
        records = AudioBook.query.all()
        audiobooks_schema = AudioBookSchema(many=True)
        response = audiobooks_schema.jsonify(records)

    return response


@audio_bp.route("/<audioFileType>/<audioFileID>", methods=["GET"])
def get_specific_audio(audioFileType, audioFileID):
    """
    GET specific Audio of the audioFileType stored in the Database.

    CRUD Operation: READ

    Parameters
    ----------
    audioFileType: str, max = 100 char
        Audio File Type

    audioFileID: int.
        Audio File ID.

    Returns
    -------
    response: json.

    """
    # default response.
    response = jsonify({})

    if audioFileType == "song":
        records = Song.query.get(audioFileID)
        song_schema = SongSchema()
        response = song_schema.jsonify(records)

    elif audioFileType == "podcast":
        records = Podcast.query.get(audioFileID)
        podcast_schema = PodcastSchema()
        response = podcast_schema.jsonify(records)

    elif audioFileType == "audiobook":
        records = AudioBook.query.get(audioFileID)
        audiobook_schema = AudioBookSchema()
        response = audiobook_schema.jsonify(records)

    return response
