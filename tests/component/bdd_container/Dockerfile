# Base image
FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libpq-dev \
  python3.7-dev \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/apt/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install the requirements before copying source code makes the subsequent docker builds faster. Wondering why?
RUN python3 -m pip install --upgrade pip
RUN pip install pip-tools requests fastapi pytest pytest-bdd psycopg2 azure-storage-blob

COPY ./component/bdd_container /component/bdd_container

WORKDIR /
ENV PYTHONPATH=/

CMD ["sh","component/bdd_container/bdd-startup.sh"]
