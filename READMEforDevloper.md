# QNADocker
This is a QNADocker repo 

## Clone the Repository

To get started, clone the repository using Git. Open a terminal (Command Prompt/PowerShell for Windows, Terminal for Linux/macOS) and run:

```bash
git clone https://github.com/itisdigite/QNADocker.git
```

# Here we are creating dockerfile, so our qna-frontend and qna-backend should be in QNADocker folder.
NOTE: Don't copy unnecessary files from qna-backend and frontend. Copy only those which shown in below folder structure.
```bash

QNADocker
├── db
│   └── init.sql
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── qna-backend
│   ├── login_page.py
│   └── requirements.txt
├── qna-frontend
│   ├── static
│   │   ├── register.css
│   │   ├── style.css
│   │   └── verify.css
│   └── templates
│       ├── login.html
│       ├── register.css
│       ├── register.html
│       └── verification.html
└── README.md
     
```

# Changes in qna-backend/login_page.py 
1. We will change host entry here to host='db' from host="127.0.0.1".
2. Also comment the init_db() function. For docker we are running one init.sql file via entrypoint to create the Database, tables & to grant permissions to user.

After changes your file looks like
Please verify it with your file

```bash
from flask import Flask, request, render_template, redirect, url_for # type: ignore
import mysql.connector
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import datetime
import bcrypt
#from db import init_db  # Import the init_db function

# Initialize the database before starting the app
#init_db()

app = Flask(__name__, 
            static_folder='../qna-frontend/static', 
            template_folder='../qna-frontend/templates')

def get_db_connection():
    return mysql.connector.connect(
        host='db',  # Connect to the MySQL container on localhost
        user='qnauser',
        password='Pass@000',
        database='qna'
    )
```


# To Build the image run following command
- docker compose build --no-cache

NOTE: Verify nothing is already running on port 8000 and 3306.
If your local mysql server is running then stop it using > systemctl stop mysql

# To run the whole setup
- docker compose up -d

# To see the application logs
- docker logs -f qna-app

# Access the application
Click on Running on http://127.0.0.1:8000 url shown in app logs 