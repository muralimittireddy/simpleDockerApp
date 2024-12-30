
from python:3.13
run pip install pandas pgcli psycopg2
workdir /app/
copy script.py script.py
# entrypoint ["python","script.py"]
