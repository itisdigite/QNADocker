## Download the QNADocker application image from Docker Hub
- docker pull aishvaryabirambole/qnadocker-app

## Change the tag of that image
- docker tag aishvaryabirambole/qnadocker-app:latest qnadocker-app:latest

## Now Clone the Repository

To get started, clone the repository using Git. Open a terminal (Command Prompt/PowerShell for Windows, Terminal for Linux/macOS) and run:

```bash
git clone https://github.com/itisdigite/QNADocker.git
```

## After clonning your QNADOCKER folder structure looks like

```bash
QNADocker
├── db
│   └── init.sql
├── docker-compose.yml
├── Dockerfile
├── LICENSE
└── README.md

```

NOTE: Verify nothing is already running on port 8000 and 3306.
If your local mysql server is running then stop it using > systemctl stop mysql

# To run the whole setup
- docker compose up -d

# To see the application logs
- docker logs -f qna-app

# Access the application
Click on Running on http://127.0.0.1:8000 url shown in app logs
