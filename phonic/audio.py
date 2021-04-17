"""
Audio Blueprint.

"""

# Flask Imports.
from flask import Blueprint

# Local Imports.
from phonic import create_app
from phonic.models import init_db

# Init Audio Blueprint.
audio_bp = Blueprint(name="audio",
                     import_name=__name__,
                     url_prefix="/api")

# Init Database.
app = create_app()
db = init_db(app)


@audio_bp.route("/audio/<audioFileType>/<audioFileID>", methods=["GET"])
def post_audio(audioFileType, audioFileID):
    """
    POST Audio.

    Parameters
    ----------
    audioFileType: str
        Audio File Type
    audioFileID: int
        Audio File ID

   """
    return "Hello!"
