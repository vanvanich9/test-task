FROM python:3.12-slim

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

COPY utils/wait_for_service.py ./wait_for_service.py

COPY __init__.py ./__init__.py
COPY __init__.py ./tests/__init__.py
COPY . /tests/functional

ENTRYPOINT ["./entrypoint.sh"]