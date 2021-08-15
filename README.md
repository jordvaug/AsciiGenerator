# ASCII Art Generator

The ASCII art generator is a python/flask application that will generate ASCII art from an uploaded image. It uses a homebaked LRU cache written to a text file to maintain object persistence between calls and application runs.

## Building the Application

First install required packages:

    On MacOS/Linux:
    python -m pip install -r requirements.txt

    On Windows:
    py -m pip install -r requirements.txt


Next create a virtual environment from which to run the application:

    On MacOS/Linux:
    python3 -m venv env

    On Windows:
    python -m venv env

## Running the Application

To run the API, simply run:
    python app.py

Unit tests can be run with:
    python -m unittest discover



## API Specification

The API has two endpoints, a home endpoint and one for uploading images. More info can be found in the postman collection below. Valid requests will respond with a 200 HTTP response. It uses a Least Recently Used (LRU) cache persisted in a text file to increase performance.


The postman collection can be imported as json from the Postman.json file in this project or by following the link below.


    Postman collection at:
    https://www.getpostman.com/collections/a85708a209d590b1d041


### Library Considerations
Flask was used to build this application due to its ability to rapidly deploy simple applications with built in debugging and unit test aiding, as the author's say: "Flask aims to keep the core simple but extensible". Flask has a strong community behind it -with 56k stars on their github project- and has been in development since 2004. It is a mature framework in use by large companies like LinkedIn and Pinterest.