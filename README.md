## Codebase Walkthrough

### Code organization 

- **data** - raw data and sql scripts for making postgres tables and importing data from CSV into postgres.
- **flask-datastore** - backend for serving data from postgres. Depends on **postgres**.
- **flask-backend** - backend for serving data to frontend. Uses **flask-datastore** as data repository. Depends on **flask-datastore**.
- **react-app** - React app for displaying results. Depends on **flask-backend**

### Running the app

```bash
docker-compose build
docker-compose up react_app
```

Visit "http://localhost:8080"

### Running backend tests

Run tests only after running previous docker compose run command to have all the dependencies started.
Trying to run **flask-backend** tests without starting whole stack first, sometimes on the first run some tests that depend on **flask-datasore** will fail because of the race conditions. Just rerun command again.

#### flask-datastore

```bash
docker-compose -f docker-compose.yml run --rm  --entrypoint "python -m pytest tests" flask_datastore
```

#### flask-backend

```bash
docker-compose -f docker-compose.yml run --rm  --entrypoint "python -m pytest tests" flask_backend
```
