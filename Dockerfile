FROM python:3.12-slim as core

WORKDIR /opt/app
RUN groupadd -r app-user && useradd -d /opt/app -r -g app-user app-user \
    && chown app-user:app-user -R /opt/app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt


FROM core as isort

RUN pip install isort==5.13.2
COPY . .
USER app-user
CMD ["isort", "--check", "."]


FROM core as style

RUN pip install flake8==7.0.0
COPY . .
USER app-user
CMD ["flake8", "."]


FROM core as app

EXPOSE 8000

COPY src .
USER app-user
ENTRYPOINT ["gunicorn", "--bind", ":8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]