FROM python:3.10-slim-buster

RUN python3 -m pip install pip==23.0.1
RUN pip install fastapi uvicorn[standard]

# Copy the required source code and change the working directory
COPY ./component/mock_container/mock_app.py /

WORKDIR /

ENV PYTHONPATH=/

CMD ["uvicorn", "mock_app:app", "--host", "0.0.0.0", "--port", "8086"]
