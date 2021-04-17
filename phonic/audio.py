"""
Audio Blueprint.

"""

# Flask Imports.
from flask import Blueprint, request

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


@audio_bp.route("/audio/<audioFileType>/<audioFileID>", methods=["POST"])
def post_audio(audioFileType, audioFileID):
    """
    POST Audio.

    Parameters
    ----------
    audioFileType: str
        Audio File Type
    audioFileID: int
        Audio File ID

    Returns
    -------
    response: json.
        Row Added to the Database.

    """

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
        title = request.json["title"]
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
