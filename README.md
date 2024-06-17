# Setting Up

## Create env
```shell
conda create --name <PROEJCT NAME> python=3.10
```

```shell
conda activate <PROEJCT NAME>
```

## Install dependencies
```shell
pip install -r requiriments.txt
```

# Setup Alembic
## Generate Initial Migration
```shell
alembic revision --autogenerate -m "Initial migration"
```

## Apply Migrations
```shell
alembic upgrade head
```

# Run the Application
```shell
python main.py
```