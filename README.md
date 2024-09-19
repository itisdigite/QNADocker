# QNADocker
This is a Docker repo for qna

# Here we are creating dockerfile so our qna-frontend and qna-backend should be here in same location.
    - following is the folder structure

```bash
├── qna-backend/
├── qna-frontend/
├── db
├── Dockerfile
├── docker-compose.yml
```

# To Build the image run following command
- docker compose build --no-cache

# To run the whole setup
- docker compose up -d