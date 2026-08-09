# MoveX Backend

MoveX Backend

MoveX Backend is a pet project created for learning and practicing backend development.

MoveX is a ride-hailing service inspired by the Uber model. Passengers can request rides by specifying a pickup point and destination, while drivers can accept available ride requests and transport passengers to their destinations.

The project focuses on implementing the backend part of such a service, including authentication, ride management, drivers, users, payments, and other supporting functionality.

The main goal of the project is to gain practical experience with backend development, system architecture, REST APIs, databases, authentication, and related technologies.

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* PostGIS
* Redis
* Pydantic
* JWT
* Docker
* uv

## Requirements

* Python 3.13+
* Docker
* Docker Compose
* uv

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd movex-backend
```

Install dependencies:

```bash
uv sync
```

Create the environment file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Start PostgreSQL and Redis:

```bash
docker compose up -d
```

Apply database migrations:

```bash
uv run alembic upgrade head
```

## Run

Start the application:

```bash
uv run python -m src.main
```

The API will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Documentation

Project documentation is available in the [`docs`](/docs) directory.

It contains the project vision, business requirements, domain model, database design, use cases, and API specification.
