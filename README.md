# Python Flask, Celery and MongoDB
This is a simple app written in Python Flask with MongoDB mongodb database.
Celery is used to manage task queue.


### Run App (python 3)
Below are the steps required to run this app successfully... good luck.

##### `creation of virtual environment by executing the command venv`
>$ python3 -m venv /path-to-project/venv3

>$ source ./venv3/bin/activate

##### `install requirements`
>$ pip install -r requirement.txt


##### `run flask app (in debug mode)`
>$ python run.py


##### `run celery task queue (in debug mode)`
>$ celery worker -A app.celery --loglevel=debug
