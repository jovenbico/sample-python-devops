# sample-python-devops
Sample Python DevOps

## Setup
### Create Virtual Environment
```
# create venv
python3 -m venv .venv

# active venv
source .venv/bin/activate

# check python version installed in venv
python --version
| Python 3.11.9

# To deactive venv type
deactivate
```

## Run hello_to_python
```
./hello.py
./age.py
./bmi.py
./timer.py

export STAGE=Production && ./running.py
unset STAGE && ./running.py
```

## Run test slack_notify
```
set -a
. .env
set +a

python slack_notify/test.py
```