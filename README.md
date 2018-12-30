# StackOverflow-V2

StackOverflow-Lite-Api is a simple question and answer platform.
--------------------------------------------------------------------
**Find the web UI here:**
https://github.com/kathy254/StackOverflow-Lite-UI


The project is managed using a Pivotal Tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2231025)

Getting started
--------------------
1. Clone this repository
```
    https://github.com/kathy254/StackOverflow-V2.git
```

2. Navigate to the cloned repository

Pre-requisites
----------------------
1. Python3
2. Flask
3. Postman
4. Flask-restplus
5. PostgreSQL
6. Psycopg2-binary

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install git-all
```

4. cd into this folder
```
    cd StackOverflow-V2
```

5. Create the development database
```
    createdb stackoverflow_db
```

6. Create the test database
```
    createdb test_db
```

7. Switch to 'develop' branch
```
    git checkout develop
```

8. Install requirements
```
    pip install -r requirements.txt
```

Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following api endpoints using postman
-----------------------------------------------

**Unrestricted endpoints**

| Endpoint | Functionality |
----------|---------------
GET /index | View all questions and answers
POST /auth/signup | Register a user
POST /auth/login | Login a user

**Restricted endpoints**

Endpoint | Functionality
---------|---------------
GET /questions | Fetch all questions
GET /questions/&lt;questionID&gt; | Fetch a specific question
POST /questions | Post a question
DELETE /questions/&lt;questionID&gt; | Delete a question
POST /questions/&lt;questionID&gt;/answers | Post an answer to a question
PUT /questions/&lt;questionID&gt;/answers/&lt;answerId&gt; | Mark an answer as accepted, or edit an answer

Resources used
-----------------
- [Travis-ci](https://travis-ci.org)
- [Coveralls](https://coveralls.io)
- [Code climate](https://codeclimate.io)
- [Codacy](https://app.codacy.com)
- Python
- Flask
- Flask-restplus
- PostgreSQL

Authors
-----------------------------
**Catherine Omondi** - _Initial work_-[kathy254](https:/github.com/kathy254)

License
--------------------------
This project is licensed under the MIT license. See [LICENSE](https://github.com/kathy254/StackOverflow-Lite-Api/blob/master/LICENSE) for details.

Acknowledgements
--------------------------------
1. Headfirst Labs
2. Andela Workshops
