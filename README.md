A simple sample application to check if an artist is related to another artist on Spotify.
The containerized API will return a 200 if found, a 404 if not found.

Run tests:
Create a virtualenv by running mkvirtualenv <name>
Install tox with 'pip install tox'
Run 'tox' to run tests and lint project

Flask:
(set rather than export on windows)
Set environment variabled with 'export FLASK_APP=src/app/py'
Set to development with 'export FLASK_ENV=development'
Start application with 'flask run'

Docker:
Build image with 'docker build -t app .'
Run the container with 'docker run app'

Usage:
Example request would be something like 'curl -i "http://localhost:5000/related?first_artist=jawbreaker&second_artist=cher"'