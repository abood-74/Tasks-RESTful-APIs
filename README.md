## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API Endpoints](#api-endpoints)
## General info
This project is simple for creating tasks, editing it and deleting it.
## Technologies
Project is created with:
* Django version: 4.2.2
* python version: Python 3.7
## Setup

to run this project you need to have python and poetry (package manager) installed on your machine

  cloning the project 
  ```bash
        git clone "[repo link](https://github.com/abood-74/Tasks-RESTful-APIs/)"
        cd "Tasks-RESTful-APIs"
  ```

- if you have poetry installed on your machienthen run the following commands
  ```bash
        poetry install 
        poetry shell
        python manage.py makemigrations && python manage.py migrate
        python manage.py runserver
  ```
    </br>
- if you don't have poetry installed on your machine (you are using pip)
  ```bash 
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        python manage.py makemigrations && python manage.py migrate
        python manage.py runserver
## API Endpoints

| Method          | Endpoint | Description                                |
|-------------------------|--------|--------------------------------------|
| GET | `/api/tasks` | To retrieve all tasks |
| POST | `/api/tasks/` | To create a task |
| GET | `/api/tasks/:taskId` | To retrieve a task by its ID |
| PUT | `/api/tasks/:taskId` | To edit the details of a single task  |
| PATCH | `/api/tasks/:taskId` | To edit the details of a single task  |
| DELETE | `/api/tasks/:causeId` | To delete a single task |
| GET | `/swagger` | well documented API endpoints of the project |





