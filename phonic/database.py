"""
Module with Initial Database Instance.

"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
