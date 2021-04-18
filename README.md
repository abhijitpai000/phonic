# phonic
A Flask API that simulates the behavior of an audio file server while using a SQL database.

## Repository Structure
    .
    └── phonic/                    # phonic application directory.
        ├── __init__.py            # phonic Flask Application Factory.
        ├── audio.py               # API Blueprint with views.
        ├── models.py              # Backend Data Models.
        └── schema.py              # Marshmallow Schema Parser init.
    ├── tests/                     # Automated Test Cases.
        ├── conftest.py            # pytest testing fixtures configuration.
        ├── test_api_delete.py     # Test Cases for DELETE (DELETE Operation) of the API.
        ├── test_api_get.py        # Test Cases for GET (READ Operation) of the API.
        ├── test_api_post.py       # Test Cases for POST (CREATE Operation) of the API.
        ├── test_api_put.py        # Test Cases for PUT (UPDATE Operation) of the API.
        ├── test_database.py       # Test Case for checking if Database file is created.
        └── test_factory.py        # Test Case for checking if Application Factory accepts external configuration.
    ├── setup.cfg                  # Setup Configuration File for testing & development.   
    ├── setup.py                   # Setup file for distribution file generation.
    └── requirements.txt           # Project Requirements
