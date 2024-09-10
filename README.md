# Eonia Backend Template (FastAPI)
## Setting Up

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
