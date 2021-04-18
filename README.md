# phonic
[![Generic badge](https://img.shields.io/badge/Python-3.7.9-<COLOR>.svg)](https://shields.io/) 
[![Generic badge](https://img.shields.io/badge/TestCoverage-96percent-<COLOR>.svg)](https://shields.io/)

A Flask API that simulates the behavior of an audio file server while using a SQL database.

## Setup Instructions:

### Linux:
1. Create a Python virtual environment
> python3 -m venv phonic_env

2. Activate Virtual Environment
> source phonic_env/bin/activate

3. Install Requirements
> pip install -r requirements.txt

OR

4. Using Setup.py
> pip install -e

5. Setup Flask Configuration & Run.

> export FLASK_APP=phonic

> export FLASK_ENV=development

> flask run


### Windows:
1. Create a Python virtual environment
> python -m venv phonic_env

2. Activate Virtual Environment
> .\phonic_env\Scripts\activate

3. Install Requirements
> pip install -r requirements.txt

OR

4. Using Setup.py
> pip install -e

5. Setup Flask Configuration & Run.
> set FLASK_APP=phonic

> set FLASK_ENV=development

> flask run

# API Usage Guide
* API URI = "/api/audioFileType/audioFileID"
* Methods = GET, POST, PUT & DELETE
  

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
