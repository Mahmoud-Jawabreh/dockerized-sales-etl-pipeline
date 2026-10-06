# Dockerized Sales ETL Pipeline

A containerized ETL pipeline built with Python, Pandas, PostgreSQL, and Docker Compose.

The project extracts sales data from a CSV file, transforms it using Pandas, and loads the processed data into PostgreSQL. Docker Compose orchestrates the ETL and database services, including networking, database health checks, and persistent storage.

## Architecture

```text
             Docker Compose
                   |
        +----------+----------+
        |                     |
        v                     v
+---------------+      +---------------+
|  ETL Service  |      |  PostgreSQL   |
|               |      |               |
| Python        |----->| sales_db      |
| Pandas        |      | sales table   |
| SQLAlchemy    |      |               |
+-------+-------+      +-------+-------+
        |                      |
        v                      v
   sales.csv            Docker Volume
                       postgres_data
```

## ETL Workflow

### Extract

The pipeline reads sales transaction data from:

`data/sales.csv`

### Transform

Pandas calculates the total amount for each transaction:

```python
total_amount = quantity * price
```

### Load

The transformed DataFrame is loaded into a PostgreSQL `sales` table using SQLAlchemy and psycopg2.

## Technologies

- Python
- Pandas
- PostgreSQL 16
- SQLAlchemy
- psycopg2
- Docker
- Docker Compose

## Docker Features

This project demonstrates:

- Custom Docker image creation using a Dockerfile
- Multi-container orchestration with Docker Compose
- Container-to-container networking
- PostgreSQL health checks
- Service dependencies
- Named volumes for persistent database storage
- Environment-variable based configuration

## Project Structure

```text
.
├── data/
│   └── sales.csv
├── pipeline.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── .env.example
└── README.md
```

## Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create the environment file

Copy `.env.example` to `.env` and provide the PostgreSQL configuration:

```env
POSTGRES_USER=etl_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=sales_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

### 3. Build and start the pipeline

```bash
docker compose up --build -d
```

Docker Compose will:

1. Start PostgreSQL.
2. Wait until PostgreSQL passes its health check.
3. Build and start the Python ETL container.
4. Extract and transform the sales data.
5. Load the transformed data into PostgreSQL.

### 4. Check the services

```bash
docker compose ps -a
```

The PostgreSQL service should be healthy and the ETL service should finish successfully with exit code `0`.

### 5. View ETL logs

```bash
docker compose logs etl
```

### 6. Query the loaded data

Connect to PostgreSQL:

```bash
docker exec -it sales-postgres psql -U etl_user -d sales_db
```

Then run:

```sql
SELECT * FROM sales;
```

Example analytical query:

```sql
SELECT
    product,
    SUM(total_amount) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
```

### 7. Stop the application

```bash
docker compose down
```

The PostgreSQL data remains stored in the named Docker volume.

To also remove the volume:

```bash
docker compose down -v
```

## What I Learned

This project provided hands-on experience with building a complete containerized ETL workflow, including:

- Designing an Extract, Transform, Load pipeline
- Loading Pandas DataFrames into PostgreSQL
- Building Docker images for Python applications
- Connecting containers through Docker networking
- Managing multiple services with Docker Compose
- Persisting database data using Docker volumes
- Using health checks to coordinate dependent services
- Separating application configuration from source code using environment variables