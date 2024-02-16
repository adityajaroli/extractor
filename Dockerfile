FROM python:3.10-slim-buster

RUN apt-get update && apt-get install --assume-yes \
  gcc \
  libpq-dev \
  python3.7-dev \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/apt/*

RUN groupadd --gid 1001 c_user
RUN useradd --create-home --shell /bin/bash  --uid 1100 --gid 1001 c_user

RUN python3 -m pip install --upgrade pip
RUN pip install pip-tools fastapi uvicorn[standard] pandas azure-storage-blob pyarrow pg-bulk-loader

# Copy the required source code and change the working directory
COPY ./src ./src
WORKDIR /

ENV PYTHONPATH=/
USER 1100

CMD ["uvicorn", "src.extractor_app:app", "--host", "0.0.0.0", "--port", "8085"]
