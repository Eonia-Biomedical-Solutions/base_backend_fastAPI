# Eonia Backend Template (FastAPI)

## Getting Started

### Clone the Repository

First, clone the repository using the command below:

```bash
git clone https://github.com/Eonia-Biomedical-Solutions/base_backend_fastAPI <YOUR PROJECT>
```

### Change Git Remote Origin

To set the correct remote origin for your project, use:

```bash
git remote set-url origin <YOUR GIT PROJECT LINK>
```

#### Verify the Remote URL:

To verify that you’ve added the correct link:

```bash
git remote -v
```

You should see output similar to the following:

```bash
origin  <YOUR GIT PROJECT LINK> (fetch)
origin  <YOUR GIT PROJECT LINK> (push)
```

### Create env
```shell
conda create --name <PROEJCT NAME> python=3.10
```

```shell
conda activate <PROEJCT NAME>
```

### Install dependencies
```shell
pip install -r requiriments.txt
```

## ENV
Create .env on core folder with the next data
```shell
ENV = development

DB_URL = <<DB URL>>
DB_PORT = <<DB PORT>>
DB_NAME = <<DB NAME>>
DB_PWD = <<DB PASSWORD>>
DB_USR = <<DB USER>>

SECRET_KEY = <<SECRET KEY>>
REFRESH_SECRET_KEY = <<REFRESH TOKEN SECRET KEY>>
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 1800
TIMEOUT = 60

MAIL_USERNAME = <<MAIL USERNAME>>
MAIL_PASSWORD = <<MAIL PASSWORD>>
MAIL_PORT = <<MAIL PORT>>
MAIL_SERVER = <<MAIL SERVER>>
MAIL_STARTTLS = true
MAIL_SSL_TLS = false
MAIL_FROM = <<EMAIL>>

```

### Generate Secret key
```shell
python -c "import os; print(os.urandom(24).hex())"
```

## Setup Alembic
### create directory versions
```shell
cd alembic 
mkdir versions
```
### Generate Initial Migration
```shell
alembic revision --autogenerate -m "Initial migration"
```

### Apply Migrations
```shell
alembic upgrade head
```

## Run the Application

### uvicorn
```shell
uvicorn app:app --reload
```

### fastapi
```shell
fastapi dev app
```

## Project Structure

The following is the project directory structure:

```
project/
│
├───api/
│   │   __init__.py
│   └───HelloWorld/
│       └───v1/
│           ├───request/
│           └───response/
│
├───app/
│   │   __init__.py
│
├───core/
│   ├───base/
│   ├───db/
│   ├───fastapi/
│   └───utils/
│
├───db_models/
│   │   __init__.py
│
```

### Directory Breakdown

- **api/**: Contains all the API endpoints and versioning.
  - **HelloWorld/**: Example endpoint for demonstration.
    - **v1/**: Version 1 of the API.
      - **request/**: Directory for request validation schemas (e.g., `say_my_name_request.py`).
      - **response/**: Directory for response models and formats (e.g., `say_my_name_response.py`).

- **app/**: Main application logic and entry point.

- **core/**: Contains essential services, configurations, and utilities.
  - **settings.py**: Application configuration and environment settings.
  - **base/**: Base classes such as enums, response models, and schema definitions.
  - **db/**: Database configurations and helpers.
    - **crud/**: Helper functions for Create, Read, Update, Delete operations (e.g., `crud.py`).
    - **table/**: Defines the base database table structure (e.g., `table.py`).
  - **fastapi/**: FastAPI-specific configurations like CORS settings and custom response handlers.
  - **utils/**: Utility functions such as token management (`token.py`) and password hashing (`hasher.py`).

- **db_models/**: Contains the definitions for database models.

## Contributions

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

---