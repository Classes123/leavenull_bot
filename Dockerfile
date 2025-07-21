FROM    python:3.12-alpine

ENV     PYTHONUNBUFFERED=1

WORKDIR /home

COPY    ["./requirements.txt", "./"]

RUN     pip install -r ./requirements.txt && rm ./requirements.txt

COPY    ["./src/config.py", "./src/main.py", "./src/phrases.py", "./"]

CMD     ["python3", "./main.py"]
