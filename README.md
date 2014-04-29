# Damn Form

Backend for Form from Developer for Developer and Designer

### Install dependencies

Following steps are only needed one time

  1. npm install
  2. bower install
  3. virtualenv venv
  4. source venv/bin/activate
  5. pip install -r requirements.pip


### Run gulp to watch and compile Sass

To compile a sass

    gulp

To compile and watch for sass file changes

    gulp watch

### Run server

    export PYTHONPATH=$(pwd)/server/
    mongod
    python server.py
